from flask import Blueprint, jsonify, request, current_app
import jwt
import os
from functools import wraps
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
import json
from bson.json_util import dumps

# Create the blueprint
about_bp = Blueprint('about', __name__)

@about_bp.route('/', methods=['GET'])
@jwt_required()
def get_about():
    """Get about information based on user role"""

    data = get_jwt_identity()
    userId  = data["UID"]
    userRole = data["Role"]

    db = current_app.config["DataBase"]

    qurry = {"id" : userId}
    user = db.qurryData("User",qurry)
    json_str = dumps(user)
    user_obj = json.loads(json_str)

    if(len(user_obj)==0):
        return jsonify({"Status" : "Error No data found"}),404
    
    user_obj = user_obj[0]


    qurry = {"id" : user_obj["Company_ID"]}
    company = db.qurryData("Company",qurry)
    json_str = dumps(company)
    company_obj = json.loads(json_str)


    if(len(company_obj)==0):
        return jsonify({"Status" : "Error No data found"})
    
    company_obj = company_obj[0]

    return jsonify({"user" : user_obj["data"], "company_data" : company_obj["data"]})



@jwt_required()
@about_bp.route('/', methods=['PUT'])
def update_about():
    return jsonify({"success": False}), 500
