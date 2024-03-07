from django.db import models


class CommonModel(models.Model):
    # 데이터 생성된 시간
    created_at = models.DateTimeField(auto_now_add=True)
    # 데이터가 업데이트된 시간 -> 업데이트된 시간으로 최신화가 이뤄져야함.
    updated_at = models.DateTimeField(auto_now=True)
    # 다른 컬럼들의 상속하기위해
    class Meta:
        abstract = True # DB데이블에 추가하지마라
