from django.shortcuts import render, redirect
from django.http import HttpResponse
from product.models import Product
from product.form import ProductForm



def index(request):
    data = Product.objects.all()

    return render(request, 'product_index.html',{'title':'Product Hari Ini','product':data})
def detail(request, id):
    response = f"parameter: {id}"
    return HttpResponse(response)

def calc(request, bil, bil2):
    result = f"Hasil tambah: {bil}+{bil2} = {bil+bil2}"
    return HttpResponse(result)

def delete(request, id):
    Product.objects.filter(id=id).delete()
    return redirect('product.index')

def create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            nama = form.cleaned_data['nama']
            deskripsi = form.cleaned_data['deskripsi']
            harga = form.cleaned_data['harga']
            Product.objects.create(nama=nama, deskripsi=deskripsi, harga=harga)
            return redirect('product.index')
        else:
            return render(request, 'product_create.html',{'form':form})
    
    else:
        form = ProductForm()
        return render(request,'product_create.html',{'form':form})
    
    
def update(request, id):
    edit= Product.objects.get(id=id)
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            edit.nama = form.cleaned_data['nama']
            edit.deskripsi = form.cleaned_data['deskripsi']
            edit.harga = form.cleaned_data['harga']
            edit.save()
            return redirect('product.index')
        else:
            return render(request, 'product_update.html',{'form':form})
    
    else:
        form = ProductForm(initial={'nama':edit.nama, 'deskripsi':edit.deskripsi, 'harga':edit.harga})
        return render(request,'product_update.html',{'form':form}) 


