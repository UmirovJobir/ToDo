from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import DetailView

from .models import Task, Image, Title
from .forms import TaskForm, TitleForm


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('list')
    else:
        form = AuthenticationForm()

    context = {'form': form}
    return render(request, 'login.html', context)


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
    return render(request, 'login.html')


@login_required(login_url='login/')
def index(request):
    tasks = Task.objects.all()

    context = {'tasks': tasks}
    return render(request, 'list.html', context)


def title(request):
    titles = Title.objects.all()

    form = TitleForm()

    if request.method == 'POST':
        form = TitleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
    context = {'titles': titles, 'form': form}
    return render(request, 'list.html', context)


def createTask(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            animal = form.save(commit=False)
            animal.user = request.user
            animal.save()
            return redirect('list')
        else:
            return redirect('list')
    else:
        context = {'form': form}
        return render(request, 'create.html', context)


def updateTask(request, pk):
    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}

    return render(request, 'update_task.html', context)


def deleteTask(request, pk):
    item = Task.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('/')

    context = {'item': item}
    return render(request, 'delete.html', context)


def photo(request, pk):
    imge = Image.objects.get(pk=pk)

    context = {'imge': imge}
    return render(request, 'list.html', context)
