from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path(r'', views.base, name='base'),
    path("ajax/", views.api, name="api"),
    path("ajax2/", views.api2, name="api2"),
    #path('', views.post_list, name='post_list'),
    #path('post/<int:pk>/', views.post_detail, name='post_detail'),
    #path('post/new/', views.post_new, name='post_new'),
    #path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]