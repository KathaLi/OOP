# This is a sample Python script.
from recipes import Recipe, MainDishRecipe

recipe = Recipe("Test", 10, "beginner")
print(recipe.display_recipe())

main_dish = MainDishRecipe("Main", 10, "beginner", cooking_time = 10)
main_dish.is_vegetarian = True
main_dish.is_vegan = True
print(main_dish.display_recipe())
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
