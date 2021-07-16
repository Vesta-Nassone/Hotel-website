from django.shortcuts import render
from .models import AboutUs, WhyChooseUs, Chefs

# Create your views here.
def aboutus_list(request):
    about = AboutUs.objects.last()
    why_choose_us = WhyChooseUs.objects.last()
    chef = Chefs.objects.last()

    context = {
        'about': about,
        'why_choose_us': why_choose_us,
        'chef': chef,

    }

    return render(request, 'aboutus/about.html', context)
