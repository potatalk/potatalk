from django.db import models

from potatalkLLMProject.period import Period

class songLLM(Period):
    # 인덱스 생성은 되지 않습니다.
    question = models.TextField(null=True, blank=True)
    answer = models.TextField(null=True, blank=True)
    # 0: 삭제
    status = models.BooleanField(null=False, blank=False, default=1)

    class Meta:
        db_table = 'tbl_song_llm'