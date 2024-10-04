from django.urls import path

from songLLM.views import FinanceIntroView, FinanceChatbotView, FinanceChatbotAPI

app_name = 'songLLM'

urlpatterns = [
    # 금융 소개 페이지 이동
    path('song-intro/', FinanceIntroView.as_view(), name='finance-intro'),
    path('song-chatbot/', FinanceChatbotView.as_view(), name='finance-chatbot'),
    path('song-chatbot/send/', FinanceChatbotAPI.as_view())
]