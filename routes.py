from flask import request, jsonify, abort
from api_helper import fetch_recipe_from_spoonacular

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