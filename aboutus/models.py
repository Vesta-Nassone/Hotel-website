from django.db import models

# Create your models here.
class AboutUs(models.Model):
    tittle = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(upload_to='about_us/')

    class Meta:
        verbose_name = _("about us")
        verbose_name_plural = _("about us")

        def __str__(self):
            return self.title
        

class WhyChooseUs(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()

    class Meta:
            verbose_name = _("why choose us")
            verbose_name_plural = _("why choose us")

            def __str__(self):
                return self.title
            

class Chefs(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    bio = models.TextField()
    image = models.ImageField(upload_to='chef/')

    class Meta:
            verbose_name = _("chef")
            verbose_name_plural = _("chefs")