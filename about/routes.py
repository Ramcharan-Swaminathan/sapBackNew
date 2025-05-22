from flask import Blueprint, jsonify, request
import jwt
import os
from functools import wraps

# Create the blueprint
about_bp = Blueprint('about', __name__)

# Mock JWT secret key (in production, this would be securely stored)
JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY', 'dev_secret_key')

# Mock database
mock_db = {
    "admin_user": {
        "user": {
            "name": "Admin User",
            "email": "admin@example.com",
            "mobile_number": "555-123-4567",
        },
        "company_data": {
            "company_name": "FoodTech Solutions",
            "Opening_Hours": "08:00",
            "Address": "123 Food Street, Delhi, India",
            "Description": "Authentic Indian cuisine with a modern twist."
        },
        "role": "admin"
    },
    "manager_user": {
        "user": {
            "name": "Manager User",
            "email": "manager@example.com",
            "mobile_number": "555-234-5678",
        },
        "company_data": {
            "company_name": "FoodTech Solutions",
            "Opening_Hours": "08:00",
            "Address": "123 Food Street, Delhi, India",
            "Description": "Authentic Indian cuisine with a modern twist.",
            "employee_id": "FT-101",
            "department": "Operations"
        },
        "role": "manager"
    },
    "employee_user": {
        "user": {
            "name": "Employee User",
            "email": "employee@example.com",
            "mobile_number": "555-345-6789",
        },
        "company_data": {
            "company_name": "FoodTech Solutions",
            "Opening_Hours": "08:00",
            "Address": "123 Food Street, Delhi, India",
            "Description": "Authentic Indian cuisine with a modern twist.",
            "employee_id": "FT-201",
            "department": "Kitchen"
        },
        "role": "employee"
    },
    "public": {
        "name": "FoodTech Solutions",
        "mobile_number": "555-987-6543",
        "Address": "123 Food Street, Delhi, India",
        "Description": "Authentic Indian cuisine with a modern twist."
    }
}

def get_user_from_token(request):
    """Extract user info from JWT token"""
    try:
        # Check if Authorization header exists
        auth_header = request.headers.get('Authorization')
        if auth_header and auth_header.startswith('Bearer '):
            token = auth_header.split(' ')[1]
            payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=['HS256'])
            user_id = payload.get('uid')
            return user_id
        return None
    except jwt.PyJWTError:
        return None

@about_bp.route('/', methods=['GET'])
def get_about():
    """Get about information based on user role"""
    user_id = get_user_from_token(request)
    
    # If no valid token or user not found, return public info
    if not user_id or user_id not in mock_db:
        return jsonify(mock_db["public"])
    
    user_data = mock_db[user_id]
    role = user_data.get("role", "public")
    
    # Return different response based on role
    if role == "admin":
        return jsonify({
            "user": user_data["user"],
            "company_data": user_data["company_data"]
        })
    elif role == "manager" or role == "employee":
        return jsonify({
            "user": {
                "name": user_data["user"]["name"],
                "mobile_number": user_data["user"]["mobile_number"]
            },
            "company_data": user_data["company_data"]
        })
    else:
        # Default to public view
        return jsonify(mock_db["public"])

@about_bp.route('/', methods=['PUT'])
def update_about():
    """Update about information based on user role"""
    try:
        # Check if request contains JSON data
        if not request.is_json:
            return jsonify({"success": False, "error": "Request must contain JSON data"}), 400
        
        data = request.get_json()
        user_id = get_user_from_token(request)
        
        # If no valid token or user not found, assume public update
        if not user_id or user_id not in mock_db:
            # Update public information (limited fields)
            public_data = {
                "name": data.get("name", mock_db["public"]["name"]),
                "mobile_number": data.get("mobile_number", mock_db["public"]["mobile_number"]),
                "Address": data.get("Address", mock_db["public"]["Address"]),
                "Description": data.get("Description", mock_db["public"]["Description"])
            }
            mock_db["public"] = public_data
            return jsonify({
                "success": True,
                "message": "Public information updated successfully",
                "updated_data": public_data
            })
        
        user_data = mock_db[user_id]
        role = user_data.get("role", "public")
        
        # Only admin can update company data
        if role == "admin":
            # Update user and company data
            if "user" in data:
                mock_db[user_id]["user"] = data["user"]
            if "company_data" in data:
                mock_db[user_id]["company_data"] = data["company_data"]
            
            return jsonify({
                "success": True,
                "message": "Admin and company information updated successfully",
                "updated_data": mock_db[user_id]
            })
        else:
            # Non-admin users can only update their own information
            if "user" in data:
                allowed_fields = ["name", "mobile_number"]
                for field in allowed_fields:
                    if field in data["user"]:
                        mock_db[user_id]["user"][field] = data["user"][field]
            
            return jsonify({
                "success": True,
                "message": "User information updated successfully",
                "updated_data": {
                    "user": {
                        "name": mock_db[user_id]["user"]["name"],
                        "mobile_number": mock_db[user_id]["user"]["mobile_number"]
                    }
                }
            })
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500
