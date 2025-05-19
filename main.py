# This is a sample Python script.
from recipes import Recipe, MainDishRecipe
from data import ingredients_data, main_dish_data
from App import App



#recipe_list = [MainDishRecipe(recipe_data['name'], recipe_data['prep_time'], recipe_data['level'], recipe_data['cooking_time'], recipe_data['ingredients'], recipe_data['text']) for recipe_data in main_dish_data]
recipe_list = [MainDishRecipe(main_dish_data[0]['name'], main_dish_data[0]['prep_time'], main_dish_data[0]['level'], main_dish_data[0]['cooking_time'], main_dish_data[0]['ingredients'], main_dish_data[0]['text']) ]

#print(main_dish_data[0]['ingredients'])
app = App(recipe_list).run()


