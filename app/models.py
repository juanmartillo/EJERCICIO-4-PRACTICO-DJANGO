from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Producto(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
class cliente(models.Model):
    name =  models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name.username
    
    
