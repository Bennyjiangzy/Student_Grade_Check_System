import mysql.connector
import yaml

with open('app_conf.yml', 'r') as f:
    app_config = yaml.safe_load(f.read())

database=app_config['datastore']
# db_conn = mysql.connector.connect(host=database['hostname'], user=database['user'],
# password=database['password'])
# db_cursor = db_conn.cursor()
# db_cursor.execute('''
#                 CREATE DATABASE assign;
#             ''')

# db_conn.commit()
# db_conn.close()

db_conn = mysql.connector.connect(host=database['hostname'], user=database['user'],
password=database['password'], database=database['db'])
db_cursor = db_conn.cursor()

db_cursor.execute('''
          CREATE TABLE user
          (id INT NOT NULL AUTO_INCREMENT, 
           username VARCHAR(250) NOT NULL,
           password VARCHAR(250) NOT NULL,
           CONSTRAINT blood_pressure_pk PRIMARY KEY (id))
          ''')

db_cursor.execute('''
          CREATE TABLE grade
          (id INT NOT NULL AUTO_INCREMENT, 
           studentID VARCHAR(250) NOT NULL,
           name VARCHAR(250) NOT NULL,
           grade INT NOT NULL,
           date_created VARCHAR(100) NOT NULL,
           CONSTRAINT blood_pressure_pk PRIMARY KEY (id))
          ''')
db_conn.commit()
db_conn.close()