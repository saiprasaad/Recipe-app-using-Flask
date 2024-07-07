from flask import request, jsonify, abort
import requests
import os

apiKey = os.environ.get("RECIPE_API_KEY")

def fetch_recipe_from_spoonacular(query):
    response = requests.get(f"https://api.spoonacular.com/recipes/complexSearch?query={query}&apiKey={apiKey}")
    if(response.status_code != 200):
        abort(response.status_code, "Recipe details could not be fetched")
    return response.json()

def configure_app_routes(app):    
    @app.route("/")
    def test_recipe_app():
        return "Recipe app works fine"
    
    @app.route("/fetch-recipes", methods = ["GET"])
    def fetch_recipes():
        query = request.args.get("query")
        if not query:
            abort(400, description = "Query parameter is required")
        food_data_response = fetch_recipe_from_spoonacular(query)
        return food_data_response
    
    @app.errorhandler(400)
    @app.errorhandler(404)
    @app.errorhandler(500)
    def handle_errors(error):
        return jsonify({"error": str(error)}), error.code