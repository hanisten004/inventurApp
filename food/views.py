from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
# Create your views here.
from .models import Location,Kasten,KastenProduct
from django.template import loader
from .forms import LocationForm
from .forms import KastenProductForm 
from .forms import ProductForm

from django.shortcuts import render, redirect, get_object_or_404
from .models import Location, Kasten, KastenProduct
from .forms import LocationForm, KastenProductForm, ProductForm

def index(request):
    location_list = Location.objects.all()
    context = {
        'location_list': location_list,
    }
    return render(request, 'food/index.html', context)

def detail(request, location_id):
    location = Location.objects.get(pk=location_id)
    context = {
        'location': location,
    }
    return render(request, 'food/detail.html', context)

def create_location(request):
    form = LocationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request, 'food/location-form.html', {'form': form})

def update_location(request, id):
    location = Location.objects.get(id=id)
    form = LocationForm(request.POST or None, instance=location)
    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request, 'food/location-form.html', {'form': form, 'location': location})

def delete_location(request, id):
    location = Location.objects.get(id=id)
    if request.method == 'POST':
        location.delete()
        return redirect('food:index')
    return render(request, 'food/location-delete.html', {'location': location})

def kasten_detail(request, kasten_id):
    kasten = get_object_or_404(Kasten, id=kasten_id)
    kasten_products = KastenProduct.objects.filter(kasten=kasten)
    context = {
        'kasten': kasten,
        'kasten_products': kasten_products,
    }
    return render(request, 'food/kasten_detail.html', context)

def update_all_quantities(request, kasten_id):
    if request.method == 'POST':
        kasten = get_object_or_404(Kasten, id=kasten_id)
        quantities = request.POST.getlist('quantities')
        kp_ids = request.POST.getlist('kp_ids')
        
        for kp_id, quantity in zip(kp_ids, quantities):
            if quantity.isdigit():
                kp = KastenProduct.objects.get(pk=kp_id)
                kp.quantity = int(quantity)
                kp.save()
                
    return redirect('food:kasten_detail', kasten_id=kasten_id)

def edit_kasten_product(request, pk):
    kasten_product = get_object_or_404(KastenProduct, pk=pk)
    if request.method == "POST":
        form = KastenProductForm(request.POST, instance=kasten_product)
        if form.is_valid():
            form.save()
            return redirect('food:kasten_detail', pk=kasten_product.kasten.pk)
    else:
        form = KastenProductForm(instance=kasten_product)
    return render(request, 'food/edit_kasten_product.html', {'form': form, 'kasten_product': kasten_product})

def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('food:index')
    else:
        form = ProductForm()
    return render(request, 'food/product_create.html', {'form': form})

"""
from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from .models import Item
from django.template import loader
from .forms import ItemForm

def index(request):
    item_list = Item.objects.all()
   
    context = {
        'item_list':item_list,
    }
    return render(request, 'food/index.html',context)

def item(request):
    return HttpResponse('<h1>This is an item view</h1>')


def detail(request,item_id):
    item = Item.objects.get(pk=item_id)
    context = {
        'item':item,
    }
    return render(request, 'food/detail.html',context)

#create function
def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('food:index')

    return render(request,'food/item-form.html',{'form':form})

#update function
def update_item(request,id):
    item = Item.objects.get(id=id)
    form = ItemForm(request.POST or None,instance=item)

    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request,'food/item-form.html',{'form':form,'item':item})

#delete function
def delete_item(request, id):
    item = Item.objects.get(id=id)
    
    if request.method == 'POST':
        item.delete()
        return redirect('food:index')

    return render(request, 'food/item-delete.html', {'item': item})  # Korrigiere den Kontext auf ein Dictionary
"""