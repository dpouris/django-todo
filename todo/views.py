from django.shortcuts import render
from .utils import *
from .models import Todo
from django.http import HttpResponseRedirect

# Create your views here.

def todo_home(request):
    all_items = Todo.objects.all()
    count = 0
    for i in all_items:
        if i.done == False:
            count = 1
            break
    
    if not handle_post(request):
        return render(request,'todo/todo.html',{
            "items" : all_items,
            'show_button' : count
        })

def todo_create(request):
    item = handle_post(request)
    
    if request.method=='POST' and item != '':
        create_item(item)
    return HttpResponseRedirect('/')

def delete_todo(request,item_id):
    delete_item(item_id)
    return HttpResponseRedirect('/')

def delete_all(request):
    Todo.objects.all().delete()
    return HttpResponseRedirect('/')

def update_todo(request,item_id):
    update_item(item_id)
    return HttpResponseRedirect('/')

def update_all_items(request):
    update_all()
    return HttpResponseRedirect('/')