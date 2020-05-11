from abstract_class import AbstractFoodClass

if __name__ == "__main__":
    food1 = AbstractFoodClass('pasta', 135, 19, 3, 5)
    food2 = AbstractFoodClass('baked potato', 80, 13, 2, 3)
    print(food1.compare_values(food2, 'calories'))
    food1.set_name('pasta with butter')
    food1.set_calories(205)
    food1.set_fat(25)
    print(food1)
    print(food1 == food1)
    print(food2)
    print(food2 != food1)