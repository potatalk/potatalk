import json
import openai
from openai import OpenAI

import pandas as pd
from django.test import TestCase
from dotenv import load_dotenv

import os

from songLLM.models import songLLM

# .env 파일에서 환경 변수 로드
load_dotenv()

class SongLLMTest(TestCase):
    # # 데이터 생성
    # csv_path = r'C:\study\project\potatalk\backup\data\dataset\songllm_insert.csv'
    # df = pd.read_csv(csv_path)
    #
    # for i in range(len(df)):
    #     data = {
    #         'question': df.question[i],
    #         'answer':  df.answer[i],
    #         'status': 1
    #     }
    #
    #     try:
    #         songLLM.objects.create(**data)
    #     except Exception as e:
    #         print('에러')

    # # 데이터 형식 변경
    # import json
    #
    # # 기존 파일 경로
    # input_file_path = r"C:\study\project\potatalk\backup\data\dataset\songllmdata_prepared.jsonl"
    # output_file_path = r"C:\study\project\potatalk\backup\data\dataset\songllm_chat_completion_format.jsonl"
    #
    # # 데이터 로드
    # data = []
    #
    # with open(input_file_path, 'r', encoding='utf-8') as file:
    #     for line in file:
    #         data.append(json.loads(line))
    #
    # # 데이터를 Chat-completion 형식으로 변환
    # converted_data = []
    #
    # for entry in data:
    #     chat_completion_format = {
    #         "messages": [
    #             {"role": "user", "content": entry['prompt'].replace(' ->', '')},
    #             {"role": "assistant", "content": entry['completion'].strip()}
    #         ]
    #     }
    #     converted_data.append(chat_completion_format)
    #
    # # 변환된 데이터를 다시 파일로 저장
    # with open(output_file_path, 'w', encoding='utf-8') as output_file:
    #     for entry in converted_data:
    #         output_file.write(json.dumps(entry, ensure_ascii=False) + '\n')
    #
    # print("파일이 성공적으로 저장되었습니다:", output_file_path)

    # 데이터 로드
    # try:
    #     client = OpenAI(
    #         api_key="key"
    #     )
    #
    #     file = client.files.create(
    #         file=open(r"C:\study\project\potatalk\backup\data\dataset\songllm_chat_completion_format.jsonl", "rb"),
    #         purpose="fine-tune"
    #     )
    #
    #     client.fine_tuning.jobs.create(
    #         training_file=file.id,
    #         model="gpt-3.5-turbo"
    #     )
    #
    # except Exception as e:
    #     print(f'실패: {str(e)}')


    pass
