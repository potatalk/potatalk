from django.urls import path
from kangLLM.views import MessageView, InformationView

app_name = 'kangLLM'

urlpatterns = [
    path('message/', MessageView.as_view(), name='message'),
    path('information/', InformationView.as_view(), name='information'),
    path('message/send/', MessageView.as_view(), name='message_send'),
]