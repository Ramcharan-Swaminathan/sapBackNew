from flask import Blueprint, jsonify, request

# Create the blueprint
foodsafety_bp = Blueprint('foodsafety', __name__)

@foodsafety_bp.route('/inspection', methods=['GET'])
def get_inspection():
    """Get food safety inspection details"""
    # Dummy response
    response = {
        "success": True,
        "data": {
            "last_inspection": "2025-04-15",
            "score": 96,
            "inspector": "Jane Smith",
            "issues": [
                {"id": 1, "description": "Temperature control in refrigerator #3", "severity": "minor"},
                {"id": 2, "description": "Employee handwashing logs incomplete", "severity": "minor"}
            ],
            "next_inspection_due": "2025-07-15"
        }
    }
    return jsonify(response)

@foodsafety_bp.route('/inspection', methods=['PUT'])
def update_inspection():
    """Update food safety inspection records"""
    try:
        # Check if request contains JSON data
        if not request.is_json:
            return jsonify({"success": False, "error": "Request must contain JSON data"}), 400
        
        data = request.get_json()
        
        # In a real app, validate and save the data
        # For now, just return success with the received data
        response = {
            "success": True,
            "message": "Inspection data updated successfully",
            "updated_data": data
        }
        return jsonify(response)
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@foodsafety_bp.route('/stats', methods=['GET'])
def get_stats():
    """Get food safety statistics"""
    # Dummy response
    response = {
        "success": True,
        "data": {
            "inspection_score_trend": [92, 94, 96, 95, 96],
            "critical_violations_ytd": 0,
            "minor_violations_ytd": 5,
            "staff_certification_percentage": 100,
            "temperature_log_compliance": 98.5
        }
    }
    return jsonify(response)
