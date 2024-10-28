from django.db import transaction
from django.shortcuts import render
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView

from kyuilLLM.models import kyuilLLM
from langchain_openai import ChatOpenAI

from potatalkLLMProject import settings


class KyuilLLMView(View):
    def get(self, request):
        return render(request, 'message/kyuil-message.html')


class InputAPI(APIView):
    @transaction.atomic
    def post(self, request):
        data = request.data

        # 유저의 질문
        user_input = data['reply_content']

        # GPT 모델을 사용하여 답변 생성 (retriever 필요 없음)
        llm = ChatOpenAI(temperature=0, model_name='ft:gpt-3.5-turbo-0125:personal::AFdUlGjP', openai_api_key=settings.OPENAI_API_KEY_KYUIL)
        # llm = ChatOpenAI(temperature=0, model_name='gpt-3.5-turbo-0125', openai_api_key=settings.OPENAI_API_KEY_KYUIL)

        # 'invoke()' 메소드로 문자열을 전달
        response = llm.invoke(user_input)

        # print(response)

        # `AIMessage` 객체에서 텍스트 응답을 추출
        # AI의 대답
        chatbot_response = response.content  # AIMessage 객체에서 content 속성을 사용

        data = {
            # 입력된 질문
            'question': data['reply_content'],
            # 그에따른 대답
            'answer': chatbot_response
        }

        # DB에 저장
        kyuilLLM.objects.create(**data)

        return Response('success')


class OutputAPI(APIView):
    def get(self, request):

        replies = kyuilLLM.objects.filter(status=1).values('question', 'answer')

        # print(replies)

        data = {
            'replies': replies
        }

        return Response(data)