class Food:
    """
    Class for representing food with calories
    and nutrients
    """
    def __init__(self, cal, carb, prot, fat):
        self.calories = cal
        self.carbohydrates = carb
        self.proteins = prot
        self.fat = fat

class Recipe(Food):
    """
    Class for representing recipes with calories, 
    nutrients, ingredients and link to its source
    """
    def __init__(self, cal, carb, prot, fat, ingred, link):
        super().__init__(cal, carb, prot, fat)
        self.ingredients = ingred
        self.link = link

class Ingredient(Food):
    """
    Class for representing ingredient with calories,
    nutrients and list of recipes it is used in
    """
    def __init__(self, cal, carb, prot, fat, recipes):
        super().__init__(cal, carb, prot, fat)
        self.recipes = recipes