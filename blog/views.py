from django.shortcuts import render
# imports the posts from the database.
from .models import Post, Category
from .forms import NameForm

# Create your views here.

def post_list(request):
    post_list = Post.objects.all()

    context = {
        'post_list': post_list,
    }

    return render(request, 'post/post_list.html', context)

def post_detail(request, id):
    post_detail = Post.objects.get(id=id)
    categories = Category.objects.all()
    form = NameForm()
    context ={
        'post_detail': post_detail,
        'categories': categories,
        'form': form,
    }

    return render(request, 'post/post_detail.html', context)
