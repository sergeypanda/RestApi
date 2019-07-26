from rest_framework import serializers
from recipe.models import Recipe, Step, Ingredient, User

import re


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        extra_kwargs = {'password': {'write_only': True}}
        fields = ('__all__')
    
    #simple field validation. better approach might be using custom validator classes in validators.py 
    def validate_password(self, password):
            if not re.findall('\d', password):
                raise serializers.ValidationError("The password must contain at least 1 digit, 0-9.")
            return password

    def validate_username(self, username):
            print(username)
            if len(username) <  2:
                raise serializers.ValidationError('Username is too small')
            return username
    

class StepSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="recipe:step-detail")
    class Meta:
        model = Step
        fields = ('id', 'url', 'step_text')
        

class IngredientSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="recipe:ingredient-detail")
    class Meta:
        model = Ingredient
        fields = ('id', 'url', 'text')


class RecipeSerializer(serializers.ModelSerializer):
    steps = StepSerializer(many=True, required=False)
    ingredients = IngredientSerializer(many=True, required=False)
    url = serializers.HyperlinkedIdentityField(view_name="recipe:recipe-detail")

    class Meta:
        model = Recipe
        fields = ('id', 'url', 'name', 'steps', 'ingredients', 'creator')
        extra_kwargs = {'creator': {'required': True, 'allow_null': False}}


    #This function redefinition will allow us to add full object of Recipe with steps and ingredients

    def create(self, validated_data):

        steps_data = validated_data.pop('steps')
        ingredients_data = validated_data.pop('ingredients')
        recipe = Recipe.objects.create(**validated_data)

        for step_data in steps_data:
            Step.objects.create(recipe=recipe, **step_data)

        for ingredient_data in ingredients_data:
            Ingredient.objects.create(recipe=recipe, **ingredient_data)

        return recipe
    

    #This function redefinition will allow us to save full object of Recipe with steps and ingredients
    #To make it simple with update of children I just delete previous steps and Ingreadiets and add updated ones
    def update(self, instance, validated_data):
        
        steps_data = validated_data.pop('steps')
        ingredients_data = validated_data.pop('ingredients')

        instance = super(RecipeSerializer, self).update(instance, validated_data)

        Step.objects.filter(recipe=instance).delete()
        Ingredient.objects.filter(recipe=instance).delete()

        for step_data in steps_data:
            Step.objects.create(recipe=instance, **step_data)

        for ingredient_data in ingredients_data:
            Ingredient.objects.create(recipe=instance, **ingredient_data)

        return instance
       


