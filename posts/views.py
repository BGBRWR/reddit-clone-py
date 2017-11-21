from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from . import models
# Create your views here.


@login_required(login_url='/accounts/login/')
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['url']:
            post = models.Post()
            post.title = request.POST['title']
            post.url = request.POST['url']
            post.pub_date = timezone.datetime.now()
            post.author = request.user
            post.save()
        else:
            return render(request, 'posts/create.html', {'error': 'ERROR: You must include a title and a URL to create a post.'})

    else:
        return render(request, 'posts/create.html')
