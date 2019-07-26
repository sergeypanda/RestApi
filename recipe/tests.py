from rest_framework.test import APITestCase
from django.urls import reverse 
from rest_framework import status

from .models import Recipe

from django.contrib.auth import get_user_model

#few tests
User = get_user_model()

class RecipeAPITestCase(APITestCase):
    def setUp(self):
        user = User(username='Quincy', email='test@test.com', password='zaq123')
        user.save()
        recipe = Recipe.objects.create(
            name ='Pizza',
            creator = user,
        )

    #test getting recepies       
    def test_get_list(self):
        ticker = Recipe.objects.first()
        data = {}
        url = reverse("api-v1:recipe-list")
        response = self.client.get(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    #testing 1 to 1 relationship recipe to user
    def test_one_to_one_rel(self):
        user = User.objects.first()

        data = {'name': 'Chimichanga', 'creator': user.pk}

        url = reverse("api-v1:recipe-list")
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    #test adding recepies
    def test_add_recipe(self):

        user = User(username='Jerry', email='test2@test.com', password='zaq123')
        user.save()

        data = {'name': 'Sushi', 'creator': user.pk,

             'steps':[
                {"step_text": "boil water"},
                {"step_text": "cut fish"}], 
                'ingredients':[
                {"text": "rice"},
                {"text": "fish"}],
            }

        url = reverse("api-v1:recipe-list")
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        recipes = Recipe.objects.all()
        self.assertEqual(recipes.count(), 2)

