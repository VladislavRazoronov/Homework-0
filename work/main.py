from data import get_data, parse_information

def find_ingredients():
    while True:
        try:
            min_calories, max_calories = map(int, input('Please enter minimum'+\
            ' and maximum calories separated by space: ').split())
        except:
            print('Invalid format, please enter again')
    ingred = imput('Please enter prefered ingredients, leave blank to'+\
    'search without selected ingredient')
    if ingred = '':
        ingred = None
    file = f'resources{max_calories}-{min_calories}.txt'
    try:
        recipes = parse_information(file)
    except:
        file = get_data(max_calories, min_calories, ingred)
        recipes = parse_information(file)

if __name__ == "__main__":
    find_ingredients()