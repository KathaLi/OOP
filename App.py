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
        for recipe in self.recipe_list:
            for ingredient in recipe.ingredients:
                if ingredient.name == user_ingredient:
                    print(f"Recipe number {recipe_index}" )
                    recipe.display_recipe()
                    source = type(recipe).__name__.replace("Recipe", "").lower() + "_data"
                    # Store the recipe's index in its own type list
                    type_index = 0
                    for i, r in enumerate(recipe_data[source]):
                        if r["name"] == recipe.name:
                            type_index = i
                            break
                    recipes.append({"index": type_index, "source": source})
                    recipe_index += 1
                else:
                    pass
        return recipes
    def return_chosen_recipe(self, result_recipes):
        while True:
            try:
                user_recipe_number = int(input("Enter recipe number: "))
                if 1 <= user_recipe_number <= len(result_recipes):
                    user_recipe = result_recipes[user_recipe_number - 1]  # Convert to 0-based index
                    chosen_type = recipe_data[user_recipe["source"]]
                    recipe = chosen_type[user_recipe["index"]]
                    print('Here is your recipe')
                    print("Ingredients:")
                    for ingredient in recipe['ingredients']:
                        print(f"- {ingredient['amount']} of {ingredient['name']}")
                    print("\nInstructions:")
                    print(recipe['text'])
                    break
                else:
                    print(f"Please enter a number between 1 and {len(result_recipes)}")
            except ValueError:
                print("Please enter a valid number")
    def run(self):
        while True:
            print("*************************")
            print("Welcome to the recipe finder!")
            print("I am here to put an end to wasting ingredients. Tell me what you have and I'll tell you what to cook.")
            result_recipes = self.find_recipe()
            if result_recipes:
                print("Tell me which one you want to choose by telling me the recipe number.")
                self.return_chosen_recipe(result_recipes)
            else:
                print("No recipe found for ingredient")
