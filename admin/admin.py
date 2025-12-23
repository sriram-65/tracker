from flask import Flask , Blueprint , request , redirect , render_template , jsonify
from db.db import TRACKING
from datetime import datetime , timedelta

Ad = Blueprint("Admin" , __name__)

@Ad.route("/admin")
def Admin():
    return render_template("admin/admin.html")

@Ad.route("/generate-placeholder" , methods=['POST'])
def Generate_Placeholder():
    try:
        doc = []
        today = datetime.today()

        for i in range(7):
          current_date = today+timedelta(days=i)

          data = {
                "day":i+1,
                "date":current_date.strftime("%d-%m-%Y"),
                "stuck": "",
                "learned": "",
                "good": "",
                "bad": "",
                "notes": "",
                "ai_feedback": [],
                "finished":False
          }

          doc.append(data)
        
        TRACKING.insert_many(doc)
        return jsonify({"Success":True , 'data':"Placeholder for 7 days has Been Created Successfully"}) , 200
    except:
        return jsonify({"Success":False , 'msg':"Server Error"}) , 500
    

@Ad.route("/show")
def Show():
    try:
        data = TRACKING.find({})
        docs = []
        for i in data:
            i['_id'] = str(i['_id'])
            docs.append(i)
        
        return jsonify({"Success":True , "data":docs}) , 200
    except:
        return jsonify({"Success":False , 'msg':"Server Error"}) , 500
    

@Ad.route("/delete-all" , methods=['DELETE'])
def Delete_All():
    TRACKING.delete_many({})
    return jsonify("Deleted")

@Ad.route("/delete/<date>" , methods=['DELETE'])
def Delete_date(date):
    try:
        data = TRACKING.find_one({"date":date})
        if not data:
            return jsonify({"Success":False , "msg":"Date not Found"}) , 400
        
        TRACKING.find_one_and_delete({"date":date})
        return jsonify({"Success":True , "msg":"Deleted Successfully"}) , 200
    except:
        return jsonify({"Success":False , 'msg':"Server Error"}) , 500




