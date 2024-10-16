import os


# Let's read the file Recipes.txt
path = os.path.join(os.getcwd(), 'Recipes.txt')
with open(path) as cook_file:
    cook_book = {} # Creating an empty dictionary
    for string in cook_file:
        dish = string.strip() # Select the name of the dish from the file
        ingredients_count = int(cook_file.readline().strip()) # Select the number of ingredients for the dish from the file
        dish_dict = [] # Creating an empty list for dictionaries with cookbook dishes
        for item in range(ingredients_count):
            # Select the ingredients from the file using the separator '|'
            ingredient_name, quantity, measure = cook_file.readline().strip().split('|')
            # Adding dictionaries with ingredients to the list
            dish_dict.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
        cook_book[dish] = dish_dict # Add dishes and their ingredients to the cookbook
        cook_file.readline() # Skip the empty line


# Creating a function to get a shopping list based on the ordered dishes and the number of people
def get_shop_list_by_dishes(dishes, person_count):
    groсery_dict = {} # Creating an empty dictionary to store the shopping list
    for dish in dishes:
        for ingredient in cook_book[dish]: # Choosing ingredients for dishes from the cookbook
            # Add ingredients, increasing their number by the number of people
            ingredient_list = dict([(ingredient['ingredient_name'],
                                {'quantity': int(ingredient['quantity']) * person_count,
                                'measure': ingredient['measure']})])

            
            # Check the ordered dish for repetition, if the dish is already on the list, then increase the number
            # Otherwise, we add the ingredient to the shopping list
            if groсery_dict.get(ingredient['ingredient_name']) == 'None':
                _merger = (int(groсery_dict[ingredient['ingredient_name']]['quantity']) +
                int(ingredient_list[ingredient['ingredient_name']]['quantity']))
                groсery_dict[ingredient['ingredient_name']]['quantity'] = _merger
            else:
                groсery_dict.update(ingredient_list)
    return groсery_dict

print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', 'Фахитос', 'Омлет', 'Запеченный картофель'], 5))