import requests
import connexion
import json
from connexion import NoContent
import yaml
from flask_cors import CORS

with open('app_conf.yml', 'r') as f:
    app_config = yaml.safe_load(f.read())


def username_password_info(body):
    response = requests.get(app_config['user']['url']+f"?username={body['username']}")
    if len(response.json()) != 0:
        if response.json()[0]['password'] == body['password']:
            return NoContent, 201
    
    return "Username or password doesn't match", 404

app = connexion.FlaskApp(__name__, specification_dir='')
CORS(app.app, resources={r"*": {"origins": "*", "headers": "*"}})
app.add_api("openapi.yml",strict_validation=True,validate_responses=True)

if __name__ == "__main__":
    app.run(port=8080)


# docker run -itd -p 8080:8080 bennyjiang/auth