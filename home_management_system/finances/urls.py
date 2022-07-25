
from django.contrib import admin
from django.urls import path
from . import views

app_name = 'finances'
urlpatterns = [
    path('', views.index, name='index'),
    path('create_new_bill', views.create_new_bill, name='create_new_bill'),
    path('create_new_paycheck', views.create_new_paycheck, name='create_new_paycheck'),
    path('delete_bill/<str:name>/<path:date>/<str:bill>', views.delete_bill, name='delete_bill'),
    path('add_bill_to_paycheck/<str:name>/<path:date>', views.add_bill_to_paycheck, name='add_bill_to_paycheck'),
    path('update_money_in_bank/<str:name>/<path:date>', views.update_money_in_bank, name='update_money_in_bank'),

]
