from django.urls import path
from . import views
urlpatterns=[
    path('',views.app,name='app'),
    path('register_form_submission',views.register_form_submission,name='register_form_submission'),

]