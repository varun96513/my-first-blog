from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('html1.html/', views.html1, name='html1'),
]