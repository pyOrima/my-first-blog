from django.urls import path
from . import views
import sys
sys.path.append('/home/pyOrima/pyorima.pythonanywhere.com/blog')
from blog import views

urlpatterns = [
    path('', views.base, name='base'),
    path('api/', views.api, name="api"),
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]