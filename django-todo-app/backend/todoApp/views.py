from django.shortcuts import render, redirect
from todoApp.handlers import (fetch_todo, save_new_todo)
from django.urls import reverse

def TestView(request):
    return render(request, '../templates/index.html')

def index_view(request):
    """
    - Home page view where we are fetching all todos from the database
    - Listing down them in template
    """
    todo_list = fetch_todo()
    context_dict = {
        'todo_list' : todo_list,
    }
    return render(request, '../templates/index.html', context_dict)

def add_todo(request):
    """
    - View to add new todo from form template and save them in database
    - Post todo save, rednering the homepage
    """
    if request.method == 'GET':
        template = '../templates/add_todo.html'
        print('get method add todo')
        return render(request, template, {'error': None})
    elif request.method == 'POST':
        print('afafafa')
        todo_title = request.POST.get('todo_title')
        todo_details = request.POST.get('todo_details')
        todo_completion = True if request.POST.get('todo_completion') else False
        try:
            save_new_todo(todo_title, todo_details, todo_completion)
            print('afafafafa')
            return redirect(reverse('index_view'))
        except Exception as ex:
            return render(request, '../templates/add_todo.html', {'error': 'Some issue in last todo save ☹️'})
    else:
        raise Exception('add todo view method not applicable')