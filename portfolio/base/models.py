from django.db import models
from django.contrib.auth.models import User


class Countries(models.Model):
    name = models.CharField(max_length=256, help_text='max_length=256')
    description = models.CharField(max_length=256, help_text='max_length=256', blank=False)
    img = models.ImageField(upload_to='base/countries/img/')
    flag = models.ImageField(upload_to='base/countries/flag/')

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Countries"


class Dish(models.Model):
    name = models.CharField(max_length=256, help_text='max_length=256')
    description = models.CharField(max_length=256, help_text='max_length=256', blank=True)
    main_img = models.ImageField(upload_to='base/dish_img/', blank=True, null=True)
    country = models.ForeignKey(Countries, on_delete=models.CASCADE, null=True)
    recipe = models.CharField(max_length=2048, help_text='max_length=2048', blank=True, null=True, default=None)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = "National Dish"
        verbose_name_plural = "National Dishes"


class DishImg(models.Model):
    name = models.CharField(max_length=256, help_text='name of picture (name_"img")')
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, null=True)
    img = models.ImageField(upload_to='base/dish_img/')
    is_activ = models.BooleanField(default=False)
    upload = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Images"


class Comment(models.Model):
    comment = models.CharField(max_length=5000)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)
    is_created = models.DateTimeField(auto_now_add=True, auto_now=False)
    is_updated = models.DateTimeField(auto_now_add=False, auto_now=True)




