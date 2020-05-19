import spoonacular
import json

def get_data(maxcal, mincal, ingredients=None):
    """
    Recieves 50 recipes in given colories range that contain
    complementary included ingredient, then writes down data into
    file and returns file name
    """
    api = spoonacular.API('738087f315ba454490f58e521168dcb7')
    if ingredients:
        info = api.search_recipes_complex('', number=20, maxCalories=maxcal,\
        minCalories=mincal, includeIngredients=ingredients, fillIngredients=True,\
        addRecipeNutrition=True, ignorePantry=True)
    else:
        info = api.search_recipes_complex('', number=20, maxCalories=maxcal,\
        minCalories=mincal, fillIngredients=True, addRecipeNutrition=True,\
        ignorePantry=True)
    data = info.json()
    js = json.dumps(data, indent=2)
    with open(f'work/resources{maxcal}-{mincal}.txt', mode='w') as result:
        result.write(js)
    return f'work/resources{maxcal}-{mincal}.txt'

def parse_information(filepath):
    """
    Parses data in given file and returns a list with
    needed data
    """
    with open(filepath) as file:
        resource = json.load(file)['results']
    result = []
    for el in resource:
        temp = el['nutrition']
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
        if 'Fat' not in nutrients.keys():
            nutrients['Fat'] = None
        if 'Carbohydrates' not in nutrients.keys():
            nutrients['Carbohydrates'] = None
        if 'Protein' not in nutrients.keys():
            nutrients['Protein'] = None
        ingredients = el['extendedIngredients']
        ingred = []
        for ingredient in ingredients:
            ingr_nutrients = {}
            ingr_nutrients['Calories'] = None
            ingr_nutrients['Fat'] = None
            ingr_nutrients['Carbohydrates'] = None
            ingr_nutrients['Protein'] = None
            ingred.append((ingredient['name'], ingredient['amount'], \
            ingredient['unit'], ingr_nutrients))
        result.append((el['title'], nutrients, ingred, el['sourceUrl']))
    return result
