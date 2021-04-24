from django.shortcuts import render

# Create your views here.

def meal_list(request):
    meal_list = Meals.objects.all()

    return render(request, 'meal/list.html', context)

def meal_detail(request, slug):
    pass