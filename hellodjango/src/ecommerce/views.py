from django.contrib.auth.decorators import login_required #importamos el decorador
from django.shortcuts import render, get_object_or_404 #importamos get_object_or_404
from django.contrib import messages #importamos esto
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q

from .forms import ProductModelForm
from .models import ProductModel

# Create your views here.
def product_model_delete_view(request, product_id):
    instance = get_object_or_404(ProductModel, id = product_id)
    if request.method == "POST":
        instance.delete()
        HttpResponseRedirect("/ecommerce/")
        messages.success(request, "Producto eliminado")
        return HttpResponseRedirect ("/ecommerce/")
    context = {
        "product": instance
    }
    template = "ecommerce/delete-view.html"
    return render(request, template, context)

def product_model_update_view(request, product_id=None):
    instance = get_object_or_404(ProductModel, id = product_id)
    form = ProductModelForm(request.POST or None, instance= instance)
    if form.is_valid():
        instance = form.save(commit = False)
        instance.save()
        messages.success(request, "Producto actualizado con éxito")
        return HttpResponseRedirect ("/ecommerce/{product_id}".format(product_id = instance.id))
    context = {
        "form": form
    }
    template = "ecommerce/update-view.html"
    return render(request, template, context)

def product_model_create_view(request):
    form = ProductModelForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit = False)
        instance.save()
        messages.success(request, "Producto creado con éxito")
        return HttpResponseRedirect ("/ecommerce/{product_id}".format(product_id = instance.id))
    context = {
        "form": form
    }
    template = "ecommerce/create-view.html"
    return render(request, template, context)


def product_model_details_view(request, product_id):
    instance = get_object_or_404(ProductModel, id = product_id)
    context = {
        "product": instance
    }
    template = "ecommerce/detail-view.html"
    return render(request, template, context)



#@login_required # <-----protección y redireccionamiento
def product_model_list_view(request):
    query = request.GET.get("q", None)
    queryset = ProductModel.objects.all() # un queryset es algo que agrupa la respuesta de un modelo
    if query is not None:
        queryset = queryset.filter(
            Q(title__icontains=query) | 
            Q(price__icontains=query)
        )
    template = "ecommerce/list-view.html"
    contex = {
        "products": queryset 
    }
    if request.user.is_authenticated: # <------añadimos esta validación
        template = "ecommerce/list-view.html"
    else:
        template = "ecommerce/list-views-public.html"   
    return render(request, template, contex)


#Ejemplo para fines demostrativos, no añadida a las urls

#@login_required # <-----protección y redireccionamiento
def login_required_list(request):
    print(request.user) ## <-------mostrar el usuario en consola
    queryset = ProductModel.objects.all() # un queryset es algo que agrupa la respuesta de un modelo
    template = "ecommerce/list-view.html"
    contex = {
        "products": queryset 
    }

    if request.user.is_authenticated: # <------añadimos esta validación
        template = "ecommerce/list-view.html"
    else:
        template = "ecommerce/list-views-public.html"   

        
    return render(request, template, contex)
   