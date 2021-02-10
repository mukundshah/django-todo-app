from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.views import generic


from .models import Todo


class IndexView(generic.ListView):
    model = Todo
    tempelate_name = 'todo/todo_list.html'
    context_object_name = 'todos'

    def get_queryset(self):
        return Todo.objects.all().order_by("-created_at")


@csrf_exempt
def add_todo(request):
    current_date = timezone.now()
    title = request.POST["title"]
    description = request.POST["description"]
    created_obj = Todo.objects.create(
        created_at=current_date, title=title, description=description)
    return HttpResponseRedirect("/")


@csrf_exempt
def mark_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    if not todo.is_done:
        todo.is_done = True
    else:
        todo.is_done = False
    todo.save()
    return HttpResponseRedirect("/")


@csrf_exempt
def delete_todo(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect("/")
