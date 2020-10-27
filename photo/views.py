from django.shortcuts import render, redirect
from django.db.models import Q
from .forms import PostSearchForm

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
        form.instance.user = self.request.user
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


class PhotoSearchView(FormView):
    form_class = PostSearchForm
    template_name = 'photo/photo_search.html'

    def form_valid(self, form):
        searchWord = form.cleaned_data['search_word']
        photo_list = Photo.objects.filter(Q(text__icontains=searchWord)).distinct()

        context = {}
        context['form'] = form
        context['search_term'] = searchWord
        context['object_list'] = photo_list

        return render(self.request, self.template_name, context)
