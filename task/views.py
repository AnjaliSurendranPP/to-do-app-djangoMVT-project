from django.shortcuts import render,redirect,get_object_or_404
from task.models import Task

# Create your views here.
def get(request):
    completed_tasks=Task.objects.filter(is_completed=True)
    pending_tasks=Task.objects.filter(is_completed=False)
    print(pending_tasks)
    print(completed_tasks)
    return render(request,'tasks\home.html',{'pending_tasks':pending_tasks,'completed_tasks':completed_tasks})

def add_task(request):
    if request.method=='POST':
        title=request.POST.get('title')
        description=request.POST.get('description')
        due_date=request.POST.get('due_date')

        Task.objects.create(title=title,description=description,due_date=due_date)
        return redirect('home')
    return render(request,'tasks/add_task.html')

def edit_task(request,id):
    task = get_object_or_404(Task, id=id)
    print("Task ID:", task.id)
    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.due_date = request.POST.get('due_date')
        task.save()
        print("Task ID:", task.id)
        return redirect('home')
    return render(request, 'tasks/edit_task.html', {'task': task})

def delete_task(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == 'POST':
        task.delete()
        return redirect('home')
    return render(request, 'tasks/delete_task.html', {'task': task})

def complete_task(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == 'POST':
        task.is_completed = not task.is_completed
        task.save()
    return redirect('home')