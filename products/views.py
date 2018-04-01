from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, View

from .models import Product
from django.http import Http404

# import all the views to urls to make action
# both function-based and class-based views are independent their urls are different


class ProductListView(ListView):
    
    queryset = Product.objects.all()
    template_name = "products/list.html"
    
    def get_context_data(self, *args, **kwargs):
        context = super(ProductListView, self).get_context_data(*args, **kwargs)
        print(context)
        return context

def product_list_view(request):
    queryset = Product.objects.all()

    context = {
        "object_list": queryset
    }
    return render(request, "products/list.html", context)

class ProductDetailView(DetailView):

    queryset = Product.objects.all()
    template_name = "products/cb-detail.html"

    def get_object(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs.get('pk')
        instance = get_object_or_404(Product, pk)
        if instance is None:
            raise Htpp404("Product doesn't exists.")
        return instance

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        print(context)
        return context


# f-based views
def product_detail_view(request, pk=None, *args, **kwargs):
    # print(args)
    # print(kwargs) for showing particular product
    # get the pk value , pk is django default object (primary key or id)
    '''
    try:
        instance = Product.objects.get(pk=pk)
    except:
        print("no product here")
        raise Http404("product does not exists")
    '''
    qs = Product.objects.filter(id= pk)
    
    if qs.exists() and qs.count() == 1:
        instance = qs.first()
    else:
        raise Http404("Product does not exists.")

    context = {
        "object": instance,
        "pkk": pk
    }
    return render(request, "products/fb-detail.html", context)