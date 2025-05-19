


class App:
    def __init__(self, recipe_list):
        self.recipe_list = recipe_list

    def find_recipe(self):
        user_ingredient = input("Enter ingredient: ")
        recipes = []
        for recipe in self.recipe_list:
            for ingredient in recipe.ingredients:
                if ingredient.name == 'broccoli':
                    recipes.append(recipe.display_recipe())
                else:
                    pass
        return recipes
    def run(self):
        print("Welcome to the recipe finder!")
        print("I am here to put an end to wasting ingredients. Tell me what you have and I'll tell you what to cook.")
        result_recipes = self.find_recipe()
        print(result_recipes)