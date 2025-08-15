from django.shortcuts import render
from django.http import HttpResponse
from django_intro.tasks.models import Task
from django.shortcuts import render
# Create your views here.



# def home(request):
#     items = Task.objects.all()
#     item_strings = (f'<li>{t.title}</li>' for t in items)
#     items_string = ''.join(item_strings)
#     html = f'''
# <h1>It works</h1>
# <ul>
#     {items_string}
# </ul>
#     '''

#     return HttpResponse(html)

def home(request):
    context = {
        'title': 'It works from the home view',
        'tasks': Task.objects.all(),
        # 'tasks': [],
    }

    return render(request, "home.html", context)