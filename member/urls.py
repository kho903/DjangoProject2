from django.conf.urls import url
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

# app_name = "member"

urlpatterns = [
    url('join/', views.create_user, name="join"),
    url('login/', views.sign_in, name="login"),
    url('logout/', views.sign_out, name='logout'),
    url('delete/',views.delete, name='delete'),
    url('change_password/',views.change_password,name='change_password'),
    url('profile_update/',views.profile_update, name='profile_update'),
    url('user_list/',views.UserList, name='UserList'), # <str:username>/
    # path('<str:username>/followers/', views.followlist, name='followers'),
    # url('people/(?P<username>\d+)/',views.people, name="people"),  # <str:username> !!URL 문제

    path('people/<str:username>/', views.peoplePage , name="people"),
    path('follow/<str:username>/',views.follow, name='follow'),
    # path('people/<int:pk>/', views.peoplePage2 , name="people"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

