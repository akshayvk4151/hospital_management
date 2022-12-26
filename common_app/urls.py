from django.urls import path
from . import views
app_name='common_app'


urlpatterns=[
    path('index',views.common_app_index,name='home'),
   
    path('about',views.common_app_about,name='about'),
    path('contact',views.common_app_contact,name='contact'),
    path('login',views.common_app_login,name='login'),
    path('register',views.common_app_register,name='register'),
    path('department',views.common_app_department,name='department'),
    path('doctors',views.common_app_doctors,name='doctors'),
    
]