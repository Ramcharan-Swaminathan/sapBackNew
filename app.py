from flask import Flask, jsonify
from dotenv import load_dotenv
import os

# Import blueprints
from api.dashboard.routes import dashboard_bp
from api.foodsafety.routes import foodsafety_bp
from api.forecast.routes import forecast_bp
from api.inventory.routes import inventory_bp
from api.profitloss.routes import profitloss_bp
from api.about.routes import about_bp
from api.foodfall.routes import foodfall_bp
from utils.Database import MongoDB

from flask_jwt_extended import JWTManager

def create_app():

    load_dotenv("/Users/balamurugan/Documents/GitHub/sapBackNew/utils")
    app = Flask(__name__)

    app.config['DataBase'] = MongoDB(str(os.getenv("MongoDBAPI")))
    
    app.config['JWT_SECRET_KEY'] = str(os.getenv("JWT_SECRET_KEY"))
    app.config['JWT_TOKEN_LOCATION'] = ['headers']
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = False
    app.config['JWT_HEADER_NAME'] = 'Authorization'
    app.config['JWT_HEADER_TYPE'] = 'Bearer'

    jwt = JWTManager(app)




    # Register blueprints with appropriate URL prefixes
    app.register_blueprint(dashboard_bp, url_prefix='/dashboard')
    app.register_blueprint(foodsafety_bp, url_prefix='/foodsafety')
    app.register_blueprint(forecast_bp, url_prefix='/forecast')
    app.register_blueprint(inventory_bp, url_prefix='/inventory')
    app.register_blueprint(profitloss_bp, url_prefix='/profitloss')
    app.register_blueprint(about_bp, url_prefix='/about')
    app.register_blueprint(foodfall_bp, url_prefix='/foodfall')
    
    # Root route
    @app.route('/')
    def index():
        return jsonify({
            "name": "Food Management API",
            "version": "1.0.0",
            "description": "API for food management system with multiple modules",
            "endpoints": {
                "dashboard": "/dashboard",
                "foodsafety": "/foodsafety",
                "forecast": "/forecast",
                "inventory": "/inventory",
                "profitloss": "/profitloss",
                "about": "/about",
                "foodfall": "/foodfall"
            }
        })
    
    # Error handlers
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({"success": False, "error": "Resource not found"}), 404
    
    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({"success": False, "error": "Bad request"}), 400
    
    @app.errorhandler(500)
    def server_error(error):
        return jsonify({"success": False, "error": "Internal server error"}), 500
    
    return app



# Create the application instance
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
