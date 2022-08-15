
from django.contrib import admin
from django.urls import path
from . import views

app_name = 'shopping_list'
urlpatterns = [
    path('', views.index, name='index'),
    path('create_new_item', views.create_new_item, name='create_new_item'),
    path('create_new_list', views.create_new_list, name='create_new_list'),
    # path('create_new_bill', views.create_new_bill, name='create_new_bill'),
    # path('delete_bill/<str:bill_id>', views.delete_bill, name='delete_bill'),
    # path('delete_bill_from_paycheck/<str:paycheck_id>/<str:bill_id>', views.delete_bill_from_paycheck, name='delete_bill_from_paycheck'),
    path('delete_list/<str:list_id>', views.delete_list, name='delete_list'),
    path('add_item_to_list/<str:list_id>', views.add_item_to_list, name='add_item_to_list'),
    path('delete_item/<str:list_id>/<str:item_id>', views.delete_item, name='delete_item'),
    path('edit_item/<str:item_id>', views.edit_item, name='edit_item'),
    path('edit_list/<str:list_id>', views.edit_list, name='edit_list'),
    # path('update_money_in_bank/<str:paycheck_id>', views.update_money_in_bank, name='update_money_in_bank'),
    # path('pay_bill/<str:paycheck_id>/<str:bill_id>/<str:paid>', views.pay_bill, name='pay_bill'),
    # path('update_bill/<str:bill_id>', views.update_bill, name='update_bill'),
    # path('edit_paycheck/<str:paycheck_id>', views.edit_paycheck, name='edit_paycheck'),


]
