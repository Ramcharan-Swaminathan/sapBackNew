from flask import Blueprint, jsonify, request

# Create the blueprint
inventory_bp = Blueprint('inventory', __name__)

@inventory_bp.route('/', methods=['GET'])
def get_inventory():
    """Get all inventory items"""
    try:
        # In a real app, fetch items from database
        # For now, return dummy data in the specified format
        dummy_items = [
            {
                "Name": "Milk",
                "Category": "Dairy",
                "Quantity": 100,
                "Quantity Type": "Liters",
                "Expiry Date": "30-05-2025"
            },
            {
                "Name": "Apples",
                "Category": "Produce",
                "Quantity": 250,
                "Quantity Type": "Kg",
                "Expiry Date": "10-06-2025"
            },
            {
                "Name": "Bread",
                "Category": "Bakery",
                "Quantity": 80,
                "Quantity Type": "Loaves",
                "Expiry Date": "25-05-2025"
            }
        ]
        
        response = {
            "ItemsCount": len(dummy_items),
            "Items": dummy_items
        }
        
        return jsonify(response)
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@inventory_bp.route('/', methods=['PUT'])
def update_inventory():
    """Update inventory items"""
    try:
        # Check if request contains JSON data
        if not request.is_json:
            return jsonify({"success": False, "error": "Request must contain JSON data"}), 400
        
        data = request.get_json()
        
        # Validate required fields
        required_fields = ["Name", "Category", "Quantity", "Quantity Type", "InDate", "Expiry Date"]
        for field in required_fields:
            if field not in data:
                return jsonify({"success": False, "error": f"Missing required field: {field}"}), 400
        
        # In a real app, validate and save the data
        # For now, just return success with the received data
        response = {
            "success": True,
            "message": "Inventory item added/updated successfully",
            "item": data
        }
        return jsonify(response)
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@inventory_bp.route('/', methods=['DELETE'])
def delete_inventory():
    """Delete inventory items"""
    try:
        # Check if request contains JSON data
        if not request.is_json:
            return jsonify({"success": False, "error": "Request must contain JSON data"}), 400
        
        data = request.get_json()
        
        # In a real app, validate and delete the specified items
        # For now, just return success with the received data
        response = {
            "success": True,
            "message": "Inventory items deleted successfully",
            "deleted_items": data
        }
        return jsonify(response)
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@inventory_bp.route('/stats', methods=['GET'])
def get_stats():
    """Get inventory statistics"""
    # Dummy response
    response = {
        "success": True,
        "data": {
            "total_items": 1250,
            "total_value": 187500,
            "categories": {
                "dairy": 120,
                "produce": 350,
                "meat": 95,
                "bakery": 175,
                "frozen": 210,
                "dry_goods": 300
            },
            "low_stock_items": 15,
            "expiring_soon": 28
        }
    }
    return jsonify(response)

@inventory_bp.route('/export', methods=['GET'])
def export_inventory():
    """Export inventory data"""
    # Dummy response
    response = {
        "success": True,
        "data": {
            "export_url": "https://example.com/exports/inventory_2025_05_22.csv",
            "export_date": "2025-05-22",
            "item_count": 1250,
            "formats_available": ["CSV", "JSON", "XLSX"]
        }
    }
    return jsonify(response)
