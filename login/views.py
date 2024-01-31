from django.shortcuts import render,redirect
from login.form import LoginForm, RegistrationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.


def  index(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['username'],
                                password=form.cleaned_data['password']
                                )
            if user:
                login(request,user)
                return redirect('product.index')
        else:
            messages.error(request, 'Invalid username or Password. Try Agaian!')
            return redirect('login.index')
    else:
        form = LoginForm()
        return render(request, 'login_index.html',{'form':form})
                
def logout_user(request):
     logout(request)
     return redirect('home.index')

def register_user (request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login.index') 
    else:
        form = RegistrationForm()
    return render(request, 'login_create.html', {'form': form})