from django.shortcuts import render, get_object_or_404
from .models import Phone


def catalog_view(request):
    sort = request.GET.get('sort', 'name')

    if sort == 'name':
        phones = Phone.objects.all().order_by('name')
    elif sort == 'min_price':
        phones = Phone.objects.all().order_by('price')
    elif sort == 'max_price':
        phones = Phone.objects.all().order_by('-price')
    else:
        phones = Phone.objects.all().order_by('name')

    context = {
        'phones': phones,
    }
    return render(request, 'catalog/catalog.html', context)


def phone_detail_view(request, slug):
    phone = get_object_or_404(Phone, slug=slug)
    context = {
        'phone': phone,
    }
    return render(request, 'catalog/phone_detail.html', context)
