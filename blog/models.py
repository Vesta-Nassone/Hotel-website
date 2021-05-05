from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # tags
    category = models.ForeignKey('Category', null=True, on_delete=models.SET_NULL)
    created = models.DateTimeField(default=timezone.now)
   
class Category(models.Model):
    category_name = models.CharField(max_length=50)
