from django.urls import path
from home import views


urlpatterns = [
    path('', views.index, name='home.index'),
    path('berita/<str:slug>', views.detail, name='home.news_detail'),
    path('berita/komentar/<str:slug>/<int:parent_id>/', views.tambah_komentar, name='tambah_komentar.chained'),
    path('berita/komentar/<str:slug>', views.tambah_komentar, name='tambah_komentar'),
    path('berita/<str:category>', views.category, name='home.category'),
    path('ajax/', views.load_ajax, name='home.ajax'),
    path('ajax/data/', views.ajax_data, name='home.ajax_data'),
    path('berita/likey/<int:id>', views.likey_ajax, name='home.likey'),
    
 
]
