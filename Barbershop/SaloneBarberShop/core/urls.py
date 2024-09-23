from django.contrib import admin
from django.urls import path ,include
from .views import *
from . import views
import os
urlpatterns = [
    path('', homepage, name='homepage'),
    path('signupstudent/',Signupclient.as_view()  , name='signupstudent'),
    path('loginstudent/',Loginclient, name='loginstudent'),
    path('loginadmin/',loginadmin, name='loginadmin'),
    path('adminpage/',adminpage, name='adminpage'),
    path('search',views.search,name='search'),
    path('service',views.service,name='service'),
    path('booking',views.booking,name='booking'),
    path('success/', booking_success_view, name='booking_success'),



]