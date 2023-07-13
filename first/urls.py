from django.urls import path, re_path

from . import views
urlpatterns = [
    # '' = 아무것도 입력안한 url
    # 들어오자마자 보여질 페이지는 index 메소드가 제공해주는 값으로 하겠다
    path('', views.index, name="index"),
    path('select/', views.select, name="select"),
    path('result/', views.result, name="result"),

]