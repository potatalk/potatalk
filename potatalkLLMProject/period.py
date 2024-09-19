from django.db import models
from django.utils import timezone

class Period(models.Model):
    createed_date = models.DateTimeField(null=False, auto_now_add=True)
    updated_date = models.DateTimeField(null=False, auto_now=timezone.now)

    class Meta:
        # migrate 시 해당 모델의 테이블 생성 X
        abstract = True