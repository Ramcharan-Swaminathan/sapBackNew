from flask import Blueprint, jsonify, request, current_app
import jwt
import os
from functools import wraps
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required


# Create the blueprint
about_bp = Blueprint('about', __name__)

@about_bp.route('/', methods=['GET'])
@jwt_required()
def get_about():
    """Get about information based on user role"""

    data = get_jwt_identity()
    userId  = data["UserID"]
    userRole = data["Role"]

    db = current_app.config["DataBase"]

    query = {"UserID" : userId}
    user = db.qurryData("User", query)
    
    if(len(user)==0):
        return jsonify({"Status" : "Error No data found"}),404
    
    user = user[0]

    query = {"CompanyID" : user["CompanyID"]}
    company = db.qurryData("Company", query)

    if(len(company)==0):
        return jsonify({"Status" : "Error No data found"})
    
    company = company[0]

    return jsonify({"user" : user["Data"], "company_data" : company["Data"]})



@about_bp.route('/', methods=['PUT'])
@jwt_required()
def update_about():
    """Updating   information for user & company"""
    data = get_jwt_identity()
    userId = data["UserID"]
    db = current_app.config["DataBase"]

    req_json = request.get_json()
    if not req_json:
        return jsonify({"success": False, "error": "No input data provided"}), 400

    user_update = req_json.get("user")
    company_update = req_json.get("company_data")
    if not user_update and not company_update:
        return jsonify({"success": False, "error": "No update data provided"}), 400

    # Update user data if provided
    user_result = None
    if user_update:
        user_query = {"UserID": userId}
        user_result = db.updateData("User", user_query, {"Data": user_update})
        if not user_result:
            return jsonify({"success": False, "error": "Failed to update user"}), 500

    # Get user's company ID
    user = db.qurryData("User", {"UserID": userId})
    if not user or "CompanyID" not in user[0]:
        return jsonify({"success": False, "error": "User or company not found"}), 404
    company_id = user[0]["CompanyID"]

    # Update company data if provided
    company_result = None
    if company_update:
        company_query = {"CompanyID": company_id}
        company_result = db.updateData("Company", company_query, {"Data": company_update})
        if not company_result:
            return jsonify({"success": False, "error": "Failed to update company"}), 500

    return jsonify({"success": True}), 200
