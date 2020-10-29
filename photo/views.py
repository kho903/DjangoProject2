import json

from django.contrib.auth.decorators import login_required
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .forms import PostSearchForm

# Create your views here.
from django.views.generic.list import ListView
from django.views.generic import CreateView, UpdateView, DeleteView, FormView, DetailView

from .models import Photo, Comment


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
    paginate_by = 10


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


class PhotoDetail(DetailView):
    model = Photo
    template_name_suffix = '_detail'


@login_required
def create_comment(request, pk):
    photo = get_object_or_404(Photo, id=pk)
    user = request.user
    text = request.POST.get('text')
    if text:
        comment = Comment.objects.create(photo=photo, user=user, text=text)
        comment.save()
        photo.save()
        data = {
            'user': user,
            'photo': photo,
            'text': text,
            'created': '방금 전',
            'comment_id': comment.id
        }
        return HttpResponse(json.dumps(data, cls=DjangoJSONEncoder), content_type="application/json")

    # if request.method == 'POST':
    #     comment = Comment()
    #     comment.text = request.POST['text']
    #     comment.photo = Photo.objects.get(pk=request.POST['Photo'])
    #     comment.user = request.user.username
    #     comment.save()
    #     return redirect('/photo/' + str(comment.photo.id))
    # else:
    #     return redirect('home')


@login_required
def delete_comment(request, pk):
    photo = get_object_or_404(Photo, id=pk)
    comment_id = request.POST.get('comment_id')
    target_comment = Comment.objects.get(pk=comment_id)

    if request.user == target_comment.user:
        target_comment.deleted = True
        target_comment.save()
        photo.save()
        data = {
            'comment_id': comment_id
        }
        return HttpResponse(json.dumps(data, cls=DjangoJSONEncoder), content_type="application/json")
