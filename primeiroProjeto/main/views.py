from django.shortcuts import render, redirect
from main.models import Item
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def homepage(request):
    return  render(request, template_name = 'main/home.html')
    

def itenspage(request):
    itens = Item.objects.all()
    return  render(request, template_name = 'main/itens.html', context = {'itens': itens})

def loginpage(request):
    if request.method == 'GET':
        return  render(request, template_name = 'main/login.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        username = request.POST.get('password')

        user = authenticate(username = username, passaword = passaword);
        if user is not None:
            login(request, user)
            return redirect('itens')
        else:
            return redirect('login')
def registerpage(request):
    if request.method == 'GET':
        return render(request, template_name='main/register.html')
    
    if request.method == 'POST':
        form = UserCreationForm(request.Post)

        if form.is_valid():
            form.save()
            username   = form.cleaned_data.get('username')
            passaword  = form.cleaned_data.get('passaword')
            passaword1 = form.cleaned_data.get('passaword1')

            user = authenticate(username = username, passaword = passaword);
            return redirect('home')
        else:
            return redirect('register')
    return redirect('register')

