from flask import Blueprint, jsonify,request,current_app
from flask_jwt_extended import get_jwt_identity, jwt_required
import datetime

bill_bp = Blueprint('bill', __name__)



@bill_bp.route('/', methods=['POST'])
@jwt_required()
def add_bill():
    '''To add a new bill to the databse'''
    data  = get_jwt_identity()
    userID = data["UserID"]
    userRole = data["Role"]

    db = current_app.config["DataBase"]

    user = db.qurryData("User", {"UserID" : userID})

    userID = user[0]["UserID"]
    cmpID = user[0]["CompanyID"]

    req_json = request.get_json()

    #if invoice id already ecists , the return status Failure
    invoices = db.qurryData("Bill", {"InvoiceID" : req_json["InvoiceID"]})
    if len(invoices) != 0:
        return jsonify({"Status":"Failure", "Message":"Invoice ID already exists"}), 400

    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
    final_json = {"CompanyId":cmpID,
                          "Datetime":formatted_time,
                          "InvoiceId":req_json["InvoiceID"],
                          "IssuedBy":userID,
                          "Data":req_json["Data"]
                         }
    
    db.insertData("Bill", final_json)

    return jsonify({"Status":"Success"}), 200
