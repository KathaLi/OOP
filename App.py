from IPython.terminal.shortcuts import reset_buffer
from data import ingredients_data, main_dish_data, dessert_data, cake_data


recipe_data = {"maindish_data": main_dish_data,
               "dessert_data": dessert_data,
               "cake_data": cake_data}


class App:
    def __init__(self, recipe_list):
        self.recipe_list = recipe_list

    def find_recipe(self):
        user_ingredient = input("Enter ingredient: ").lower()
        recipes = []
        recipe_index = 1
        for index, recipe in enumerate(self.recipe_list):
            for ingredient in recipe.ingredients:
                if ingredient.name == user_ingredient:
                    print(f"Recipe number {recipe_index}" )
                    recipe.display_recipe()
                    source = type(recipe).__name__.replace("Recipe", "").lower() + "_data"
                    recipes.append({"index":index, "source": source})
                    recipe_index += 1
                else:
                    pass
        return recipes
    def return_chosen_recipe(self, result_recipes):
        user_recipe_number = input("Enter recipe number: ")
        user_recipe = result_recipes[int(user_recipe_number)-1]
        chosen_type = recipe_data[user_recipe["source"]]
        recipe = chosen_type[user_recipe["index"]]
        print(recipe)
    def run(self):
        print("Welcome to the recipe finder!")
        print("I am here to put an end to wasting ingredients. Tell me what you have and I'll tell you what to cook.")
        result_recipes = self.find_recipe()
        print("Tell me which one you want to choose by telling me the recipe number.")
        self.return_chosen_recipe(result_recipes)
