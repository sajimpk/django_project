from . import views
from django.urls import path

urlpatterns = [
    path('',views.home,name='cont'),
    path('add',views.ad,name='add'),
    
   
]