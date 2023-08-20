from rest_framework import viewsets
from .models import Todo
from .serializers import TodoSerializer
from django.shortcuts import render
from django.utils import timezone


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


def update_todos_same_date(request, date_str):
    date = timezone.datetime.strptime(date_str, "%Y-%m-%d").date()
    todos = Todo.objects.filter(created_date=date)

    return render(request, 'update_todos_same_date.html', {'todos': todos})

def delete_todos_same_date(request, date_str):
    date = timezone.datetime.strptime(date_str, "%Y-%m-%d").date()
    todos = Todo.objects.filter(updated_date=date)

    return render(request, 'delete_todos_same_date.html', {'todos': todos})

def delete_todos_same_name(request, todo_title):
    todos = Todo.objects.filter(title=todo_title)

    return render(request, 'delete_todos_same_name.html', {'todos': todos})
