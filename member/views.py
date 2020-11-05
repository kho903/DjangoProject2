import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))


from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash, get_user_model
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.views.generic import ListView
from rest_framework.generics import get_object_or_404

from .forms import UserCreationForm, ProfileForm
from .models import User
# from ..photo.models import Photo
# import sys
# sys.path.append("..")



def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, '패스워드가 성공적으로 업데이트 되었습니다.')
            return redirect('index') # 다음 url로 이동한다.
        else:
            messages.error(request,"다음 에러를 확인해주세요.")
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/change_password.html',{'form':form})

# 계정 삭제 기능
@login_required
def delete(request):
    if request.method == "POST":
        request.User.delete()
        return redirect('index')
    return redirect('index')


# New User Registration(회원가입 기능)
def create_user(request):
    if request.method == 'POST':
        try:
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password1']
            new_user = User.objects.create_user(username, email, password)
            new_user.save()
            return render(request, 'registration/signup_done.html', {'message': '회원가입이 완료되었습니다.'})
        except:
            return render(request, 'registration/signup_done.html', {'message': '회원이 이미 있음'})
    else:
        form = UserCreationForm()
        return render(request, 'registration/signup.html', {'form': form})


# 로그아웃 기능
def sign_out(request):
    logout(request)
    return render(request, 'home/base.html')

# 로그인 기능
def sign_in(request):
    # 로그인 폼을 제출했을 때
    if request.method == 'POST':
        # 유저 (username, password)로 인증
        user = authenticate(request, username=request.POST.get('username', ''),
                            password=request.POST.get('password', ''))
        # 인증이 완료되면,
        if user is not None:
            login(request, user) # 로그인 (django.contrib.auth 제공)
            # 로그인 이후 페이지로 이동
            return render(request, 'registration/signup_done.html', {'message': "로그인 되었습니다."})
        else:
            return render(request, 'registration/signup_done.html', {'message': "로그인에 실패하였습니다."})
    else:
        # 로그인 폼 생성
        form = AuthenticationForm()
        return render(request, 'registration/login.html', {'form': form})
# profile update
def profile_update(request):
    user = request.user
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES, instance=user)
        if profile_form.is_valid(): # 단, form이 valid하지 않으면 저장되지 않는다. (예) 생일의 형식이 안맞을 때
            profile_form.save()
        return redirect('people', request.user.username)
    else:
        profile_form = ProfileForm(instance=user)
    return render(request, 'profile/profile_update.html', {'profile_form': profile_form})

#
class UserList(ListView):
    # person = get_object_or_404(User, username=username)
    model = User
    template_name_suffix="_list"

#
# def followlist(request,username):
#     object = Connection.objects.filter(following_username=username)
#     return render(request, "user/user_list.html",{'object': object})


# 게시물의 작성자의 username을 통해 user 페이지에 접근하기
def peoplePage(request,username):
    person = get_object_or_404(User, username=username)
    # 작성자가 username인 photo를 전달하기
    photo_list = Photo.objects.filter(username=username).distinct()
    context={}
    context['people']=person
    context['object_list']=photo_list

    return render(request, "profile/people.html",context)


def follow(request, username):
    people = get_object_or_404(get_user_model(), username=username)
    if request.user in people.followers.all():
        # people을 unfollow하기
        people.followers.remove(request.user)
    else:
        # people을 follow하기
        people.followers.add(request.user)
    return render(request, "profile/people.html",{'people': people})

