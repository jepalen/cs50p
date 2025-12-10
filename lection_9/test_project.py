import pytest
import requests_mock
from project import get_info, get_url_recipes_spoonacular, get_recipe_from_spoonacular_id, choose_random_recipe,html_to_text

API_KEY = 'MY_API_KEY'
RECIPE_ID_MOCK = 660306
ENDPOINT_SEARCH_URL = f"https://api.spoonacular.com/recipes/complexSearch"
RECIPE_INFO_URL = f'https://api.spoonacular.com/recipes/{RECIPE_ID_MOCK}/information'


RECIPES_TEST ={"results":[
    {"id":660306,"title":"Slow Cooker: Pork and Garbanzo Beans","image":"https://img.spoonacular.com/recipes/660306-312x231.jpg","imageType":"jpg"},
    {"id":715421,"title":"Cheesy Chicken Enchilada Quinoa Casserole","image":"https://img.spoonacular.com/recipes/715421-312x231.jpg","imageType":"jpg"},
    ],
    "offset":0,
    "number":2,
    "totalResults":1090
}

RECIPE_INFO_TEST ={'instructions':'<ol><li>In slow cooker layer in this order: pork, then garbanzo beans, onion, pour water over all. Mix spices together and sprinkle over pork and beans. Cover. Set on low and cook for approximately 6 hours. The beans should be tender and creamy. The pork should fall very easily from the bone. The pork can be either shredded for cubed for your preference. *3</li><li>Serving Suggestion: Scoop about 1 cup of beans with broth into a soup bowl. Top with shredded pork. Add 1/4 of an avocado sliced, top with chopped fresh cilantro.</li><li>NOTES:</li><li>*1 The beans do not need to be soaked before adding to the slow cooker. They will be perfectly soft and creamy without pre-soaking.</li><li>*2 Substitute the water for: 2 cups water and 1 bottle of good quality dark beer like Negra Modelo. You can also substitute the water for chicken stock or pork stock. Each of these substitutions will add an extra dimension of flavor.</li><li>*3 If you want to shred the pork, it is easiest to do when the pork is hot. Use two forks to pull the pork apart and shred. If you want to slice the pork (like for sandwiches) it is best to do when the pork is cold. Let the pork rest in the refrigerator for several hours or over night. Slice with a serrated knife or a very sharp chef knife.</li></ol>',
    "image":"https://img.spoonacular.com/recipes/660306-312x231.jpg",
    "id":660306,
    "vegetarian":"true",
    "vegan":"true",
    "glutenFree":"true",
    "dairyFree":"true",
    "veryHealthy":"true",
    "cheap":"true",
    "title":"Slow Cooker: Pork and Garbanzo Beans",
    "readyInMinutes":45,
    "nutrition":{
        "calories":120,
        "protein":10,
        "carbohydrates":10,
        "fat":10
    }
}

def test_get_url_recipes_spoonacular():
    with requests_mock.Mocker() as m:
        m.get(ENDPOINT_SEARCH_URL, json=RECIPES_TEST, status_code=200)
        assert get_url_recipes_spoonacular([], 60) == RECIPES_TEST

def test_get_url_recipes_spoonacular_bad_answer():
    with requests_mock.Mocker() as m:
        m.get(ENDPOINT_SEARCH_URL,  status_code=404)
        with pytest.raises(SystemExit):
            get_url_recipes_spoonacular([], 60)

def test_get_url_recipes_spoonacular_bad_values():
    with requests_mock.Mocker() as m:
        m.get(ENDPOINT_SEARCH_URL, text='This is not JSON', status_code=200) 
        with pytest.raises(SystemExit):
            get_url_recipes_spoonacular([], 60)

def test_get_recipe_from_spoonacular_id():
    with requests_mock.Mocker() as m:
        m.get(RECIPE_INFO_URL, json=RECIPE_INFO_TEST, status_code=200,)
        assert get_recipe_from_spoonacular_id(RECIPE_ID_MOCK) == RECIPE_INFO_TEST

def test_get_recipe_from_spoonacular_id_bad_answer():
    with requests_mock.Mocker() as m:
        m.get(RECIPE_INFO_URL,  status_code=404)
        with pytest.raises(SystemExit):
            get_recipe_from_spoonacular_id(RECIPE_ID_MOCK)

def test_get_recipe_from_spoonacular_id_bad_values():
    with requests_mock.Mocker() as m:
        m.get(RECIPE_INFO_URL, text='error', status_code=200) 
        with pytest.raises(SystemExit):
            get_recipe_from_spoonacular_id(RECIPE_ID_MOCK)

def test_html_to_text():
    assert html_to_text('<html><body><div><p>Test recipe</p></div></body></html>') == 'Test recipe'

def test_choose_random_recipe():
    assert choose_random_recipe(RECIPES_TEST) == 660306 or 715421

def test_choose_random_recipe_no_recepies():
    with pytest.raises(SystemExit):
        choose_random_recipe({"results": []})

def test_choose_random_recipe_no_recepies():
    with pytest.raises(TypeError):
        choose_random_recipe()


    




