from django.contrib import admin
from django.urls import path, include

from jooLLM.views import MessageView, InformationView

app_name = 'jooLLM'

urlpatterns = [
    path('joo-message/', MessageView.as_view(), name='message'),
    path('joo-information/', InformationView.as_view(), name='information'),
]