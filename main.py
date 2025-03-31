# This is a sample Python script.
from recipes import Recipe, MainDishRecipe
from data import ingredients_data, main_dish_data
from App import App



recipe_list = [MainDishRecipe(recipe_data['name'], recipe_data['prep_time'], recipe_data['level'], recipe_data['cooking_time'], recipe_data['ingredients']) for recipe_data in main_dish_data]

app = App(recipe_list).run()


