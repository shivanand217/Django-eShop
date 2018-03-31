from django.shortcuts import render
from django.views.generic import ListView, DetailView, View

from .models import Product

# import all the views to urls to make action
# class based views

class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = "products/list.html"

    '''
    def get_context_data(self, *args, **kwargs):
        context = super(ProductListView, self).get_context_data(*args, **kwargs)
        print(context)
        return context
    '''

# function based views
def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, "products/list.html", context)


class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = "products/detail.html"

    '''
    def get_context_data(self, *args, **kwargs):
        context = super(ProductListView, self).get_context_data(*args, **kwargs)
        print(context)
        return context
    '''

# function based views
def product_detail_view(request):
    queryset = Product.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, "products/detail.html", context)


