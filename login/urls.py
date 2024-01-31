from django.urls import path
from login import views

urlpatterns = [
    path ('login/',views.index, name='login.index'),
    path ('logout/',views.logout_user, name='logout'),
    path ('registrasi/',views.register_user, name='register'),
]
