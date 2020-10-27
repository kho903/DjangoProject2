from django.urls import path
from .views import PhotoCreate, PhotoList, PhotoUpdate, PhotoDelete, PhotoSearchView

from django.conf.urls.static import static
from django.conf import settings

app_name = 'photo'

urlpatterns = [
    path("", PhotoList.as_view(), name='index'),
    path("create/", PhotoCreate.as_view(), name='create'),
    path("update/<int:pk>/", PhotoUpdate.as_view(), name='update'),
    path("delete/<int:pk>/", PhotoDelete.as_view(), name='delete'),
    path("search/", PhotoSearchView.as_view(), name='search'),
]

urlpatterns += \
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
