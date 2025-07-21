# This script holds the needed data: recipes, ingredients.

## carbs, fat, sugar per 100g or piece, depending on ingredient
## values are exemplary only and were not verified
ingredients_data = {
    "broccoli": {"calories": 30, "carbs": 6, "fat": 0.3, "sugar": 1},
    "noodles": {"calories": 150, "carbs": 30, "fat": 1.2, "sugar": 1},
    "apple": {"calories": 52, "carbs": 14, "fat": 0.2, "sugar": 10},
    "oats": {"calories": 380, "carbs": 62, "fat": 7, "sugar": 1},
    "sugar": {"calories": 400, "carbs": 100, "fat": 0, "sugar": 100},
    "cinnamon": {"calories": 250, "carbs": 80, "fat": 1.2, "sugar": 2},
    "risotto rice": {"calories": 130, "carbs": 28, "fat": 0.4, "sugar": 0},
    "parmesan": {"calories": 400, "carbs": 4, "fat": 30, "sugar": 0},
    "tofu": {"calories": 76, "carbs": 1.9, "fat": 4.8, "sugar": 0.3},
    "tomato": {"calories": 18, "carbs": 3.9, "fat": 0.2, "sugar": 2.6},
    "lentils": {"calories": 116, "carbs": 20, "fat": 0.4, "sugar": 1.8},
    "olive oil": {"calories": 900, "carbs": 0, "fat": 100, "sugar": 0},
    "spinach": {"calories": 23, "carbs": 3.6, "fat": 0.4, "sugar": 0.4},
    "egg": {"calories": 72, "carbs": 0.6, "fat": 5.4, "sugar": 0},
    "milk": {"calories": 64, "carbs": 5, "fat": 3.6, "sugar": 5},
    "flour": {"calories": 364, "carbs": 76, "fat": 1, "sugar": 0.3},
    "butter": {"calories": 717, "carbs": 0.1, "fat": 81, "sugar": 0},
    "chocolate": {"calories": 546, "carbs": 61, "fat": 31, "sugar": 48},
    "vanilla sugar": {"calories": 400, "carbs": 100, "fat": 0, "sugar": 100},
    "baking powder": {"calories": 53, "carbs": 27, "fat": 0, "sugar": 0}
}
# prep_time, cooking_time in minutes
# amount in grams or piece depending on ingredient
main_dish_data = [
    {
        "name": "Broccoli Noodles",
        "prep_time": 10,
        "level": "beginner",
        "cooking_time": 10,
        "ingredients": [
            {"name": "broccoli", "amount": 200},
            {"name": "noodles", "amount": 100}
        ],
        "text": "Start by preparing some water for the noodles.",
        "is_meal_prep": True,
        "is_vegetarian": True
    },
    {
        "name": "Apple Crumble",
        "prep_time": 10,
        "level": "beginner",
        "cooking_time": 15,
        "ingredients": [
            {"name": "apple", "amount": 150},
            {"name": "oats", "amount": 50},
            {"name": "sugar", "amount": 20},
            {"name": "cinnamon", "amount": 5}
        ],
        "text": "Start by cutting the apples.",
        "is_vegetarian": True
    },
    {
        "name": "Broccoli Risotto",
        "prep_time": 10,
        "level": "beginner",
        "cooking_time": 20,
        "ingredients": [
            {"name": "broccoli", "amount": 150},
            {"name": "risotto rice", "amount": 100},
            {"name": "parmesan", "amount": 30}
        ],
        "text": "Start by cutting the broccoli.",
        "is_vegetarian": True
    },
    {
        "name": "Vegan Lentil Bowl",
        "prep_time": 15,
        "level": "beginner",
        "cooking_time": 20,
        "ingredients": [
            {"name": "lentils", "amount": 100},
            {"name": "spinach", "amount": 50},
            {"name": "tomato", "amount": 100},
            {"name": "olive oil", "amount": 10}
        ],
        "text": "Boil lentils and sauté vegetables.",
        "is_vegetarian": True,
        "is_vegan": True
    },
    {
        "name": "Tofu Stir Fry",
        "prep_time": 10,
        "level": "advanced",
        "cooking_time": 15,
        "ingredients": [
            {"name": "tofu", "amount": 150},
            {"name": "broccoli", "amount": 100},
            {"name": "olive oil", "amount": 10}
        ],
        "text": "Fry the tofu until crispy, then add broccoli.",
        "is_vegetarian": True,
        "is_vegan": True
    },
    {
        "name": "Spinach Omelette",
        "prep_time": 5,
        "level": "beginner",
        "cooking_time": 7,
        "ingredients": [
            {"name": "egg", "amount": 2},
            {"name": "spinach", "amount": 50},
            {"name": "olive oil", "amount": 5}
        ],
        "text": "Beat eggs, mix with spinach, and cook in a pan.",
        "is_vegetarian": True,
        "is_vegan": False
    }
]

dessert_data = [
    {
        "name": "Vanilla Pudding",
        "prep_time": 10,
        "level": "beginner",
        "cooling_time": 30,
        "ingredients": [
            {"name": "milk", "amount": 250},
            {"name": "sugar", "amount": 20},
            {"name": "vanilla sugar", "amount": 10}
        ],
        "text": "Heat milk and stir in vanilla sugar until smooth."
    },
    {
        "name": "Chocolate Cream",
        "prep_time": 15,
        "level": "advanced",
        "cooling_time": 40,
        "ingredients": [
            {"name": "milk", "amount": 200},
            {"name": "chocolate", "amount": 50},
            {"name": "sugar", "amount": 15}
        ],
        "text": "Melt chocolate in warm milk and chill the cream."
    }
]

cake_data = [
    {
        "name": "Apple Cake",
        "prep_time": 20,
        "level": "beginner",
        "cooling_time": 30,
        "baking_time": 40,
        "ingredients": [
            {"name": "apple", "amount": 150},
            {"name": "flour", "amount": 200},
            {"name": "butter", "amount": 100},
            {"name": "sugar", "amount": 100},
            {"name": "egg", "amount": 2},
            {"name": "baking powder", "amount": 5}
        ],
        "text": "Mix all ingredients, fill into baking dish, and bake."
    },
    {
        "name": "Chocolate Cake",
        "prep_time": 30,
        "level": "advanced",
        "cooling_time": 40,
        "baking_time": 45,
        "ingredients": [
            {"name": "flour", "amount": 200},
            {"name": "chocolate", "amount": 100},
            {"name": "butter", "amount": 100},
            {"name": "sugar", "amount": 100},
            {"name": "egg", "amount": 3},
            {"name": "baking powder", "amount": 5}
        ],
        "text": "Mix chocolate with butter and other ingredients. Bake until ready."
    }
]

