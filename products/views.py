from django.shortcuts import render
from django.views.generic import ListView, DetailView, View

from .models import Product

# import all the views to urls to make action

# class based views

class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = "products/list.html"


# function based views
def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, "products/list.html", context)
