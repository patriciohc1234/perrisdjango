from django.urls import path
from . import views

urlpatterns = [
    #path('', views.base, name='base'),
	path('', views.post_list, name='post_list'),
]