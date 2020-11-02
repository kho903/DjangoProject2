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

    # if request.method == 'POST':
    #     comment = Comment()
    #     comment.text = request.POST['text']
    #     comment.photo = Photo.objects.get(pk=request.POST['Photo'])
    #     comment.user = request.user
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


# @login_required
# def Like(request, pk):
#     photo = get_object_or_404(Photo, id=pk)
#
#     Like, like_created = photo.like.get_or_create(user=request.user)
#
#     if not like_created:
#         Like.delete()
#         message = "좋아요 취소"
#     else:
#         message = "좋아요!"
#
#     data = {
#         'like_count': photo.like_count,
#         'message': message,
#         'user': request.user
#     }
#     print(data)
#     return HttpResponse(json.dumps(data), content_type='application/json')
#

def Like(request):
    if request.is_ajax():  # ajax 방식일 때 아래 코드 실행
        photo_id = request.GET['photo_id']  # 좋아요를 누른 게시물id (blog_id)가지고 오기
        photo = Photo.objects.get(id=photo_id)

        if not request.user.is_authenticated:
            message = "로그인이 필요합니다!"
            context = {'like_count': photo.like.count(), "message": message}
            return HttpResponse(json.dumps(context), content_type='application/json')

        user = request.user
        if photo.like.filter(id=user.id).exists():
            photo.like.remove(user)
            message = "좋아요 취소"
        else:
            photo.like.add(user)
            message = "좋아요"
        context = {'like_count': photo.like.count(), "message": message}
        return HttpResponse(json.dumps(context), content_type='application/json')
