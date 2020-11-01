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
    url('profile/',views.profile, name='profile')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

