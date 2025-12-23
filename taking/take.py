from flask import Flask , Blueprint , request , jsonify 
from db.db import TRACKING
from admin.tools import Check_Password

Take = Blueprint("Take" , __name__)

@Take.route("/finish/<date>" , methods=['POST'])
def Finish_Date(date):
    try:
        learned = request.json.get("learned")
        good = request.json.get("good")
        bad = request.json.get("bad")
        stuck = request.json.get("stuck")
        notes = request.json.get("notes")

        
        if not learned and not good and not bad and not stuck and not notes:
            return jsonify({"Success":False , "msg":"Must Provide all Feilds"}) , 400
        
        data = TRACKING.find_one({"date":date})
        if not data:
            return jsonify({"Success":False , "msg":"Date Not Found"})
        
        TRACKING.find_one_and_update({"date":date} , {"$set":{
            "stuck":stuck,
            "learned":learned,
            "good":good,
            "bad":bad,
            "notes":notes,
            "finished":True
        }})
        return jsonify({"Success":True , "msg":"Data Updated Succesfully"}) , 200
    except:
        return jsonify({"Success":False , 'msg':"Internal Server Error"}) , 500



    