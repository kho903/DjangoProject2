# from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from .forms import UserCreationForm, UserUpdateForm
from .models import User

# Create your views here.
# 마이 페이지에서 자기 정보를 수정하기
# @login_required
def update(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST.copy(), instance=User) #, instance=user
        if form.is_valid():
            form.save()
        return render(request, 'home/base.html', {'message': "계정 정보가 수정되었습니다."})
    else:
        form = UserUpdateForm()
        return render(request, 'registration/update.html', {'form': form})


def change_password(request):
    if request.method =="POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, '패스워드가 성공적으로 업데이트 되었습니다.')
            return redirect('index') #다음 url로 이동한다.
        else:
            messages.error(request,"다음 에러를 확인해주세요.")
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/change_password.html',{'form':form})

# @login_required
def delete(request):
    if request.method == "POST":
        request.User.delete()
        return redirect('index')
    return redirect('index')


# New User Registration
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



def sign_out(request):
    logout(request)
    return render(request, 'home/base.html')


def sign_in(request):
    if request.method == 'POST':
        user = authenticate(request, username=request.POST.get('username', ''),
                            password=request.POST.get('password', ''))
        if user is not None:
            login(request, user)
            return render(request, 'registration/signup_done.html', {'message': "로그인 되었습니다."})
        else:
            return render(request, 'registration/signup_done.html', {'message': "로그인에 실패하였습니다."})
    else:
        form = AuthenticationForm()
        return render(request, 'registration/login.html', {'form': form})

# 정보 수정하는 기능
def profile(request):
    if request.method == 'GET':
        return render(request, 'registration/mypage.html')

    elif request.method == 'POST':
        user = request.user

        text = request.POST.get('text')
        email = request.POST.get('email')
        # birth_date = request.POST.get('birth_date')
        img = request.POST.get('img')

        user.text = text
        user.email = email
        # user.birth_date = birth_date
        user.img = img

        user.save()

        return redirect('member/profile', user.username)