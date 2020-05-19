from data import get_data, parse_information
from classes import Recipe, Ingredient
import os

def main():
    recipes = find_recipes()
    top_ingr = find_most_used(recipes)
    print_results(top_ingr)

def find_recipes():
    """
    Gets data about food from API
    """
    while True:
        try:
            min_calories, max_calories = map(int, input('Please enter minimum'+\
            ' and maximum calories separated by space: ').split())
            break
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
    return recipebook

def find_max_dict_value(dictionary):
    """
    Finds max value item in dictionary and removes it
    """
    biggest = dictionary.keys()[0]
    for key in dictionary.keys()[1:]:
        if dictionary[key] > dictionary[biggest]:
            biggest = key
    res = (biggest, dictionary[biggest])
    dictionary.pop(biggest)
    return res

def find_most_used(recipe_list):
    """
    Finds the most used ingredient
    """
    ingredient_amounts = {}
    for recipe in recipe_list:
        for ingr in recipe._ingredients.keys():
            if ingr not in ingredient_amounts.keys():
                ingredient_amounts[ingr] = (ingr.calculate_total_amount(), ingr._recipes)
            else:
                ingredient_amounts[ingr][0] += ingr.calculate_total_amount()
                ingredient_amounts[ingr][1].update(ingr._recipes)
    while True:
        try:
            count = int(input('Please insert size of top list'))
            break
        except:
            print('Variable must be integer')
    results = []
    for _ in range(count):
        results.append(find_max_dict_value(ingredient_amounts))
    return results

def print_results(results):
    print('№        Name        Value')
    for i in range(len(results)):
        print(f'{i+1}       {results[i][0]}     {results[i][1][0]}')
        if not os.path.exists(os.path.dirname(f'recipes/{results[i][0]}.txt')):
            try:
                os.makedirs(os.path.dirname(f'recipes/{results[i][0]}.txt'))
            except:
                pass
        with open(f'recipes/{results[i][0]}.txt', mode='w') as file:
            for rec in results[i][1][1]:
                file.write(rec)


if __name__ == "__main__":
    main()