from django.shortcuts import render, redirect
from django.db.models import Q

# Create your views here.
from django.views.generic.list import ListView
from django.views.generic import CreateView, UpdateView, DeleteView, FormView

from .models import Photo


class PhotoCreate(CreateView):
    model = Photo
    fields = ['text', 'img']
    template_name_suffix = '_create'
    success_url = '/photo'

    def form_valid(self, form):
        form.instance.save()
        return redirect('/photo')


class PhotoList(ListView):
    model = Photo
    template_name_suffix = '_list'


class PhotoUpdate(UpdateView):
    model = Photo
    fields = ['text', 'img']
    template_name_suffix = '_update'
    success_url = '/photo'


class PhotoDelete(DeleteView):
    model = Photo
    template_name_suffix = '_delete'
    success_url = '/photo'




