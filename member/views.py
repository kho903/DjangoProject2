from django.shortcuts import render
# Create your views here.
from .forms import UserCreationForm, UserUpdateForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm


# 마이 페이지에서 자기 정보를 수정하기
def update(request):
    if request.method == 'POST':
        # 수정하는 로직 필요
        postdata= request.POST.copy()
        form = UserUpdateForm(postdata)

        if form.is_valid():
            form.save()
        return render(request, 'home/base.html', {'message': "계정 정보가 수정되었습니다."})
    else:
        form = UserUpdateForm()
        return render(request, 'registration/update.html', {'form': form})

def create_user(request):
    if request.method == 'POST':
        try:
            nickname = request.POST['nickname']
            email = request.POST['email']
            password = request.POST['password1']
            new_user = User.objects.create_user(nickname, email, password)
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
            return render(request, 'registration/login.html', {'message': "로그인 되었습니다."})
        return render(request, 'registration/login.html', {'message': "로그인에 실패하였습니다."})
    else:
        form = AuthenticationForm()
        return render(request, 'registration/login.html', {'form': form})

