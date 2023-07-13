from django.db import models


# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=30) # 이름
    address = models.CharField(max_length=200) # 주소

    # 기존에 사용되고 있는 모델에 필드추가 할때는 default속성으로 어떤 값 넣어주어야 함
    password = models.CharField(max_length=20, default=None, null=True)
    image = models.CharField(max_length=500, default=None, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Review(models.Model):
    point = models.IntegerField()
    comment = models.CharField(max_length=500)

    # on_delete CASCADE => 식당 삭제되면 리뷰도 삭제 되도록 해주는 것
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)