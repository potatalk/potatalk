import json
from langchain_openai import ChatOpenAI

from django.shortcuts import render
from django.views import View
from langchain_community.chat_models import ChatOpenAI

from potatalkLLMProject import settings


class InformationView(View):
    def get(self, request):
        return render(request, 'information/joo-information.html')

class MessageView(View):
    def get(self, request):
        return render(request, 'message/joo-message.html')



from django.http import JsonResponse
from django.views import View


class MessageConnectView(View):

    def post(self, request):
        try:
            if not request.body:
                print("Empty request body")
                return JsonResponse({'status': 'error', 'message': 'Empty request body'}, status=400)

            body_unicode = request.body.decode('utf-8')
            print("Request Body:", body_unicode)  # 디버깅을 위해 출력

            try:
                body_data = json.loads(body_unicode)
            except json.JSONDecodeError as json_err:
                print("JSON Decode Error:", json_err)
                return JsonResponse({'status': 'error', 'message': 'Invalid JSON format'}, status=400)

            client_message = body_data.get('clientMessage', '')

            if not isinstance(client_message, str):
                print("Invalid clientMessage type:", type(client_message))
                return JsonResponse({'status': 'error', 'message': 'clientMessage must be a string'}, status=400)

            user_input = client_message
            print("User Input:", user_input)

            # LLM 생성 및 응답
            llm = ChatOpenAI(
                temperature=0,
                model_name='ft:gpt-3.5-turbo-0125:personal::ANAkQhuG',
                openai_api_key=settings.OPENAI_API_KEY_NICK
            )

            # invoke 메서드로 호출
            response = llm.invoke(user_input)
            chatbot_response = response.content

            # 챗봇의 응답을 더 자연스럽게 변형
            friendly_response = f"제가 말씀드릴게요: {chatbot_response}. 혹시 더 궁금한 점이 있으신가요?"

            # 세션에 기록 - 'history' 키가 없으면 초기화
            if 'history' not in request.session:
                request.session['history'] = []

            request.session['history'].append((user_input, friendly_response))
            print('client_message: ', client_message)
            print('chatbot_response', friendly_response)

            return JsonResponse({
                'status': 'success',
                'client-message': client_message,
                'chatbot-response': friendly_response
            })

        except Exception as e:
            print("Exception:", str(e))
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
