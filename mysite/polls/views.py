from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("Hello, World. 수행과제 중간 발표에 오신것을 환영합니다.")
