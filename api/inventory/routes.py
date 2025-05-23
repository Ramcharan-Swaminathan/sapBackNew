from flask import Blueprint, jsonify, request, current_app
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required

# Create the blueprint
inventory_bp = Blueprint('inventory', __name__)




@inventory_bp.route('/', methods=['GET'])
@jwt_required()
def get_inventory():
    """Get all inventory items"""
    try:
        db = current_app.config['DataBase']

        data = get_jwt_identity()
        UserID = data['UserID']
        qurry = {"UserID" : UserID}

        companyID = db.qurryData("User",qurry)[0]["CompanyID"]

        qurry = {"CompanyID" : companyID}
        data = db.qurryData("Inventory",qurry)[0]

        response = {}
        response["ItemsCount"] = len(data["Items"])
        response["Items"] = data["Items"]

        
        return jsonify(response)
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500





@inventory_bp.route('/', methods=['POST'])
@jwt_required()
def insert_inventory():
    """Update inventory items"""
    try:
        # Check if request contains JSON data
        if not request.is_json:
            return jsonify({"success": False, "error": "Request must contain JSON data"}), 400
        
        req = request.get_json()
        
        # Validate required fields
        required_fields = [ "Name", "Category", "Quantity", "QuantityType", "InDate", "Expiry Date"]
        
        if "Item" not in req:
            return jsonify({"success": False, "error": f"Missing required field: Item"}), 400

        item = req["Item"]

        for field in required_fields:
            if field not in item:
                return jsonify({"success": False, "error": f"Missing required field: {field}"}), 400

        db = current_app.config['DataBase']

        data = get_jwt_identity()
        UserID = data['UserID']
        qurry = {"UserID" : UserID}

        companyID = db.qurryData("User",qurry)[0]["CompanyID"]

        qurry = {"CompanyID" : companyID}
        data = db.qurryData("Inventory",qurry)[0]

        if data is None:
            data['CompanyID'] = companyID
            item["ItemID"] = 1
            data['Items'] = [item]
            db.insertData("Inventory",data)
        else:
            item["ItemID"] = len(data['Items']) + 1
            data['Items'].append(item)
            db.updateData("Inventory",qurry,{"Items" : data["Items"]})

        response = {
            "success": True,
            "message": "Inventory item added/updated successfully",
            "item": data
        }

        return jsonify(response)

    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@inventory_bp.route('/', methods=['PUT'])
@jwt_required()
def update_inventory():
    try:
        # Check if request contains JSON data
        if not request.is_json:
            return jsonify({"success": False, "error": "Request must contain JSON data"}), 400
        
        item = request.get_json()

        if "Item" not in item:
            return jsonify({"success": False, "error": f"Missing required field: Item"}), 400

        item = item["Item"]
        required_fields = ["ItemID", "Name", "Category", "Quantity", "QuantityType", "InDate", "Expiry Date"]

        for field in required_fields:
            if field not in item:
                return jsonify({"success": False, "error": f"Missing required field: {field}"}), 400

        itemID = item["ItemID"]
        db = current_app.config['DataBase']

        data = get_jwt_identity()
        UserID = data['UserID']
        qurry = {"UserID" : UserID}

        companyID = db.qurryData("User",qurry)[0]["CompanyID"]

        qurry = {"CompanyID" : companyID}
        data = db.qurryData("Inventory",qurry)[0]

        pos = -1

        for i in range(0,len(data["Items"])):
            if "ItemID" not in data["Items"][i]:
                continue
            if data["Items"][i]["ItemID"] == itemID:
                pos = i
                break

        if pos == -1:
            return jsonify({"sucess" : False, "message" : "Invalid ItemID"}), 400

        data['Items'][pos] = item

        db.updateData("Inventory",qurry,{"Items" : data["Items"]})

        response = {
            "success": True,
            "message": "Inventory items updated successfully",
            "deleted_items": data
        }
        return jsonify(response)
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@inventory_bp.route('/', methods=['DELETE'])
@jwt_required()
def delete_inventory():
    """Delete inventory items"""
    try:
        # Check if request contains JSON data
        if not request.is_json:
            return jsonify({"success": False, "error": "Request must contain JSON data"}), 400
        
        data = request.get_json()

        if "ItemID" not in data:
            return jsonify({"success": False, "error": f"Missing required field: ItemID"}), 400

        itemID = data["ItemID"]
        db = current_app.config['DataBase']

        data = get_jwt_identity()
        UserID = data['UserID']
        qurry = {"UserID" : UserID}

        companyID = db.qurryData("User",qurry)[0]["CompanyID"]

        qurry = {"CompanyID" : companyID}
        data = db.qurryData("Inventory",qurry)[0]

        pos = -1

        return jsonify({"COunt" : len(data["Items"])})

        for i in range(0,len(data["Items"])):
            if "ItemID" not in data["Items"][i]:
                continue
            if data["Items"][i]["ItemID"] == itemID:
                pos = i
                break

        if pos == -1:
            return jsonify({"sucess" : False, "message" : "Invalid ItemID"}), 400

        data['Items'].pop(pos)
        db.updateData("Inventory",qurry,{"Items" : data["Items"]})

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
