from django.contrib import admin
from .models import Recipe, Step, Ingredient, User

# Register your models here.
admin.site.register(Recipe)
admin.site.register(Step)
admin.site.register(Ingredient)
admin.site.register(User)