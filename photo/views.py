import json

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .forms import PostSearchForm

from django.views.generic.list import ListView
from django.views.generic import CreateView, UpdateView, DeleteView, FormView, DetailView, TemplateView

from .models import Photo, Comment


class PhotoCreate(LoginRequiredMixin, CreateView):
    login_url = '/member/login/'
    model = Photo
    fields = ['text', 'img', 'tags']
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
    fields = ['text', 'img', 'tags']
    template_name_suffix = '_update'
    success_url = '/photo'


class PhotoDelete(DeleteView):
    model = Photo
    template_name_suffix = '_delete'
    success_url = '/photo'


class PhotoSearchView(LoginRequiredMixin, FormView):
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
    user = request.user._wrapped  # <SimpleLazyObject로 받아와져서 ._wrapped 추가해서 없애도 같은 증상
    # TypeError: Object of type User is not JSON serializable
    text = request.POST.get('text')
    if text:
        comment = Comment.objects.create(photo=photo, user=user, text=text)
        comment.save()
        photo.save()
        data = {
            'user': str(user),
            'photo': str(photo),
            'text': str(text),
            'created': '방금 전',
            'comment_id': comment.id
        }
        print(data)
        return HttpResponse(json.dumps(data, cls=DjangoJSONEncoder), content_type="application/json")


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


@login_required
def Like(request, pk):
    photo = get_object_or_404(Photo, id=pk)
    user = request.user

    if photo.like.filter(id=user.id).exists():
        photo.like.remove(user)
        message = "좋아요 취소"
    else:
        photo.like.add(user)
        message = "좋아요"
    context = {'like_count': photo.like.count(), "message": message}
    return HttpResponse(json.dumps(context), content_type='application/json')


class TagPhotoView(ListView):
    template_name = 'taggit/taggit_post_list.html'
    model = Photo

    def get_queryset(self):
        return Photo.objects.filter(tags__name=self.kwargs.get('tag'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tagname'] = self.kwargs['tag']
        return context



class TagcloudTV(TemplateView):
    template_name = 'taggit/taggit_cloud.html'