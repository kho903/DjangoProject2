from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index),
    # path('sign-up/',SignUp.as_view()),
    url('join/', views.create_user, name="join"),
    url('login/', views.sign_in, name="login"),
    url('logout/', views.sign_out, name='logout'),
    url('update/', views.update, name='update')
]
