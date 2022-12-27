from django.shortcuts import render, redirect
from .models import Computers
from .forms import ComputersForm

#Главное
def post_main(request):
    return render(request, 'post_main.html')

def post_we(request):
    return render(request, 'post_we.html')

def post_contact(request):
    return render(request, 'post_contact.html')
#Список
def post_list(request):
    computers = Computers.objects.all()
    context = {
        'computers' : computers
    }
    return render(request, 'post_list.html', context)

#информация
def post_retrieve(request, pk):
    computer = Computers.objects.get(id=pk)
    context = {
        'computer' : computer
    }
    return render(request, 'post_retrieve.html', context)

#создать
def post_create(request):
    form = ComputersForm
    if request.method == 'POST':
        form = ComputersForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/main/buy/')
    context = {
       'form' : form 
    }
    return render(request, 'post_create.html', context)

#Удалить
def post_delete(request, pk):
    computer = Computers.objects.get(id=pk)
    computer.delete()
    return redirect('/main/buy/')

#редактировать 
def post_update(request, pk):
    computer = Computers.objects.get(id=pk)
    form = ComputersForm(instance=computer)
    if request.method == 'POST':
        form = ComputersForm(request.POST, instance=computer, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/main/buy/')
    context = {
       'form' : form 
    }
    return render(request, 'post_update.html', context)
