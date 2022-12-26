from django.urls import path
from . import views
app_name='patient'


urlpatterns=[
    path('doc_booking',views.patient_doc_booking,name='booking'),
    path('profile',views.patient_profile,name='profile'),
    path('booked',views.patient_booked,name='booked'),
]