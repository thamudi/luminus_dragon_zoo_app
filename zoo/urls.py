from django.urls import path
from .views import *
urlpatterns = [
    path('', dragon_list_view, name='index'),
    path('create/', dragon_create_view, name='create'),
    path('edit/<dragon_id>', dragon_edit_view, name='edit'),
    path('delete/<dragon_id>', dragon_delete_view, name='delete'),
]
