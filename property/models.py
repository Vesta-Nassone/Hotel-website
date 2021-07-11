from django.db import models

# Create your models here.
class Property(models.Model):
    # property_type = {
    #     {
    #         'S', 'sale',
    #         'R', "rent"
    #     }
    # }
    name = models.CharField(max_length=50)
    location = ''
