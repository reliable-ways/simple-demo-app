from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
  path('', views.post_list, name='post_list'),
  path('<slug:slug>/', views.post_detail, name='post_detail'),
  # path('post/<int:pk>/', views.post_detail, name='post_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)