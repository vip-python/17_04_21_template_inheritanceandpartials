from django.urls import path
from app1 import views
app_name='app1'

urlpatterns = [
    path('samp1/',views.samp1,name='samp1'),
    path('samp2/',views.samp2,name='samp2'),
 ]
 
