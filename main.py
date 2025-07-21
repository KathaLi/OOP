# This script loads the recipes and runs the App.
# Run to start.
# Recipe data is only exemplary, therefore only some ingredients can be found.
# Here are some examples: Broccoli, egg, apple

from recipes import MainDishRecipe, DessertRecipe, CakeRecipe
from data import main_dish_data, dessert_data, cake_data
from App import App


# Load MainDishRecipe data and create instances of the class MainDishRecipe
recipe_list = [MainDishRecipe(recipe_data['name'], recipe_data['prep_time'], recipe_data['level'],
                            recipe_data['cooking_time'], recipe_data['ingredients'], recipe_data['text'],
                            is_vegetarian=recipe_data.get('is_vegetarian', False),
                            is_vegan=recipe_data.get('is_vegan', False),
                            need_oven=recipe_data.get('need_oven', False),
                            is_meal_prep=recipe_data.get('is_meal_prep', False)
                            ) for recipe_data in main_dish_data]

# Load Dessert data and create instances of the class DessertRecipe
recipe_list += [DessertRecipe(recipe_data['name'], recipe_data['prep_time'], recipe_data['level'],
                            recipe_data['cooling_time'], recipe_data['ingredients'], recipe_data['text'],
                            is_meal_prep=recipe_data.get('is_meal_prep', False)
                            ) for recipe_data in dessert_data]

# Load Cake data and create instances of the class CakeRecipe
recipe_list += [CakeRecipe(recipe_data['name'], recipe_data['prep_time'], recipe_data['level'],
                           recipe_data['cooling_time'],recipe_data['baking_time'], recipe_data['ingredients'],
                           recipe_data['text'], is_meal_prep=recipe_data.get('is_meal_prep', False)
                           ) for recipe_data in cake_data]

# Start App
app = App(recipe_list).run()


