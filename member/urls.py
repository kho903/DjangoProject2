from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url('join/', views.create_user, name="join"),
    url('login/', views.sign_in, name="login"),
    url('logout/', views.sign_out, name='logout'),
    url('delete/',views.delete, name='delete'),
    url('change_password/',views.change_password,name='change_password'),
    url('profile/',views.profile, name='profile'),
    url('follow/',views.follow, name='follow'),
    url('user_list/',views.UserList, name='Userlist'),
    url('people/',views.people,name="people")
    # url('follow/<int:pk>/',views.Following, name='follow'),
    # url('unfollow/<int:pk>/',views.Unfollow, name='unfollow'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

