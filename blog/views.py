from django.shortcuts import render
# imports the posts from the database.
from .models import Post, Category
from .forms import CommentForm
from taggit.models import Tag

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
    form = CommentForm()
    all_tags = Tag.objects.all()
    context ={
        'post_detail': post_detail,
        'categories': categories,
        'form': form,
        'all_tags': all_tags
    }

    return render(request, 'post/post_detail.html', context)

def post_by_tag(request, tag):
    post_by_tag = Post.objects.filter(tags__name__in=[tag])
    context ={
        'post_list': post_by_tag,
    }

    return render(request, 'post/post_list.html', context)

def post_by_category(request, category):
    post_by_category = Post.objects.filter(category__category_name=category)
    context ={
        'post_list': post_by_category,
    }

    return render(request, 'post/post_list.html', context)
