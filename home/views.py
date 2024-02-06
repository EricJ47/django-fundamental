from django.shortcuts import render, redirect, get_object_or_404,HttpResponseRedirect
from news.models import Article, Category, Komentar, ArticleLike
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse

# Create your views here.

def index(request):
    news = Article.objects.all()
    data_terbaru = Article.objects.order_by('-tanggal')[:5]
    paginator = Paginator(news, 3)
    
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
    
    cat= Category.objects.all()
    
    current_time = timezone.now()
    recent_articles = Article.objects.filter(tanggal__gte=current_time - timezone.timedelta(days=1))
    
    return render(request, 'home_index.html',{'news':news,'cat':cat, 'recent_articles': recent_articles, 'articles': articles, 'data_terbaru': data_terbaru})

def detail(request, slug,  ):
    news = Article.objects.order_by('-tanggal').all()
    
    cat = Category.objects.all()
    article = Article.objects.get(slug=slug)
    article.total_views += 1
    article.save()
    
    komentar = Komentar.objects.filter(article=article, parent__isnull=True)
    return render(request, 'home_detail.html',{'news':news, 'cat':cat, 'article' :article, 'komentar': komentar})


def category(request, category):
    news = Article.objects.order_by('-tanggal').all()

    # Mengambil satu objek kategori atau menangani kesalahan jika tidak ditemukan
    cat = get_object_or_404(Category, nama_category=category)

    # Mengambil artikel berdasarkan kategori tertentu
    news_category = Article.objects.filter(category=cat)

    return render(request, 'home_category.html', {'news': news, 'cat': cat, 'news_category': news_category, 'category': category})

def tambah_komentar (request, slug, parent_id=None):
    article = Article.objects.get(slug=slug)
    parent_komentar = None
    if parent_id:
        parent_komentar = get_object_or_404(Komentar, id=parent_id)

    if request.method == 'POST':
        isi_komentar = request.POST.get('isi_komentar')

        if parent_komentar:
            Komentar.objects.create(article=article, pengguna=request.user, isi_komentar=isi_komentar, parent=parent_komentar)
        else:
            Komentar.objects.create(article=article, pengguna=request.user, isi_komentar=isi_komentar)


    return HttpResponseRedirect(request.META.get('HTTP_REFERER', 'berita/<str:slug>'))


def load_ajax(request):
    return render(request, 'ajax.html')


def ajax_data(request):
    data = {
        'nama': 'Ronaldo',
        'alamat': 'sabu',
        'club':[
            {
                "nama_club": "AL-nasr",
                "tahun": '2019'
            },
            {
                "nama_club": "PSG",
                "tahun": '2021'
            }
        ]
    }
    return JsonResponse(data)



def likey_ajax(request, id):
   
    
    article = Article.objects.get(id=id)
    ArticleLike.objects.create(article=article)

    newsLikedCount = article.like.count()
    
    data = {
        "newsLikedCount": newsLikedCount
    }    
    return JsonResponse(data)
