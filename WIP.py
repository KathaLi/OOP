## Create class MainDishRecipe
class MainDishRecipe:
    def __init__(self, name, prep_time, level, ingredients, text, cooking_time):
        # name of the recipe as string
        self.name = name
        # preparation time of the recipe in minutes as integer
        self.prep_time = prep_time
        # cooking level needed for the recipe with values ['beginner', 'advanced', 'expert']
        self.level = level
        # ingredients needed for the recipe as list of strings
        self.ingredients = ingredients
        # explanation of the recipe as string
        self.text = text
        # cooking time needed for the recipe in minutes as integer
        self.cooking_time = cooking_time
        # boolean to specify whether the recipe is suitable for meal prepping
        self.is_meal_prep = False
        # boolean to specify whether the recipe is suitable for vegetarian diet
        self.is_vegetarian = False
        # boolean to specify whether the recipe is suitable for vegan diet
        self.is_vegan = False
        # boolean to specify whether one needs an oven
        self.need_oven = False

    def display_recipe(self):
        print(f"{self.name} for {self.level} \n")
        print(f"Prep time:{self.prep_time} minutes \n")
        if self.is_meal_prep:
            print(f"Perfect for meal prep \n")
        if self.is_vegetarian and (self.is_vegan == False):
            print(f"Suitable for a vegetarian diet \n")
        if self.is_vegan:
            print(f"Suitable for a vegan diet \n")

