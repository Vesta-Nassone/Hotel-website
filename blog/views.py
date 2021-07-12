from django.shortcuts import render
# imports the posts from the database.
from .models import Post, Category

# Create your views here.

def post_list(request):
    post_list = Post.objects.all()

    context = {
        'posts_list': post_list
    }

    return render(request, 'post/post_list.html', context)

def post_detail(request, id):
    pass
