from abstract_type import AbstractFood

class Recipe(AbstractFood):
    """
    Class for representing recipes with calories, 
    nutrients, ingredients and link to its source
    """
    def __init__(self, name, cal, carb, prot, fat, ingred, link):
        self._name = name
        self._calories = cal
        self._carbohydrates = carb
        self._proteins = prot
        self._fat = fat
        self._ingredients = ingred
        self._link = link
    
    def __hash__(self):
        return ord(self._name) + ord(self._calories) + ord(self._link) 
    
    def add_ingredient(self, ingredient, value, units):
        self._ingredients[ingredient] = (value, units)
    
    def find_ingredient(self, ingredient):
        if ingredient not in self._ingredients.keys():
            raise KeyError('This recipe do not contain this ingredient')
        return self._ingredients[ingredient]
    
    def __str__(self):
        st = ''
        for ingr in self._ingredients.keys():
            st += f'{ingr._name}: {self._ingredients[ingr][0]} {self._ingredients[ingr][1]}'
        return f"The recipe {self._name} has {self._calories} calories." +\
            f"\n And contains such ingredients:\n {st} \n And here is its link: {self._link}"
    
    

class Ingredient(AbstractFood):
    """
    Class for representing ingredient with calories,
    nutrients and list of recipes it is used in
    """
    def __init__(self, name, cal, carb, prot, fat, recipes):
        self._name = name
        self._calories = cal
        self._carbohydrates = carb
        self._proteins = prot
        self._fat = fat
        self._recipes = set(recipes)
    
    def __hash__(self):
        return ord(self._name) + ord(self._calories)
    
    def add_recipe(self, recipe):
        self._recipes.add(recipe)
    
    def calculate_total_amount(self):
        total = 0.0
        for recipe in self._recipes:
            data = recipe.find_ingredient(self)
            total += data[0]
            unit = data[1]
        return (total, unit)
    
    def __eq__(self, other):
        return self._name == other._name