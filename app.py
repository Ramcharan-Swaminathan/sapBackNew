from flask import Flask, jsonify

# Import blueprints
from dashboard.routes import dashboard_bp
from foodsafety.routes import foodsafety_bp
from forecast.routes import forecast_bp
from inventory.routes import inventory_bp
from profitloss.routes import profitloss_bp
from about.routes import about_bp
from foodfall.routes import foodfall_bp

def create_app():
    app = Flask(__name__)
    
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
