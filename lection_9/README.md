# 0 Waste
## Author: 
    Name: Jeff
    GitHub: https://github.com/jepalen
    edX UserName : jepalen
    City/Country: Vienna - Austria
    Date: 08/12/2025

 ### Description: 
 This is a small CS50 project that uses Spoonacular API (https://spoonacular.com/food-api) basic account to find recipes based on the ingredients the user has at home and the time they have for cooking (By now it  requires extra ingredients for making the recipe). The user can choose via arguments to export the recipe to a pdf file or to an audio file. The project is a command line application that uses argparse to parse the arguments and later on ask the user for the ingredients and the time they have for cooking. The project is also using cowsay to welcome the user and requests library to get the data from the API.
 
 The main file is project.py, here is where the main function is located, where the arguments are parsed and where we ask the user for the ingredients and the time they have for cooking.

 Also there are two other files inside the export folder:
    - voice.py: here is where is located the functions that convert all the recipe information to an audio file. It works with pyttsx3 library. In the very same way it was shown in the last lection.
    - pdf_print.py: here is where is located the functions that convert all the recipe information to a pdf file. It works with fpdf library and works using classes. Here are defined the functions that create the pdf file and the functions that add the information to the pdf file.

 ### Important: 
 - You need a Spoonacular API key to run the project and locate it in the .env file in the root directory.
 - The project is using a basic account of Spoonacular API, so the number of requests is limited to 50 per day.

 ### How to run the project locally:
for testing the project you can use the following command:
    ```python project.py -e pdf or python project.py -e audio or directly python project.py```

for unit tests you can use the following command:
    ```pytest test_project.py```