from django.urls import path
from .views import PhotoCreate, PhotoList, PhotoUpdate, PhotoDelete, PhotoSearchView, create_comment, delete_comment, \
    PhotoDetail, Like, TagPhotoView, TagcloudTV

from django.conf.urls.static import static
from django.conf import settings

app_name = 'photo'

urlpatterns = [
    path("", PhotoList.as_view(), name='index'),
    path("create/", PhotoCreate.as_view(), name='create'),
    path("<int:pk>/", PhotoDetail.as_view(), name='detail'),
    path('<int:pk>/comment/create/', create_comment, name='create_comment'),
    path('<int:pk>/comment/delete/', delete_comment, name='delete_comment'),
    path("update/<int:pk>/", PhotoUpdate.as_view(), name='update'),
    path("delete/<int:pk>/", PhotoDelete.as_view(), name='delete'),
    path("search/", PhotoSearchView.as_view(), name='search'),
    path("<int:pk>/like", Like, name='like'),
    path('tag/', TagcloudTV.as_view(), name='tag_cloud'),
    path('tag/<str:tag>', TagPhotoView.as_view(), name='tagged_object_list'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
