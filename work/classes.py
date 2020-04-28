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


class Recipe(Food):
    """
    Class for representing recipes with calories, 
    nutrients, ingredients and link to its source
    """
    def __init__(self, name, cal, carb, prot, fat, ingred, link):
        super().__init__(name, cal, carb, prot, fat)
        self.ingredients = set(ingred)
        self.link = link
    
    def __hash__(self):
        return ord(self.name) + ord(self.calories) + ord(self.link) 
    
    def add_ingredient(self, ingredient):
        self.ingredients.add(ingredient)


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