from datetime import datetime
import requests
import connexion
from connexion import NoContent
from apscheduler.schedulers.background import BackgroundScheduler
from pymongo import MongoClient
import pymongo
import datetime
import yaml
from flask_cors import CORS

LAST_UPDATE_DEFAULT="2022-10-05 18:20:17.885247"

with open('app_conf.yml', 'r') as f:
    app_config = yaml.safe_load(f.read())


def get_database():
 
   CONNECTION_STRING = app_config['datastore']['connectionstring']
 
   client = MongoClient(CONNECTION_STRING)
 
   return client['test']

def read_data():
    dbname = get_database()
    collection_name = dbname[app_config['datastore']['db']]
    result = list(collection_name.find().sort('last_updated',pymongo.DESCENDING))
    if len(result) == 0:
        return LAST_UPDATE_DEFAULT
    return result[0]['last_updated']

def write_data(data):
    dbname = get_database()
    collection_name = dbname[app_config['datastore']['db']]
    item={
        "top_grade":data['top_grade'],
        "avg_grade":data['avg_grade'],
        "last_updated":data['last_updated']
    }
    collection_name.insert_one(item)
    return 

def calculate_data(data):
    new={
        "top_grade":0,
        "avg_grade":0
    }
    if len(data) == 0:
        return new
    avg_grade=0
    top_grade=data[0]['grade']
    for i in data:
        top_grade=max(top_grade,i['grade'])
        avg_grade+=i['grade']
    
    new['top_grade'] = top_grade
    new['avg_grade'] = avg_grade/len(data)
    return new

def populate_stats():
    """ Periodically update stats """
    

    last_update=read_data()

    raw_data = requests.get(app_config['mysql']['url']+f"?timestamp={last_update}")
    processed_data = calculate_data(raw_data.json())

    mongo_data ={
        "top_grade":processed_data['top_grade'],
        "avg_grade":processed_data['avg_grade'],
        "last_updated":datetime.datetime.now()
    }
    write_data(mongo_data)
    print(f"data insert{mongo_data}")


def init_scheduler():
    sched = BackgroundScheduler(daemon=True)
    sched.add_job(populate_stats, 'interval', seconds=app_config['scheduler']['period_sec'])
    sched.start()

app = connexion.FlaskApp(__name__, specification_dir='')
CORS(app.app, resources={r"*": {"origins": "*", "headers": "*"}})

if __name__ == "__main__":
    init_scheduler()
    app.run(port=8092)