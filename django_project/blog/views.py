from django.shortcuts import render
from django.http import HttpResponse
from .models import Post




posts=[
    {
        'author':'Corey',
        'title':'Blog Post 1',
        'content':'First Post Content',
        'date_posted':'August'
    },
    {
        'author':'Jane',
        'title':'Blog Post 2',
        'content':'First Post Content 3',
        'date_posted':'April'
    }
]
def home(request):
    context = {
        'posts':Post.objects.all()
    }
    return render(request, 'home.html',context)

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})