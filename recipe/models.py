from django.db import models

# Created simple User model just for easy testing 
class User(models.Model):

    username        = models.CharField(max_length=50, db_index=True, unique=True, blank=False, null=False)
    email           = models.EmailField(max_length=50, unique=True, blank=False, null=False)
    first_name      = models.CharField(max_length=50, db_index=True, blank=False, null=False)
    last_name       = models.CharField(max_length=50, db_index=True)
    password        = models.CharField(max_length=50)   

    def __str__(self):
        return self.username 


class Recipe(models.Model):
    name            = models.CharField(max_length=100, db_index=True, blank=False, null=False)
    creator         = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True) 

    def __str__(self):
        return self.name 


        
class Step(models.Model):    

    step_text       = models.CharField(max_length=200, blank=False, null=False)
    recipe          = models.ForeignKey(Recipe, related_name='steps', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.step_text     


class Ingredient(models.Model):
    text            = models.CharField(max_length=100, blank=False, null=False)
    recipe          = models.ForeignKey(Recipe, related_name='ingredients', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.text 