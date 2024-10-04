import json

from django.db.models import Q, Count
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.utils import timezone
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView

# GPT API 를 사용하기 위한 라이브러리
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain import LLMChain
from potatalkLLMProject import settings


# 메세지 설명창으로 이동하는 view
class InformationView(View):
    def get(self, request):
        return render(request, 'information/kyusan-information.html')

# 메세지 입력창으로 이동하는 view
class MessageView(View):
    def get(self, request):
        return render(request, 'message/kyusan-message.html')

# class MessageConnectView(View):
#     def post(self, request):
#         # POST 요청 처리
#         try:
#             body_unicode = request.body.decode('utf-8')
#             body_data = json.loads(body_unicode)
#
#             client_message = body_data.get('clientMessage', '')
#             server_message = body_data.get('serverMessage', '')
#
#             # 처리 후 JSON 응답 반환
#             return JsonResponse({
#                 'status': 'success',
#                 'clientMessage': client_message,
#                 'serverMessage': server_message
#             })
#         except Exception as e:
#             # 에러 처리
#             return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

class MessageConnectView(View):
    def post(self, request):
        # POST 요청 처리
        try:
            body_unicode = request.body.decode('utf-8')
            body_data = json.loads(body_unicode)

            # query
            client_message = body_data.get('clientMessage', '')
            # 불필요
            # server_message = body_data.get('serverMessage', '')

            user_input = client_message
            print(user_input)

            # GPT-3.5-turbo 모델을 사용하여 답변 생성 (retriever 필요 없음)
            llm_origin = ChatOpenAI(temperature=0, model_name='gpt-3.5-turbo', openai_api_key=settings.OPENAI_API_KEY)

            response_origin = llm_origin.invoke(user_input)
            chatbot_response = response_origin.content  # AIMessage 객체에서 content 속성을 사용
            print(f"chatbot_response{chatbot_response}")

            # GPT-3.5-turbo 을 fine-tuning 한 모델을 사용하여 답변 생성
            llm = ChatOpenAI(temperature=0.3, model_name='ft:gpt-3.5-turbo-0125:personal::AEYIQstN',
                             openai_api_key=settings.OPENAI_API_KEY)

            # 'invoke()' 메소드로 문자열을 전달
            response = llm.invoke(user_input)

            # `AIMessage` 객체에서 텍스트 응답을 추출
            chatbot_response = response.content  # AIMessage 객체에서 content 속성을 사용

            # 챗봇의 응답을 세션에 저장
            request.session['history'].append((user_input, chatbot_response))  # GPT가 반환하는 텍스트 응답
            print('client_message: ', client_message)
            print('chatbot_response', chatbot_response)
            return JsonResponse({
                'status': 'success',
                'client-message': client_message,
                'chatbot-response': chatbot_response
            })

        except json.JSONDecodeError as json_err:
            print("JSONDecodeError:", json_err)
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON format'}, status=400)
        except Exception as e:
            print("Exception:", str(e))
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

