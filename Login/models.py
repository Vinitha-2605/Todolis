from django.db import models

# Create your models here.

class Login(models.Model):
    Username = models.CharField(max_length=25)
    Password =  models.CharField(max_length=10)

    def __str__(self):
        return self.Username
    
class Register(models.Model):
    Username = models.CharField(max_length=10)
    Password = models.CharField(max_length=20)
    EMAIL = models.EmailField()
    def __str__(self):
        return self.Username

class TodoList(models.Model):
    title = models.CharField(max_length=25)
    description = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.title},{self.description}"

class TodoItem(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    duedate = models.DateField(default='2023-05-06')
    is_complete = models.BooleanField(default=False)
    todolist = models.ForeignKey(TodoList, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.todolist},{self.title},{self.description}"
    