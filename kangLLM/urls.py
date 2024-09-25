from django.urls import path
from kangLLM.views import KangLLMView

app_name = 'kangLLM'

urlpatterns = [
    path('wine/', KangLLMView.as_view())
]