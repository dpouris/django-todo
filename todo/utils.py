from .models import Todo

def handle_post(req,item:str='item'):
    if req.method == 'POST':
        return req.POST.get(item)
    return

def create_item(item,model=Todo):
    model.objects.create(todo = item)

def delete_item(item,model = Todo):
    model.objects.get(id = item).delete()

def update_item(item,model = Todo):
    item_to_update = model.objects.get(id = item)
    if item_to_update.done: item_to_update.done = False
    else: item_to_update.done = True
    item_to_update.save()
    
def update_all():
    for i in Todo.objects.all():
        if not i.done: 
            i.done = True
            i.save()
            print(i.done)