from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Auth, User
from .forms import UserForm

# 로그인
def login(request):
    ID_user = User.ID_user.all() 

    context = {}
    return render(request, 'blog/index.html', context)


def create(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            
    else:
        form = UserForm()
    context = {'form': form,}
    return render(request, 'accounts/login.html', context)
