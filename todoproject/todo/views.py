from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import TodoModels

class TodoList(ListView):
    template_name = 'list.html'
    model = TodoModels

class TodoDetail(DetailView):
    template_name = 'detail.html'
    model = TodoModels

class TodoCreate(CreateView):
    template_name = 'create.html'
    model = TodoModels
    fields = '__all__'
    success_url = reverse_lazy('list')

class TodoDelete(DeleteView):
    template_name = 'delete.html'
    model = TodoModels
    success_url = reverse_lazy('list')

class TodoUpdate(UpdateView):
    template_name = 'update.html'
    model = TodoModels
    fields = '__all__'
    success_url = reverse_lazy('list')
