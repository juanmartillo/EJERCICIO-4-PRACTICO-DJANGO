from django.forms import ModelForm
from .models import Producto

class productForm(ModelForm):
    class Meta:
        model = Producto
        fields = ['title', 'description']
