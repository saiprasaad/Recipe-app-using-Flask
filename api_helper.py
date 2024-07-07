from flask import abort
import requests
import os

apiKey = os.environ.get("RECIPE_API_KEY")

def fetch_recipe_from_spoonacular(query):
    response = requests.get(f"https://api.spoonacular.com/recipes/complexSearch?query={query}&apiKey={apiKey}")
    if(response.status_code != 200):
        abort(response.status_code, "Recipe details could not be fetched")
    return response.json()
