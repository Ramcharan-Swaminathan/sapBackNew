from flask import Blueprint, jsonify, request

# Create the blueprint
foodfall_bp = Blueprint('foodfall', __name__)

@foodfall_bp.route('/stats', methods=['GET'])
def get_stats():
    """Get food fall (wastage) statistics"""
    # Response based on frontend requirements
    response = {
        "Total Wastage": 1250,
        "Cost Impact": 1875,
        "Environmental Impact": 320
    }
    return jsonify(response)

@foodfall_bp.route('/wastage', methods=['GET', 'POST'])
def get_wastage():
    """Get detailed food wastage information by time period"""
    try:
        # Default values
        base_type = 'M'  # Monthly by default
        base_count = 3   # 3 periods by default
        
        # Handle POST request with parameters
        if request.method == 'POST' and request.is_json:
            data = request.get_json()
            
            # Validate required fields
            if 'BaseType' not in data or 'BaseCount' not in data:
                return jsonify({"success": False, "error": "Missing required fields: BaseType and BaseCount"}), 400
                
            # Validate BaseType is one of the allowed values
            if data['BaseType'] not in ['W', 'M', 'Y', 'D']:
                return jsonify({"success": False, "error": "BaseType must be W, M, Y, or D"}), 400
                
            base_type = data['BaseType']
            base_count = data['BaseCount']
        
        # Generate dummy data based on requested parameters
        # In a real app, this would query the database for the specified time periods
        
        # Create wastage amounts for the requested periods
        wastage_amounts = [980, 1050, 1250][:base_count]
        
        if base_count > 3:
            # Generate additional dummy data if base_count > 3
            for i in range(3, base_count):
                wastage_amounts.append(900 + (i * 100))
        
        # Wastage response
        wastage_response = {
            "Wastage": wastage_amounts
        }
        
        return jsonify(wastage_response)
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@foodfall_bp.route('/items', methods=['GET', 'POST'])
def get_items():
    """Get wasted food items"""
    try:
        # Default values
        base_type = 'M'  # Monthly by default
        base_count = 3   # 3 periods by default
        
        # Handle POST request with parameters
        if request.method == 'POST' and request.is_json:
            data = request.get_json()
            
            # Validate required fields
            if 'BaseType' not in data or 'BaseCount' not in data:
                return jsonify({"success": False, "error": "Missing required fields: BaseType and BaseCount"}), 400
                
            # Validate BaseType is one of the allowed values
            if data['BaseType'] not in ['W', 'M', 'Y', 'D']:
                return jsonify({"success": False, "error": "BaseType must be W, M, Y, or D"}), 400
                
            base_type = data['BaseType']
            base_count = data['BaseCount']
        
        # In a real app, this would query the database for the most wasted items
        # based on the specified time periods
        
        # Items wastage response with dummy data
        items_response = {
            "Items": [
                {"Fried Rice": 32},
                {"Biryani": 28},
                {"Noodles": 22},
                {"Dosa": 18},
                {"Idly": 15}
            ]
        }
        
        return jsonify(items_response)
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@foodfall_bp.route('/category', methods=['GET', 'POST'])
def get_category():
    """Get food wastage by category"""
    try:
        # Default values
        base_type = 'M'  # Monthly by default
        base_count = 3   # 3 periods by default
        
        # Handle POST request with parameters
        if request.method == 'POST' and request.is_json:
            data = request.get_json()
            
            # Validate required fields
            if 'BaseType' not in data or 'BaseCount' not in data:
                return jsonify({"success": False, "error": "Missing required fields: BaseType and BaseCount"}), 400
                
            # Validate BaseType is one of the allowed values
            if data['BaseType'] not in ['W', 'M', 'Y', 'D']:
                return jsonify({"success": False, "error": "BaseType must be W, M, Y, or D"}), 400
                
            base_type = data['BaseType']
            base_count = data['BaseCount']
        
        # In a real app, this would query the database for wastage by category
        # based on the specified time periods
        
        # Category wastage response with dummy data
        category_response = {
            "Category": [
                {"Rice Items": 450},
                {"Breakfast Items": 320},
                {"Side Dishes": 280},
                {"Beverages": 120},
                {"Desserts": 80}
            ]
        }
        
        return jsonify(category_response)
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@foodfall_bp.route('/reason', methods=['GET', 'POST'])
def get_reason():
    """Get food wastage by reason"""
    try:
        # Default values
        base_type = 'M'  # Monthly by default
        base_count = 3   # 3 periods by default
        
        # Handle POST request with parameters
        if request.method == 'POST' and request.is_json:
            data = request.get_json()
            
            # Validate required fields
            if 'BaseType' not in data or 'BaseCount' not in data:
                return jsonify({"success": False, "error": "Missing required fields: BaseType and BaseCount"}), 400
                
            # Validate BaseType is one of the allowed values
            if data['BaseType'] not in ['W', 'M', 'Y', 'D']:
                return jsonify({"success": False, "error": "BaseType must be W, M, Y, or D"}), 400
                
            base_type = data['BaseType']
            base_count = data['BaseCount']
        
        # In a real app, this would query the database for wastage reasons
        # based on the specified time periods
        
        # Reason response with dummy data
        reason_response = {
            "Reason": [
                {"OverProduction": 625},
                {"Customer Returns": 300},
                {"Expired": 200},
                {"Quality Issues": 125}
            ]
        }
        
        return jsonify(reason_response)
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@foodfall_bp.route('/aiinsight', methods=['GET'])
def get_ai_insight():
    """Get AI-driven insights on food wastage"""
    # AI insights response
    response = {
        "Wastage Patterns": [
            "Fried Rice wastage increases by 18% during weekends",
            "Items prepared on Monday mornings have 12% higher wastage rate",
            "Reducing production quantities for dosas on Thursdays could save approximately ₹1,500 per month"
        ],
        "Recommendations": [
            "Adjust production for rice items to reduce by 15% on weekends",
            "Implement better forecasting for breakfast items to avoid overproduction",
            "Consider special offers for items that typically have higher wastage",
            "Review portion sizes for biryani as it shows consistent wastage"
        ],
        "Predicted Savings": {
            "Next Month": 8500,
            "Six Months": 60000,
            "Annual": 135000
        }
    }
    return jsonify(response)
