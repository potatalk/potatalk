import os
import json
import openai

from django.db import transaction
from django.shortcuts import render
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView
from dotenv import load_dotenv
from django.http import JsonResponse

# AI 모델
from langchain_openai import ChatOpenAI

from potatalkLLMProject import settings

# .env 파일에서 환경 변수 로드
load_dotenv()

# intro 페이지 이동
class FinanceIntroView(View):
    def get(self, request):
        return render(request, 'information/songLLM/songLLM-information.html')


# 챗봇 페이지 이동
class FinanceChatbotView(View):
    def get(self, request):
        return render(request, 'message/songLLM/songLLM-message.html')


class FinanceChatbotAPI(APIView):
    @transaction.atomic
    def post(self, request):
        data = request.data
        client_message = data['clientMessageText']

        # OpenAI API 키를 환경 변수에서 읽기
        api_key = os.getenv("SONG_OPENAI_API_KEY")

        # 모델로 뽑아내기
        llm_gpt = ChatOpenAI(temperature=0.3, model_name='ft:gpt-3.5-turbo-0125:personal::AEckZLFs', openai_api_key=api_key)

        response = llm_gpt.invoke(client_message)

        context = {
            'serverMessageText': f'{response.content}'
        }

        return Response(context)

# class FinanceChatbotAPI(APIView):
#     def post(self, request):
#         data = request.data
#
#         client_message = data['clientMessageText']
#
#         print(client_message)
#
#         # 모델로 뽑아내기
#         llm_gpt = ChatOpenAI(temperature=0, model_name='gpt-3.5-turbo', openai_api_key=settings.SONG_OPENAI_API_KEY)
#
#         server_llm = llm_gpt.predict(client_message)
#
#         print(server_llm)
#         print(type(server_llm))
#
#         context = {
#             'serverMessageText': f'{server_llm}'
#             # 'serverMessageText': f'{client_message}입니다.'
#         }
#
#         return Response(context)

    # llm_gpt = ChatOpenAI(temperature=0, model_name='gpt-3.5-turbo'
    # OpenAIError(
    # openai.OpenAIError: The api_key client option must be set either by passing api_key to the client or by setting the OPENAI_API_KEY environment variable