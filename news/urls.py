from django.urls import path
from news import views


urlpatterns = [
    path('', views.index, name='category.index'),
    path('article/', views.index_article, name='article.index'),
    path('article/create/', views.create_article, name='article.create'),
    path('article/delete/<int:id>', views.article_delete, name='article.delete'),
    path('article/update/<int:id>', views.update_article, name='article.update'),
    
    
    path('category/delete/<int:category_id>', views.delete, name='category.delete'),
    path('category/update/<int:category_id>', views.update, name='category.update'),
    path('category/create/',views.create, name='category.create')
]
