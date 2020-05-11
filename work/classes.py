from abstract_class import AbstractFoodClass

class Recipe(AbstractFoodClass):
    """
    Class for representing recipes with calories, 
    nutrients, ingredients and link to its source
    """
    def __init__(self, name, cal, carb, prot, fat, ingred, link):
        super().__init__(name, cal, carb, prot, fat)
        self.ingredients = ingred
        self.link = link
    
    def __hash__(self):
        return ord(self.name) + ord(self.calories) + ord(self.link) 
    
    def add_ingredient(self, ingredient, value, units):
        self.ingredients[ingredient] = (value, units)
    
    def find_ingredient(self, ingredient):
        return self.ingredients[ingredient]

class Ingredient(AbstractFoodClass):
    """
    Class for representing ingredient with calories,
    nutrients and list of recipes it is used in
    """
    def __init__(self, name, cal, carb, prot, fat, recipes):
        super().__init__(name, cal, carb, prot, fat)
        self.recipes = set(recipes)
    
    def __hash__(self):
        return ord(self.name) + ord(self.calories)
    
    def add_recipe(self, recipe):
        self.recipes.add(recipe)
    
    def calculate_total_amount(self):
        total = 0.0
        for recipe in self.recipes:
            data = recipe.find_ingredient(self)
            total += data[0]
            unit = data[1]
        return (total, unit)