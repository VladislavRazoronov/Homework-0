class Food:
    """
    Class for representing food with calories
    and nutrients
    """
    def __init__(self, name ,cal, carb, prot, fat):
        self.name = name
        self.calories = cal
        self.carbohydrates = carb
        self.proteins = prot
        self.fat = fat

    def set_name(self, name):
        """
        Set food name
        """
        self.name = name

    def set_calories(self, calories):
        """
        Set food calories to given number
        """
        self.calories = calories
    
    def set_carbohydrates(self, carbohydrates):
        """
        Set food carbohydrates to given number
        """
        self.carbohydrates = carbohydrates
    
    def set_proteins(self, proteins):
        """
        Set food proteins to given number
        """
        self.proteins = proteins
    
    def set_fat(self, fat):
        """
        Set food fat to given number
        """
        self.fat = fat
    
    def __eq__(self, other):
        return self.name == other.name and self.calories == other.calories
    
    def __str__(self):
        return f'{self.name} has {self.calories} calories, {self.carbohydrates}' +\
        f'g. carbohydrates, {self.fat}g. of fat and {self.proteins}g. of proteins'


class Recipe(Food):
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

class Ingredient(Food):
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