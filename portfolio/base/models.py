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

class TypesOfDishes(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None) #type
    main_img = models.ImageField(upload_to='base/type_dish_img/', blank=True, null=True)
    description = models.CharField(max_length=256, help_text='max_length=256', blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = "Type"
        verbose_name_plural = "Types"


class Dish(models.Model):
    name = models.CharField(max_length=256, help_text='max_length=256')
    description = models.CharField(max_length=256, help_text='max_length=256', blank=True)
    main_img = models.ImageField(upload_to='base/dish_img/', blank=True, null=True)
    country = models.ForeignKey(Countries, on_delete=models.CASCADE, null=True)
    type = models.ForeignKey(TypesOfDishes, on_delete=models.CASCADE, null=False, default=None)
    recipe = models.CharField(max_length=2048, help_text='max_length=2048', blank=True, null=True, default=None)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = "Dish"
        verbose_name_plural = "Dishes"


class DishImg(models.Model):
    name = models.CharField(max_length=256, help_text='name of picture (name_"img")')
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, null=True)
    img = models.ImageField(upload_to='base/dish_img/')

    is_active = models.BooleanField(default=False)
    upload = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Images"



class Comment(models.Model):
    comment = models.TextField('Comment')
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True)

    is_active = models.BooleanField(default=False)
    is_created = models.DateTimeField(auto_now_add=True, auto_now=False)
    is_updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.dish

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"




