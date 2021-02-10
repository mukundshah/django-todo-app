from django.urls import path

from . import views

app_name = 'todo'
urlpatterns = [
    # ex: /
    path('', views.IndexView.as_view(), name='index'),
    path('add/', views.add_todo, name='add'),
    path('delete_todo/<int:todo_id>/', views.delete_todo),
    path('mark_todo/<int:todo_id>/', views.mark_todo)
    # ex: /todos/5/del
    #path('todos/<pk>/del', views.delete, name='delete_todo')
]
