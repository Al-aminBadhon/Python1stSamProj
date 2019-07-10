from django.views.generic import ListView
from . models import Category
from . models import Product
from . models import Cart


class HomeView(ListView):
    template_name = 'home.html'
    model = Product

