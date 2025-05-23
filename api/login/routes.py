from flask import Blueprint, request, jsonify, current_app
from flask_jwt_extended import create_access_token


login_bp = Blueprint('login', __name__)


@login_bp.route('/', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        return jsonify({'msg': 'Missing username or password'}), 400

    db = current_app.config['DataBase']
    user_list = db.qurryData('User', {'UserID': username})
    if not user_list:
        return jsonify({'msg': 'User not found'}), 404
    user = user_list[0]

    if 'password' not in user or user['password'] != password:
        return jsonify({'msg': 'Bad username or password'}), 401
    user_id = user['UserID']
    role = user['Data']['role']
    access_token = create_access_token(identity={"UserID": user_id, "Role": role})
    return jsonify(access_token=access_token, role=role), 200
