from rest_framework import routers
from recipe import views


router = routers.DefaultRouter(trailing_slash=False)

router.register('recipe', views.RecipeView, base_name='recipe')
router.register('step', views.StepView)
router.register('ingredient', views.IngredientView)
router.register('user', views.UserView)

for url in router.urls:
    print(url)