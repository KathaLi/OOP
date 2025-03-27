### This script creates the parent, abstract class recipe
class Recipe:
    def __init__(self, name, prep_time, level, is_meal_prep = False):
        self.name = name
        #prep_time in min
        self.prep_time = prep_time
        self.is_meal_prep = False
        self.level = level
        #self.ingredients = ingredients
    def display_recipe(self):
        print(f"{self.name} for {self.level} \n")
        print(f"{self.prep_time} minutes \n")
        if self.is_meal_prep:
            print(f"{self.is_meal_prep} \n")
    def calculate_calories(self):
        calories = 50
        return calories
    def calculate_total_time(self):
        total_time = self.prep_time
    def calculate_rating(self):
        rating = 10

recipe = Recipe("Test", 10, "beginner")
print(recipe.display_recipe())