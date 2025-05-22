from flask import Blueprint, jsonify

# Create the blueprint
dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/stats', methods=['GET'])
def get_stats():
    """Get dashboard statistics"""
    # Dummy response
    response = {
        "success": True,
        "data": {
            "total_inventory": 1250,
            "low_stock_items": 15,
            "revenue_this_month": 45000,
            "expenses_this_month": 32000,
            "profit_this_month": 13000,
            "food_wastage_percentage": 4.2,
            "upcoming_inspections": 2
        }
    }
    return jsonify(response)
