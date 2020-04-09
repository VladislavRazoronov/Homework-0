import json
def parse_file(filename):
    """
    Parse given file as json and extract special
    data
    """
    result = []
    with open(filename) as file:
        data = json.load(file)['results']
    for el in data:
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
        result.append((el['title'], nutrients, ingredients))
    return result

if __name__ == "__main__":
    print(parse_file('result.txt'))

