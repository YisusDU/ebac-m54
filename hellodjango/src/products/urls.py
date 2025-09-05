from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView, RedirectView

from products.views import (
    ProductListView, 
    ProductDetailView, 
    DigitalProductListView, 
    ProductIDRedirectView, 
    ProductRedirectView,
    ProtectedProductDetailView,
    ProtectedProductCreateView, 
    ProtectedProductUpdateView, # New import
    ProtectedProductDeleteView # New import
    )

urlpatterns = [
    path('admin/', admin.site.urls),
    path("about-us/", RedirectView.as_view(url = "/products/about/")), 
    path("about/", TemplateView.as_view(template_name = "about.html")),  
    path("team/", TemplateView.as_view(template_name = "team.html")),  
    path("products/", ProductListView.as_view()),  
    path("digital-products/", DigitalProductListView.as_view()),  
    path("products/<int:pk>/", ProductDetailView.as_view()),
    path("products/<slug:slug>/", ProductDetailView.as_view()), 
    path("p/<int:pk>/", ProductIDRedirectView.as_view()), 
    path("p/<slug:slug>/", ProductRedirectView.as_view()), 

    path("my-products/create/", ProtectedProductCreateView.as_view()), # elemos la vista de creación 
    path("my-products/<slug:slug>/", ProtectedProductDetailView.as_view()),
    path("my-products/<slug:slug>/edit/", ProtectedProductUpdateView.as_view()),  # < -- New URL pattern
    path("my-products/<slug:slug>/delete/", ProtectedProductDeleteView.as_view()),  # < -- New URL pattern
    
]