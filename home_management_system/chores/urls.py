
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
# from users import views as user_views

app_name = 'chores'

urlpatterns = [
    path('', views.index, name='index'),
    path('add_new_chore/<str:day>/<str:user>', views.add_new_chore, name='add_new_chore'),
    path('complete_chore/<str:chore_id>/<str:user>', views.complete_chore, name='complete_chore'),


]



# from django.contrib import admin
# from django.urls import path
# from . import views
#
# app_name = 'shopping_list'
# urlpatterns = [
#     path('', views.index, name='index'),
#     path('create_new_item', views.create_new_item, name='create_new_item'),
#     path('create_new_list', views.create_new_list, name='create_new_list'),
#     path('delete_list/<str:list_id>', views.delete_list, name='delete_list'),
#     path('add_item_to_list/<str:list_id>', views.add_item_to_list, name='add_item_to_list'),
#     path('delete_item/<str:list_id>/<str:item_id>', views.delete_item, name='delete_item'),
#     path('edit_item/<str:item_id>', views.edit_item, name='edit_item'),
#     path('edit_list/<str:list_id>', views.edit_list, name='edit_list'),
#
# ]
