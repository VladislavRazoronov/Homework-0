import spoonacular
import json

def get_data(maxcal, mincal, ingredients=None):
    """
    Recieves 100 recipes in given colories range that contain
    complementary included ingredient, then writes down data into
    file and returns file name
    """
    api = spoonacular.API('738087f315ba454490f58e521168dcb7')
    if ingredients:
        info = api.search_recipes_complex('', number=100, maxCalories=maxcal,\
        minCalories=mincal, includeIngredients=ingredients, fillIngredients=True,\
        addRecipeNutrition=True, ignorePantry=True)
    else:
        info = api.search_recipes_complex('', number=100, maxCalories=maxcal,\
        minCalories=mincal, includeIngredients=ingredients, addRecipeNutrition=True,\
        ignorePantry=True)
    data = info.json()
    js = json.dumps(data, indent=2)
    with open(f'resources{maxcal}-{mincal}.txt', mode='w') as result:
        result.write(js)
    return f'resources{maxcal}-{mincal}.txt'

def parse_information(filepath):
    """
    Parses data in given file and returns a list with
    needed data
    """
    with open(filepath) as file:
        resource = json.load(file)['results']
    result = []
    for el in resource:
        temp = el['nutrition']['nutrients']
        nutrients = {}
        for nutrient in temp:
            if nutrient['title'] == 'Calories':
                nutrients['Calories'] = nutrient['amount']
            if nutrient['title'] == 'Fat':
                nutrients['Fat'] = nutrient['amount']
            if nutrient['title'] == 'Carbohydrates':
                nutrients['Carbohydrates'] = nutrient['amount']
            if nutrient['title'] == 'Protein':
                nutrients['Protein'] = nutrient['amount']
        ingredients = el['nutrition']['ingredients']
        ingred = []
        for ingredient in ingredients:
            temp = el['nutrients']
            ingr_nutrients = {}
            for nutrient in temp:
                if nutrient['title'] == 'Calories':
                    ingr_nutrients['Calories'] = nutrient['amount']
                elif nutrient['title'] == 'Fat':
                    ingr_nutrients['Fat'] = nutrient['amount']
                elif nutrient['title'] == 'Carbohydrates':
                    ingr_nutrients['Carbohydrates'] = nutrient['amount']
                elif nutrient['title'] == 'Protein':
                    ingr_nutrients['Protein'] = nutrient['amount']
            ingred.append((ingredient['name'], ingredient['amount'], \
            ingredient['unit'], ingr_nutrients))
        result.append((el['title'], nutrients, ingred, el['sourceUrl']))
    return result