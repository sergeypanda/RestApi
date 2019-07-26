from rest_framework import viewsets
from .models import Recipe, Step, Ingredient, User
from .api.serializers import RecipeSerializer, StepSerializer, IngredientSerializer, UserSerializer


class RecipeView(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    
    # this will allow us to access recipies by user id  like this /api/v1/recipe?user_id={id}
    # Because Recipe has 1-1 relationship with User this will return us an array with 1 element 
    def get_queryset(self):
        user_id = self.request.GET.get("user_id")
        if user_id is not None:
            return Recipe.objects.filter(creator_id=user_id)
        else:
            return Recipe.objects.all()
    
    
class StepView(viewsets.ModelViewSet):
    queryset = Step.objects.all()
    serializer_class = StepSerializer

class IngredientView(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

    
class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer







