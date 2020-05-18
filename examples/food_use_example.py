from abstract_type import AbstractFood

class Burger(AbstractFood):
    def __init__(self, name, cal, carb, fat, prot):
        self._name = name
        self._calories = cal
        self._carbohydrates = carb
        self._fat = fat
        self._proteins = prot

if __name__ == "__main__":
    b1 = Burger('Cheeseburger', 650, 80, 120, 90)
    print(b1['name'])
    b1['fat'] = 110
    print(b1['fat'])