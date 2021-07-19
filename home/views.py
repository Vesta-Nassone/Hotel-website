from django.shortcuts import render
from meals.models import Meals, Category

# Create your views here.
def home(request):
    meals = Meals.objects.all()
    meals_list = Meals.objects.all()
    categories = Category.objects.all()

    context = {
        'meals': meals,
        'meals_list': meals_list,
        'categories': categories,

    }

    return render(request, 'home/index.html', context)
