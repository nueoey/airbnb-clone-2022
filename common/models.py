from django.db import models

# 이 모델은 DB에 추가하기 위한 모델이 아니라, 다른 모델들에서 재사용하기 위한 모델. 즉, 모델의 blueprint 같은 개념


class CommonModel(models.Model):

    """Common Model Definition"""

    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    # auto_now_add는 필드값을 해당 object가 처음 생성되었을 때의 시간으로 설정함
    updated_at = models.DateTimeField(
        auto_now=True,
    )
    # auto_now는 필드값을 해당 object가 저장될 때마다 그 때의 시간으로 설정함

    class Meta:
        abstract = True
        # abstract 모델: 장고가 이 모델을 봐도 이를 DB에 저장하지 않음
