from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('myform/', views.myform),
    path('view', views.view_data),
    path('store', views.store_data),
    path('update/<rollno>', views.updatedata),
    path('updatedata/<rollno>', views.updaterecord),
    path('deletedata/<rollno>', views.delete_data),
]
