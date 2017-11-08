from django.contrib import admin
from .models import *


class CountriesAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Countries._meta.fields]

    class Meta:
        model = Countries


admin.site.register(Countries, CountriesAdmin)


class DishImgInline(admin.TabularInline):
    model = DishImg
    extra = 0


class DishAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Dish._meta.fields]
    inlines = [DishImgInline]

    class Meta:
        model = Dish


admin.site.register(Dish, DishAdmin)


class DishImgAdmin(admin.ModelAdmin):
    list_display = [field.name for field in DishImg._meta.fields]

    class Meta:
        model = DishImg


admin.site.register(DishImg, DishImgAdmin)

