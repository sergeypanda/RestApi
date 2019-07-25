
ULRS

'api/v1/recipe/' - List of recipies/Create a recipe
'api/v1/recipe/{id}' - get/update/delete a recipe

'api/v1/recipe?user_id={id}' -  get recipe by user_id

There are different ways of implementing these API operations. For example, we can use ViewSets or APIView.
APIView is more low level class, I would use it for more complex cases or cases when we need more flexibility. 
Based on requirements ViewSets would be simplier and sufficient to implement needed operaions.




