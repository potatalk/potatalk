from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
import os
import json
import openai
from dotenv import load_dotenv

# .env 파일에서 환경 변수 로드
load_dotenv()


class MessageView(View):
    def get(self, request):
        print('들어옴')
        return render(request, 'message/kangLLM-message.html')

    def post(self, request, *args, **kwargs):
        try:
            # JSON 데이터 파싱
            message_data = json.loads(request.body.decode('utf-8'))
            wine_info = message_data.get('wine')  # 'wine' 키에서 정보 추출

            # OpenAI API 키를 환경 변수에서 읽기
            api_key = os.getenv("OPENAI_API_KEY")
            openai.api_key = api_key  # API 키 설정

            # API 호출
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": f"이 {wine_info} 대해 설명해줘: 특정한 와인으로 추천하고, 한국이름, 영어이름, 포도 품종, 산미, 타닌, 바디감"}
                ]
            )

            # 응답 내용을 출력
            print(response.choices[0].message['content'])

            # 성공적인 응답을 반환합니다.
            return JsonResponse({'status': 'success', 'data': response.choices[0].message['content']})

        except Exception as e:
            print(f"Error: {str(e)}")
            return JsonResponse({'status': 'error', 'message': str(e)})
class InformationView(View):
    def get(self, request):
        return render(request, 'information/kang-information.html')
