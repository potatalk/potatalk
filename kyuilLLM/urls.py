from django.urls import path

from kyuilLLM.views import KyuilLLMView, InputAPI, OutputAPI

app_name = 'kyuilLLM'

urlpatterns = [
    path('kyuil/', KyuilLLMView.as_view(), name='kyuil'),
    path('kyuil/input/', InputAPI.as_view(), name='input'),
    path('kyuil/output/', OutputAPI.as_view(), name='output'),
]