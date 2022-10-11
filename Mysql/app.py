import connexion
from connexion import NoContent
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from base import Base
import yaml
import datetime
import pymysql
from user import User
from grade import Grade
from flask_cors import CORS


with open('app_conf.yml', 'r') as f:
    app_config = yaml.safe_load(f.read())


database=app_config['datastore']

DB_ENGINE= create_engine('mysql+pymysql://{}:{}@{}:{}/{}'.format(database['user'],database['password'],database['hostname'],database['port'],database['db']))
Base.metadata.bind = DB_ENGINE
DB_SESSION = sessionmaker(bind=DB_ENGINE)


def get_username_password(username):
    session = DB_SESSION()
    readings = session.query(User).filter(User.username == username)
    result=[]
    for i in readings:
        result.append(i.to_dict())
    session.close()

    return result, 200


def get_raw_data(timestamp):
    session = DB_SESSION()
    timestamp="".join(timestamp.split())
    timestamp_datetime = datetime.datetime.strptime(timestamp, '%Y-%m-%d%H:%M:%S.%f')
    readings = session.query(Grade).filter(Grade.date_created >= timestamp_datetime)
    results_list = []
    for reading in readings:
        results_list.append(reading.to_dict())
    session.close()

    return results_list, 200

def grade_data_in(body):

    session = DB_SESSION()

    grade = Grade(  
            body['studentID'],
            body['name'],
            body['grade']
            )

    session.add(grade)

    session.commit()
    session.close()
    return NoContent, 200

def user_data_in(body):

    session = DB_SESSION()
    print(body)
    user = User(  
            body['username'],
            body['password'],
            )

    session.add(user)

    session.commit()
    session.close()
    return NoContent, 200


app = connexion.FlaskApp(__name__, specification_dir='')
CORS(app.app, resources={r"*": {"origins": "*", "headers": "*"}})
app.add_api("openapi.yml",strict_validation=True,validate_responses=True)

if __name__ == "__main__":
    app.run(port=8090)