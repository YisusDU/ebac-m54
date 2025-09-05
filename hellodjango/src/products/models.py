from django.conf import settings 
from django.db import models

User = settings.AUTH_USER_MODEL 

# Create your models here.
class Product(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL) 
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)

    def get_absolute_url(self): 
        return f"/products/products/{self.slug}"
    
    def get_edit_url(self): # Redirige a la vista de edición
        return f"/products/my-products/{self.slug}/edit"
    
    def get_delete_url(self): # Redirige a la vista de eliminación
        return f"/products/my-products/{self.slug}/delete"
    
# Usar modelos proxy para cambiar el comportamiento sin cambiar la estructura de la base de datos
class DigitalProduct(Product):
    class Meta:
        proxy = True