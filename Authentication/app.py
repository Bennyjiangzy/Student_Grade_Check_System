import requests
import connexion
import json
from connexion import NoContent
import yaml


with open('app_conf.yml', 'r') as f:
    app_config = yaml.safe_load(f.read())


def username_password_info(body):
    name_password = {
                "username":body['username'],
                "password":body['password']
                }
    print(name_password)
    # response = requests.get(app_config['user']['url']+f"{name_password['username']}")
    # if reponse[0].to_dict() == name_password['password']:
    #     return NoContent, 201
    if "123456" == name_password['password']:
        return NoContent, 201
    else:
        return "Username or password doesn't match", 404

app = connexion.FlaskApp(__name__, specification_dir='')
app.add_api("openapi.yml",strict_validation=True,validate_responses=True)

if __name__ == "__main__":
    app.run(port=8080)