from django.shortcuts import render, redirect
from django.http import HttpResponse
from news.models import Category
from news.forms import CategoryForm
from .models import Article
from .forms import ArticleForm



def index(request):
    data = Category.objects.all()

    return render(request, 'category_index.html',{'title':'List Daftar Kategori','category':data})


def delete(request, category_id):
    Category.objects.filter(category_idid=category_id).delete()
    return redirect('category.index')


def create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            nama_category = form.cleaned_data['nama_category']
           
            Category.objects.create(nama_category=nama_category)
            return redirect('category.index')
        else:
            return render(request, 'category_create.html',{'form':form})
    
    else:
        form = CategoryForm()
        return render(request,'category_create.html',{'form':form})
    
def update(request, category_id):
    edit= Category.objects.get(category_id=category_id)
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            edit.nama_category = form.cleaned_data['nama_category']
            edit.save()
            return redirect('category.index')
        else:
            return render(request, 'category_update.html',{'form':form})
    
    else:
        form = CategoryForm(initial={'nama_category':edit.nama_category })
        return render(request,'category_update.html',{'form':form}) 
    

def index_article(request):
    data = Article.objects.all()

    return render(request, './articles/article_list.html',{'title':'List Daftar Artikel','article':data})
    
def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('article.index') 
    else:
        form = ArticleForm()
    return render(request, 'articles/article_create.html', {'form': form})

def update_article(request, id):
    edit= Article.objects.get(id=id)
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            edit.category = form.cleaned_data['category']
            edit.title = form.cleaned_data['title']
            edit.deskripsi = form.cleaned_data['deskripsi']
            edit.tanggal = form.cleaned_data['tanggal']
            edit.image = form.cleaned_data['image']
            
            
            edit.save()
            return redirect('article.index')
        else:
            return render(request, 'articles/article_update.html',{'form':form})
    
    else:
        form = ArticleForm(initial={'category':edit.category,'title':edit.title,'deskripsi':edit.deskripsi,'tanggal':edit.tanggal,'image':edit.image })
        return render(request,'articles/article_update.html',{'form':form}) 

def article_delete(request, id):
    Article.objects.filter(id=id).delete()
    return redirect('article.index')