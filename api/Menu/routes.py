from flask import Blueprint,current_app,request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import jsonify


menu_bp = Blueprint('menu', __name__)


@menu_bp.route('/',methods=['GET'])
@jwt_required()
def get_menu():
    ''' To get the menu  of the unavagam'''
    data = get_jwt_identity()
    userID = data["UserID"]
    #userRole = data["Role"]
    db = current_app.config["DataBase"]
    user = db.qurryData("User", {"UserID": userID})
    if len(user) == 0:
        return jsonify({"Status": "Failure", "Message": "User not found"}), 400
    userID = user[0]["UserID"]
    cmpID = user[0]["CompanyID"]
    menu_cmp = db.qurryData("Menu", {"CompanyID": cmpID})
    if len(menu_cmp) == 0:
        return jsonify({"Status": "Failure", "Message": "No menu found"}), 400
    else:
        menu = menu_cmp[0]["Items"]
        return jsonify({"Status": "Success", "Items": menu}), 200



@menu_bp.route('/', methods=['POST'])
@jwt_required()
def add_menu():
    ''' To add menu for the unavagam'''
    data = get_jwt_identity()
    userID = data["UserID"]
    db = current_app.config["DataBase"]

    user = db.qurryData("User", {"UserID": userID})
    if not user:
        return jsonify({"Status": "Failure", "Message": "User not found"}), 400

    company_id = user[0]["CompanyID"]
    req = request.get_json()

    if "Items" not in req or not isinstance(req["Items"], list):
        return jsonify({"Status": "Failure", "Message": "Invalid input data"}), 400

    menu_list = db.qurryData("Menu", {"CompanyID": company_id})
    if menu_list:
        # Menu exists, append or update items
        menu = menu_list[0]
        existing_items = menu.get("Items", [])
        existing_item_ids = {item["ItemID"]: item for item in existing_items}
        for new_item in req["Items"]:
            if new_item["ItemID"] in existing_item_ids:
                # Update the exist item 
                existing_item_ids[new_item["ItemID"]].update(new_item)
            else:
                # Add new item
                existing_items.append(new_item)
        # Update the menu
        result = db.updateData("Menu", {"CompanyID": company_id}, {"Items": existing_items})
        if hasattr(result, 'modified_count') and result.modified_count > 0:
            return jsonify({"Status": "Success", "Message": "Menu updated with new items"}), 200
        else:
            return jsonify({"Status": "Failure", "Message": "Failed to update menu"}), 500
    else:
        # No menu exists, so create new
        menu_doc = {
            "CompanyID": company_id,
            "Items": req["Items"]
        }
        success = db.insertData("Menu", menu_doc)
        if success:
            return jsonify({"Status": "Success", "Message": "Menu added successfully"}), 201
        else:
            return jsonify({"Status": "Failure", "Message": "Failed to insert menu"}), 500


@menu_bp.route('/', methods=['PUT'])
@jwt_required()
def update_menu():
    '''Update the menu for the unavagam'''
    data = get_jwt_identity()
    userID = data["UserID"]
    db = current_app.config["DataBase"]

    user = db.qurryData("User", {"UserID": userID})
    if not user:
        return jsonify({"Status": "Failure", "Message": "User not found"}), 400

    company_id = user[0]["CompanyID"]
    req = request.get_json()

    if "Items" not in req or not isinstance(req["Items"], list):
        return jsonify({"Status": "Failure", "Message": "Invalid input data"}), 400

    # Get currant menu
    menu_list = db.qurryData("Menu", {"CompanyID": company_id})
    if not menu_list:
        return jsonify({"Status": "Failure", "Message": "Menu not found"}), 400
    menu = menu_list[0]
    existing_items = menu.get("Items", [])
    existing_item_ids = {item["ItemID"]: item for item in existing_items}
    updated = False
    for upd_item in req["Items"]:
        item_id = upd_item.get("ItemID")
        if item_id in existing_item_ids:
            existing_item_ids[item_id].update(upd_item)
            updated = True
    if not updated:
        return jsonify({"Status": "Failure", "Message": "No matching items to update"}), 400
    
    # Saving updated items
    result = db.updateData("Menu", {"CompanyID": company_id}, {"Items": list(existing_item_ids.values())})
    if hasattr(result, 'modified_count') and result.modified_count > 0:
        return jsonify({"Status": "Success", "Message": "Menu updated successfully"}), 200
    else:
        return jsonify({"Status": "Failure", "Message": "No changes made or menu not found"}), 400