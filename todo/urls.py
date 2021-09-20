from django.urls import path
from .views import *

urlpatterns = [
    path('',todo_home),
    path('create/',todo_create, name='create'),
    path('delete/<item_id>',delete_todo, name='delete'),
    path('delete_all/',delete_all,name='delete_all'),
    path('update/<item_id>',update_todo,name='update'),
    path('update_all', update_all_items, name='update_all')
]