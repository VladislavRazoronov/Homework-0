import urllib.request as URL
import spoonacular
import json

if __name__ == "__main__":
    device = spoonacular.API('738087f315ba454490f58e521168dcb7')
    res = device.search_recipes_complex('pasta', number=10, fillIngredients=True, addRecipeNutrition=True, ignorePantry=True)
    data = res.json()
    js = json.dumps(data, indent=2)
    with open('result.txt', mode='w') as result:
        result.write(js)