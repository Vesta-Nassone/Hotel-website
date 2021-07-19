from django.shortcuts import render
from meals.models import Meals, Category
from blog.models import Post

# Create your views here.
def home(request):
    meals = Meals.objects.all()
    meals_list = Meals.objects.all()
    categories = Category.objects.all()
    posts = Post.objects.all()

    context = {
        'meals': meals,
        'meals_list': meals_list,
        'categories': categories,
        'posts': posts,

    }

    return render(request, 'home/index.html', context)
