from django.urls import path
from product import views


urlpatterns = [
    path('', views.index, name='product.index'),
    path('<int:id>/', views.detail),
    path("calc/<int:bil>/<int:bil2>", views.calc),
    path('delete/<int:id>', views.delete, name='product.delete'),
    path('update/<int:id>', views.update, name='product.update'),
    path('create/',views.create, name='product.create')
]
