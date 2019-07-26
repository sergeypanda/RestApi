from django.db import models
from django.contrib.auth.models import User

# Design the User Model with username(unique field), email(unique field), first_name,
# last_name,m password. (You can use the django inbuilt user model)

# Commented out. Using django inbuilt user model instead
'''class User(models.Model):

    username        = models.CharField(max_length=50, db_index=True, unique=True, blank=False, null=False)
    email           = models.EmailField(max_length=50, unique=True, blank=False, null=False)
    first_name      = models.CharField(max_length=50, db_index=True, blank=False, null=False)
    last_name       = models.CharField(max_length=50, db_index=True)
    password        = models.CharField(max_length=50)   

    def __str__(self):
        return self.username 
'''

# Design A Recipe Model with name(string, not null), Foreign Key to User table(one to one
# relationship), One to Many relationship with Step and Ingredient Model
class Recipe(models.Model):
    name            = models.CharField(max_length=100, db_index=True, blank=False, null=False)
    creator         = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True) 

    def __str__(self):
        return self.name 


# Design A Step Model with step_text(string field, not null), Many to One relationship with
# Recipe       
class Step(models.Model):    

    step_text       = models.CharField(max_length=200, blank=False, null=False)
    recipe          = models.ForeignKey(Recipe, related_name='steps', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.step_text     

# Design An Ingredient Model with text(not null, string), Many to One relationship with
# Recipe
class Ingredient(models.Model):
    text            = models.CharField(max_length=100, blank=False, null=False)
    recipe          = models.ForeignKey(Recipe, related_name='ingredients', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.text 