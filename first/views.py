from django.shortcuts import render
from django.http import HttpResponse

from django.template import loader
from datetime import datetime

import random

# Create your views here.
def index(request):
    # 현재시간 불러오기
    now = datetime.now()
    # 삽입할 변수들을 object로 정의
    context = {
        'current_date': now
    }
    # context는 index.html을 렌더링해서 response로 보낼때 삽입하기 원하는 데이터
    return render(request, 'first/index.html', context)


def select(request):
    context = {}
    return render(request, 'first/select.html', context)


def result(request):
    chosen =int(request.GET['number'])
    results = []
    if chosen >=1 and chosen <= 45:
        results.append(chosen)
    box = []
    for i in range(0,45):
        if chosen != i+1:
            box.append(i+1)

    random.shuffle(box)

    while len(results) < 6:
        results.append(box.pop())
    context = {
        'numbers': results
    }
    return render(request, 'first/result.html', context)
