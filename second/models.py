from django.db import models

# Create your models here.
class Post(models.Model):
    # 문자열이 저장되는 곳이고 최대 30자 까지 문자열 가능
    title = models.CharField(max_length=30)
    # 문자열 길이 정해두지 않는 문자열 필드 생성
    content = models.TextField()

    # auto_now_add=True => 데이터가 생성될 때 자동으로 현재 시각 기록됨
    created_at = models.DateTimeField(auto_now_add=True)
    # auto_now=True => 수정될 때만 시각 추가 됨
    update_at = models.DateTimeField(auto_now=True)

