class AbstractFoodClass:
    """
    Abstract class for representing food with calories
    and nutrients
    AbstractFoodClass(name, cal, carb, prot, fat)
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
    
    def compare_values(self, other, value):
        """
        Compares given values of two food items
        """
        if value in self.__dir__() and value in other.__dir__():
            return float(self.__getattribute__(value)) > float(other.__getattribute__(value))
        else:
            return "Can't compare values"

    def __eq__(self, other):
        if self is other:
            return True
        if type(self) == type(other):
            return self.name == other.name and self.calories == other.calories and \
                self.carbohydrates == other.carbohydrates and self.fat == other.fat\
                and self.proteins == other.proteins
    
    def __str__(self):
        return f'{self.name} has {self.calories} calories, {self.carbohydrates}' +\
        f'g. carbohydrates, {self.fat}g. of fat and {self.proteins}g. of proteins'
