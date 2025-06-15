# This script loads the recipes and runs the App.
# Run to start.

from recipes import Recipe, MainDishRecipe, DessertRecipe, CakeRecipe, IngredientItem
from data import ingredients_data, main_dish_data, dessert_data, cake_data
from App import App



recipe_list = [MainDishRecipe(recipe_data['name'], recipe_data['prep_time'], recipe_data['level'],
                            recipe_data['cooking_time'], recipe_data['ingredients'], recipe_data['text'],
                            is_vegetarian=recipe_data.get('is_vegetarian', False),
                            is_vegan=recipe_data.get('is_vegan', False),
                            need_oven=recipe_data.get('need_oven', False),
                            is_meal_prep=recipe_data.get('is_meal_prep', False)
                            ) for recipe_data in main_dish_data]
#recipe_list = [MainDishRecipe(main_dish_data[0]['name'], main_dish_data[0]['prep_time'], main_dish_data[0]['level'], main_dish_data[0]['cooking_time'], main_dish_data[0]['ingredients'], main_dish_data[0]['text']) ]

# Desserts
recipe_list += [DessertRecipe(recipe_data['name'], recipe_data['prep_time'], recipe_data['level'],
                            recipe_data['cooling_time'], recipe_data['ingredients'], recipe_data['text'],
                            is_meal_prep=recipe_data.get('is_meal_prep', False)
                            ) for recipe_data in dessert_data]

# Cakes
recipe_list += [CakeRecipe(recipe_data['name'], recipe_data['prep_time'], recipe_data['level'],
                           recipe_data['cooling_time'],recipe_data['baking_time'], recipe_data['ingredients'],
                           recipe_data['text'], is_meal_prep=recipe_data.get('is_meal_prep', False)
                           ) for recipe_data in cake_data]
#print(main_dish_data[0]['ingredients'])#
app = App(recipe_list).run()
#print(recipe_list[0].calculate_carbs())

