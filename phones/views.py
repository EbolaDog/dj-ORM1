from django.shortcuts import render,redirect, get_object_or_404
from phones.models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sorting = request.GET.get('sort')
    if sorting == 'name':
        context = {'phones':Phone.objects.order_by('name')}
    elif sorting == 'min_price':
        context = {'phones':Phone.objects.order_by('price')}
    elif sorting == 'max_price':
        context = {'phones':Phone.objects.order_by('price').reverse()}
    else:
        context = {'phones':Phone.objects.all()}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    product = get_object_or_404(Phone, slug = slug)
    context = {'phone': product}
    return render(request, template, context)