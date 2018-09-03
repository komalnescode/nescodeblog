from django.urls import path
from . import views

app_name='donor'

urlpatterns = [
    path('', views.donor_info, name='donor_info'),
    path('item/', views.item, name='item'),
]