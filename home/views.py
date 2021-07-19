from django.shortcuts import render
from meals.models import Meals, Category

# Create your views here.
def home(request):
    meals = Meals.objects.all()
    categories = Category.objects.all()

    context = {
        'meals': meals
        'categories': categories,

    }

    return render(request, 'home/index.html', context)
