from django.urls import path
from member import views


urlpatterns = [
    path('', views.index, name='member.index'),
    path('delete/<int:id>', views.delete, name='member.delete'),
    path('update/<int:id>', views.update, name='member.update'),
    path('create/',views.create, name='member.create')
]
