from django.contrib import admin
from django.urls import path, include

from kyusanLLM.views import MessageView, InformationView, MessageConnectView

# app_name
app_name = 'kyusanLLM'

urlpatterns = [
    path('kyusan-message/', MessageView.as_view(), name='message'),
    path('kyusan-information/', InformationView.as_view(), name='information'),
    path('message-connect/', MessageConnectView.as_view(), name='message-connect'),
]