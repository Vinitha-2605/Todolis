from django.urls import path
from . import views

urlpatterns =[
    path("", views.createtodo),
    path("todoitem", views.createtodo_item),
    path("tododetails", views.gettodo_list_itemId),
    path("/<id>", views.gettodo_list),
    path("todoitems/<id>", views.gettodo_item),
    path("tododelete/<id>", views.tododelete, name="delete"),
    path("todoitemdelete/<id>", views.todoitem_delete, name="tododelete")
]