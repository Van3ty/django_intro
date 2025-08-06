from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.



def home(request):
    items = ''.join(f'<li>{i}</li>' for i in range(4))
    html = f'''
<h1>It works</h1>
<ul>
    {items}
</ul>
    '''

    return HttpResponse(html)