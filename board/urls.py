from django.urls import path
from .views import *


app_name = 'board'

urlpatterns = [
    path('', post_list),
    path('post/create/', post_create),
    path('post/detail/<int:pk>/', post_detail),
    path('post/update/<int:pk>/', post_update),
    path('post/delete/<int:pk>/', post_delete),
]