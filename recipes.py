import random


def display_header_footer():
    print("*" * 30 + "\n")

class IngredientItem:
    def __init__(self, name, amount, calories, carbs, fat, sugar):
        self.name = name
        self.amount = amount
        self.calories = calories
        self.carbs = carbs
        self.fat =fat
        self.sugar = sugar




### This script creates the parent, abstract class recipe

## Create class Recipe
class Recipe:
    def __init__(self, name, prep_time, level, ingredients, text, is_meal_prep = False):
        # name of the recipe as string
        self.name = name
        # preparation time of the recipe in minutes as integers
        self.prep_time = prep_time
        # cooking level needed for the recipe with values ['beginner', 'advanced', 'expert']
        self.level = level
        # ingredients needed for the recipe as list of strings
        self.ingredients = [IngredientItem(IN['name'], IN['amount'], IN['calories'], IN['carbs'], IN['fat'], IN['sugar']) for IN in ingredients]
        # explanation of the recipe as string
        self.text = text
        # boolean to specify whether the recipe is suitable for optional attribute meal prepping
        self.is_meal_prep = is_meal_prep

    def display_recipe(self):
        # method displays display_body with header and footer
        display_header_footer()
        self.display_body()
        display_header_footer()

    def display_body(self):
        # method displays all relevant information for recipe selection
        print(f"{self.name} for {self.level} \n")
        print(f"Prep time:{self.prep_time} minutes \n")
        if self.is_meal_prep:
            print(f"Perfect for meal prep \n")

    def calculate_calories(self):
        # method calculates the total calories of the recipe with used ingredients
        calories = 0
        for ingredient in self.ingredients:
            calories += ingredient.calories
        return calories
    def calculate_total_time(self):
        # method calculates the total time needed for the recipe
        return self.prep_time
    def calculate_rating(self):
        # method calculates the ratings given vy other users
        return random.randint(50,100)

# Create child class MainDishRecipe
class MainDishRecipe(Recipe):
    def __init__(self, name, prep_time, level,cooking_time, ingredients, text, is_vegetarian = False, is_vegan = False,
                 need_oven = False):
        # initialize parent class
        Recipe.__init__(self, name = name, prep_time = prep_time, level = level, ingredients = ingredients, text = text,
                        is_meal_prep = False)
        # cooking_time of the recipe in minutes as integers
        self.cooking_time = cooking_time
        # boolean for optional attribute to specify whether suitable for vegetarian diet
        self.is_vegetarian = is_vegetarian
        # boolean for optional attribute to specify whether suitable for vegan diet
        self.is_vegan = is_vegan
        # boolean for optional attribute to specify whether oven is needed
        self.need_oven = need_oven
    def display_body(self):
        # call parent method
        Recipe.display_body(self)
        # add further information
        print(f"Cooking time:{self.cooking_time} minutes \n")
        if self.is_meal_prep:
            print(f"Perfect for meal prep \n")
        if self.is_vegetarian and (self.is_vegan == False):
            print(f"Suitable for a vegetarian diet \n")
        elif self.is_vegan:
            print(f"Suitable for a vegan diet \n")
    def calculate_carbs(self):
        calories = 0
        for ingredient in self.ingredients:
            calories += ingredient.calories
        return calories
    def calculate_total_time(self):
        return self.prep_time + self.cooking_time

class DessertRecipe(Recipe):
    def __init__(self, name, prep_time, level, ingredients, text, cooling_time):
        Recipe.__init__(self, name = name, prep_time = prep_time, level = level, ingredients=ingredients, text = text, is_meal_prep = False)
        self.cooling_time = cooling_time
        self.contains_nuts = False
    def display_recipe(self):
        print(f"{self.name} for {self.level} \n")
        print(f"Prep time:{self.prep_time} minutes \n")
        if self.is_meal_prep:
            print(f"Perfect for meal prep \n")
        if not self.contains_nuts:
            print(f"Suitable for a nut allergies \n")
    def calculate_fat(self):
        fat = 0
        for ingredient in self.ingredients:
            fat += ingredient.sugar
        return fat
    def calculate_sugar(self):
        sugar = 0
        for ingredient in self.ingredients:
            sugar += ingredient.sugar
            return sugar
    def calculate_total_time(self):
        return self.prep_time +self.cooling_time

class CakeRecipe(DessertRecipe):
    def __init__(self, name, prep_time, level,cooling_time, baking_time):
        DessertRecipe.__init__(self, name = name, prep_time = prep_time, level = level, cooling_time = cooling_time)
        self.baking_time = baking_time
    def calculate_total_time(self):
        return self.prep_time + self.cooling_time + self.baking_time
    def display_recipe(self):
        print(f"{self.name} for {self.level} \n")
        print(f"Prep time:{self.prep_time} minutes \n")
        if self.is_meal_prep:
            print(f"Perfect for meal prep \n")
        if not self.contains_nuts:
            print(f"Suitable for a nut allergies \n")





