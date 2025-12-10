from export import voice  
from export import pdf_print
import os
from dotenv import load_dotenv
load_dotenv() 

import argparse
import requests
import cowsay
import random
import sys
import re

API_KEY = os.getenv("API_KEY")
ENDPOINT_URL = f"https://api.spoonacular.com/recipes/complexSearch?apiKey={API_KEY}"
ENDPOINT_RECIPE_URL = f'https://api.spoonacular.com/recipes/recipeId/information?apiKey={API_KEY}'
WELLCOME = 'Welcome to 0Waste,the best way for cooking with what U have at home right now'

def set_args():
    parser = argparse.ArgumentParser(description="You can export a recipe to a pdf file or to an audio file")
    parser.add_argument("-e", help="Export recipe", type=str, default='audio', choices=['audio', 'pdf'])
    args = parser.parse_args()
    return args

def main():
    args = set_args()

    if args.e != 'audio' and args.e != 'pdf' and len(sys.argv) > 2:
        sys.exit('You need to choose only one option')

    cowsay.cow(WELLCOME)
    info = get_info()
    recepies = get_url_recipes_spoonacular(time=info['time'], ingredients=info['ingredients'])
    recipe_id= choose_random_recipe(recepies)
    recipe = get_recipe_from_spoonacular_id(recipe_id)

    title = f'Hello {info["user"]}, we are going to cook today {recipe['title']}'
    time = f'your dish will be ready in {recipe['readyInMinutes']} minutes, enjoy your meal'
    instructions = html_to_text(recipe['instructions'])

    if args.e == 'audio':

        voice.get_voice(title, time, instructions)
    else:
        picture = recipe['image']
        pdf_print.receipt(time=time, instructions=instructions, picture=picture, title=recipe['title'])

def html_to_text(html):
    pattern = r'<[^>]*>'
    return re.sub(pattern, '', html)

def choose_random_recipe (recepies):
    try:
        if recepies['results'] == []:
            sys.exit('No recipes found, try with other ingredients or more time for cooking')
        random_recipe_id = random.randint(0, len(recepies['results'])-1)
        return recepies['results'][random_recipe_id]['id']
    except TypeError:
        print('error finding an exact recipe')

def get_url_recipes_spoonacular(ingredients, time):
    try:
        params = {
            'includeIngredients': ','.join(ingredients),
            'instructionsRequired': 'true',
            'maxReadyTime': time,
            'ignorePantry': 'true',
            'number':2
        }

        response = requests.get(ENDPOINT_URL, params=params)
        response.raise_for_status()

        return response.json()

    except requests.exceptions.RequestException :
        sys.exit('service unavailable')


def get_recipe_from_spoonacular_id(recipeId):

    try:

        params = {
            'includeNutrition': 'true'
        }
        url =  ENDPOINT_RECIPE_URL.replace('recipeId', str(recipeId))

        response = requests.get(url, params=params)
        response.raise_for_status()
        response =  response.json()
        return response

    except requests.exceptions.RequestException :
        sys.exit('service unavailable')

def get_info ():
    max_ingredients = 5
    ingredients=[]
    try:
        user = input('what is your name: ').strip()
        time = int(input('How many minutes U have for cooking: ').strip())
    except:
        sys.exit('Time should be a number in minutes')


    print(f'Now tell us the ingredients U have right now for cooking, maximum {max_ingredients}')
    while True or len(ingredients) < max_ingredients:
        try:
            ingredient = input("Ingredient: ").strip()
            if ingredient == '':
                print('\n')
                break
            ingredients.append(ingredient)
            if len(ingredients) == max_ingredients:
                break
        except EOFError:
            print('\n')
            break
        except KeyboardInterrupt:
            print('\n')
            break
    if len(ingredients) == 0:
        sys.exit('U need to add at least one ingredient')
    if time < 5:
        sys.exit('Time should be at least 5 minutes,come back when you have more time')

    return {"ingredients":ingredients,"time":time,"user":user}

if __name__ == "__main__":
    main()
