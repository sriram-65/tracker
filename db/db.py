from pymongo import MongoClient

client = MongoClient("mongodb+srv://sriram65raja_db_user:1324sriram@cluster0.rbnikra.mongodb.net/")

db = client['mytracker']
TRACKING = db['TRACKING']

