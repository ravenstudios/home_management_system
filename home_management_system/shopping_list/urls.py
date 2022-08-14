
from django.contrib import admin
from django.urls import path
from . import views

app_name = 'shopping_list'
urlpatterns = [
    path('', views.index, name='index'),
    # path('create_new_bill', views.create_new_bill, name='create_new_bill'),
    # path('delete_bill/<str:bill_id>', views.delete_bill, name='delete_bill'),
    # path('create_new_paycheck', views.create_new_paycheck, name='create_new_paycheck'),
    # path('delete_bill_from_paycheck/<str:paycheck_id>/<str:bill_id>', views.delete_bill_from_paycheck, name='delete_bill_from_paycheck'),
    # path('delete_paycheck/<str:paycheck_id>', views.delete_paycheck, name='delete_paycheck'),
    # path('add_bill_to_paycheck/<str:paycheck_id>/<path:bill_id>', views.add_bill_to_paycheck, name='add_bill_to_paycheck'),
    # path('update_money_in_bank/<str:paycheck_id>', views.update_money_in_bank, name='update_money_in_bank'),
    # path('pay_bill/<str:paycheck_id>/<str:bill_id>/<str:paid>', views.pay_bill, name='pay_bill'),
    # path('update_bill/<str:bill_id>', views.update_bill, name='update_bill'),
    # path('edit_paycheck/<str:paycheck_id>', views.edit_paycheck, name='edit_paycheck'),


]
