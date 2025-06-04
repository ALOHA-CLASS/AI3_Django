from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import *   # models 의 모든 모델 import

# Create your views here.
def index(request):
    print('메인 화면...')
    return render(request, 'todo/index.html', {})

def todo(request):
    print('할 일 목록 화면...')
    # 할 일 목록 조회
    todos = Todo.objects.all()  # Todo 모델의 모든 데이터 조회
    content = {'todos': todos}
    # render(request, 템플릿 경로, 데이터{})
    # - 데이터{} : 템플릿에 데이터를 전달
    return render(request, 'todo/todo.html', content)

def create(request):
    print('할 일 등록...')
    # POST 방식의 파라미터
    title = request.POST['title']
    # 등록 요청
    new_todo = Todo(title = title)
    new_todo.save()     # DB에 저장
    # 할 일 목록(todo)으로 리다이렉트
    return HttpResponseRedirect(reverse('todo'))


def delete(request):
    print("삭제 요청...")
    # 파라미터 
    no = request.POST['no']
    print('no : {}'.format(no))
    try:
        todo = Todo.objects.get(no=no)
        todo.delete()   # 할 일 삭제 요청
    except Todo.DoesNotExist:
        print('삭제할 할 일이 없습니다.')
    return HttpResponseRedirect(reverse('todo'))