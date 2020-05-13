class AbstractFood:
    """
    Abstract type for food
    """
    
    def __getitem__(self, value_name):
        if f'_{value_name}' in self.__dir__():
            return self.__getattribute__(f'_{value_name}')
        else:
            raise KeyError('Argument does not exist')

    def __setitem__(self, value_name, value):
        if f'_{value_name}' in self.__dir__():
            self.__setattr__(f'_{value_name}', value)
        else:
            raise KeyError('Argument does not exist')

    def compare_values(self, other, value):
        """
        Compares given values of two food items
        """
        if value in self.__dir__() and value in other.__dir__():
            return float(self.__getattribute__(value)) > float(other.__getattribute__(value))
        else:
            return "Can't compare values"

    def __eq__(self, other):
        """
        Checks if two food items are the same
        """
        if self is other:
            return True
        if type(self) == type(other):
            return self._name == other._name and self._calories == other._calories and \
                self._carbohydrates == other._carbohydrates and self._fat == other._fat\
                and self._proteins == other._proteins
    
    def __str__(self):
        """
        Returns string representation of food
        """
        return f'{self._name} has {self._calories} calories, {self._carbohydrates}' +\
        f'g. carbohydrates, {self._fat}g. of fat and {self._proteins}g. of proteins'

