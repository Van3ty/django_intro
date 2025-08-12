from django.shortcuts import render
from django.http import HttpResponse
from django_intro.tasks.models import Task
# Create your views here.



def home(request):
    items = Task.objects.all()
    item_strings = (f'<li>{t.title}</li>' for t in items)
    items_string = ''.join(item_strings)
    html = f'''
<h1>It works</h1>
<ul>
    {items_string}
</ul>
    '''

    return HttpResponse(html)