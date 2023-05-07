from django.shortcuts import render
from Login.forms import TodoListForm, TodoItemForm
from Login.models import TodoItem, TodoList
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

def createtodo(request):
    if (request.method == "POST"):
        form = TodoListForm(request.POST)

        if form.is_valid():
          todolist = TodoList(title = form.cleaned_data['title'], description =form.cleaned_data['description'])
          todolist.save()
          return HttpResponse("Saved Suucessfully")
        
    else:
         todoform = TodoListForm()
         return render(request, 'TodoList.html',{
            "todoforms": todoform,
         })

def createtodo_item(request):
    if (request.method == "POST"):
         formtodo = TodoItemForm(request.POST)
         if formtodo.is_valid():
          todoItem = TodoItem(title = formtodo.cleaned_data['title'], 
                              description = formtodo.cleaned_data['description'],
                              duedate = formtodo.cleaned_data['duedate'],
                              is_complete = formtodo.cleaned_data['is_complete'],
                              todolist = formtodo.cleaned_data['todolist'])
          todoItem.save()
          return HttpResponse("Saved Suucessfully")
        
    else:
         todoitemform = TodoItemForm()
         return render(request, 'TodoItem.html',{
            "todoitemform": todoitemform
        })
    
def gettodo_list_itemId(request):
    tododetails = TodoList.objects.all()
    todoitemdetails = TodoItem.objects.all()
    return render(request, "TodoDetails.html",{
        "forms": tododetails,
        "todoitemforms": todoitemdetails
    })

def gettodo_list(request, id):
    try:
     if (request.method == "POST"):
        form = TodoListForm(request.POST)

        if form.is_valid():
          tododetails = TodoList.objects.get(id=id)
          tododetails.title = form.cleaned_data['title']
          tododetails.description = form.cleaned_data['description']
          tododetails.save()
          return HttpResponse("Saved Suucessfully")
     else:
      tododetails = TodoList.objects.get(id=id)
      form = TodoListForm()
      form.initial['title'] = tododetails.title
      form.initial['description'] = tododetails.description

      return render(request, "TodoList.html", {
        "todoforms":form
    })
    except:
     return HttpResponseNotFound("No data is present")

def gettodo_item(request, id):
    if (request.method == "POST"):
        form = TodoItemForm(request.POST)

        if form.is_valid():
          tododetails = TodoItem.objects.get(id=id)
          tododetails.title = form.cleaned_data['title']
          tododetails.description = form.cleaned_data['description']
          tododetails.duedate = form.cleaned_data['duedate']
          tododetails.save()
          return HttpResponse("Saved Suucessfully")
    else:
     tododetails = TodoItem.objects.get(id=id)
     form = TodoItemForm()
     form.initial['title'] = tododetails.title
     form.initial['description'] = tododetails.description
     form.initial['duedate'] = tododetails.duedate
     form.initial['is_complete'] = tododetails.is_complete
     form.initial['todolist'] = tododetails.todolist

    return render(request, "TodoItem.html", {
        "todoitemform":form
    })

def tododelete(request, id):
    tododetails = TodoList.objects.get(id=id)
    tododetails.delete()
    return HttpResponse("Deleted Suucessfully")

def todoitem_delete(request, id):
    tododetails = TodoItem.objects.get(id=id)
    tododetails.delete()
    return HttpResponse("Deleted Successfully")