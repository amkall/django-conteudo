from django.shortcuts import render
from main.models import Item

# Create your views here.
def homepage(request):
    return  render(request, template_name = 'main/home.html')
    

def itenspage(request):
    itens = Item.objects.all()
    return  render(request, template_name = 'main/itens.html', context = {'itens': itens})