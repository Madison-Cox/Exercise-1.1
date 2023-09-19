import pickle


def calc_difficulty(recipe):
    if recipe['Cooking_Time'] < 10 and len(recipe['Ingredients']) < 4:
        difficulty = 'Easy'

    elif recipe['Cooking_Time'] < 10 and len(recipe['Ingredients']) >= 4:
        difficulty = 'Medium'

    elif recipe['Cooking_Time'] >= 10 and len(recipe['Ingredients']) < 4:
        difficulty = 'Intermediate'

    elif recipe['Cooking_Time'] >= 10 and len(recipe['Ingredients']) >= 4:
        difficulty = 'Hard'
    return difficulty


def take_recipe():
    name = input('Enter the name of your recipe: ')
    cooking_time = int(
        input('Enter the cooking time for your recipe in minutes: '))
    ingredients = input('Enter the ingredients for your recipe: ')
    ingredients = ingredients.split()
    ingredients = [ingredient.lower() for ingredient in ingredients]
    recipe = {'Name': name, 'Cooking_Time': cooking_time,
              'Ingredients': ingredients}
    recipe['Difficulty'] = calc_difficulty(recipe)
    return recipe


recipes_list = []
all_ingredients = []

filename = input('Enter a filename with your recipes: ')

try:
    recipes_file = open(filename, 'rb')
    data = pickle.load(recipes_file)
except FileNotFoundError:
    print('File not found. Creating a new file.')
    data = {'recipes_list': [], 'all_ingredients': []}
except:
    print('Unexpected error. Creating a new file. ')
    data = {'recipes_list': [], 'all_ingredients': []}
else:
    recipes_file.close()
finally:
    recipes_list = data['recipes_list']
    all_ingredients = data['all_ingredients']

num = int(input('How many recipes would you like to enter? '))

for i in range(num):
    recipe = take_recipe()
    print(recipe)

    for ingredient in recipe['Ingredients']:
        if ingredient not in all_ingredients:
            all_ingredients.append(ingredient)

    recipes_list.append(recipe)

data = {'recipes_list': recipes_list, 'all_ingredients': all_ingredients}

new_file_name = input('Enter a name for your new file.')
with open(new_file_name, 'wb') as f:
    pickle.dump(data, f)