from data import get_data, parse_information
from classes import Recipe, Ingredient

def find_ingredients():
    while True:
        try:
            min_calories, max_calories = map(int, input('Please enter minimum'+\
            ' and maximum calories separated by space: ').split())
        except:
            print('Invalid format, please enter again')
    ingred = input('Please enter prefered ingredients, leave blank to'+\
    'search without selected ingredient')
    if ingred == '':
        ingred = None
    file = f'resources{max_calories}-{min_calories}.txt'
    try:
        recipes = parse_information(file)
    except:
        file = get_data(max_calories, min_calories, ingred)
        recipes = parse_information(file)
    recipebook = []
    for el in recipes:
        ingredients = {}
        for ingr in el[2]:
            ingredients[Ingredient(ingr[0],ingr[3]['Calories'],ingr[3]\
                ['Carbohydrates'],ingr[3]['Protein'],ingr[3]['Fat'],set())]\
                = (ingr[1], ingr[2])
        recipebook.append(Recipe(el[0],el[1]['Calories'],el[1]['Carbohydrates'],el[1]\
            ['Protein'],el[1]['Fat'],ingredients,el[3]))
        for ingr in ingredients:
            ingr[0].add_recipe(recipebook[-1])


if __name__ == "__main__":
    find_ingredients()