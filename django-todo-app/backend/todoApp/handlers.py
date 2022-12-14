from turtle import title
from todoApp.models import Todo

# handler method to fetch all todo items from the model/ database
def fetch_todo():
    todo_list = Todo.objects.values()
    todos = [todo for todo in todo_list]
    return todos

# handler method to save new todo from customer to database
def save_new_todo(title, detail, is_completed):
    new_todo = Todo(title=title, detail=detail, isCompleted=is_completed)
    new_todo.save()

# handler method to delete a todo from database
def delete_todo_handler(id):
    Todo.objects.filter(id=id).delete()
    print('deleted')