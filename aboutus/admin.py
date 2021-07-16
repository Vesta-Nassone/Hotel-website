from django.contrib import admin

# Register your models here.
from .models import AboutUs, WhyChooseUs, Chefs

admin.site.register(AboutUs)
admin.site.register(WhyChooseUs)
admin.site.register(Chefs)

