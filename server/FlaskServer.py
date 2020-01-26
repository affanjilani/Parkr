from db.credentials import db_name, user, pw, db_url
from flask import Flask, request
import psycopg2
import json

# www.api.py

# rest API (front-end request things from the end-points)
# react.js app - for front-end, query flask -> database -> show to user
# showing visual statistics

# connect to "aws rds Aurora" which hosts "postgresql database" which you should query/communicate with
# https://aws.amazon.com/blogs/database/using-the-data-api-to-interact-with-an-amazon-aurora-serverless-mysql-database/
# Wael sends license plate & parking spot to server; method sends the info from a docString to the database. Post request end-point args = parkingID, licensePlate

app = Flask(__name__)

@app.route('/')
def home():
    return 'db_name = ' + db_name + ', user = ' + user + ', pw = ' + pw + ', db_url = ' + db_url

# http://127.0.0.1:8080/updateParkingSpot?licensePlate=H9R1K7&parkingID=1
# parkingID = 1, licensePlate = H9R1K7
@app.route('/updateParkingSpot')
def updateParkingSpot():
    licensePlate = request.args.get('licensePlate', default = 'emptyLicensePlate', type = str)
    parkingID = request.args.get('parkingID', default = 'emptyParkingID', type = str)
    return 'licensePlate = ' + licensePlate + ', parkingID = ' + parkingID

@app.route('/getParkingSpots')
def getParkingSpots():
    data = {}
    data['key'] = 'value'
    json_data = json.dumps(data)
    return json_data

@app.route('/getHeatMaps')
def getHeatMaps():
    return "connect & query postgresql database for statistics"

if __name__ == '__main__':
    # Connect to the PostgreSQL database server
    conn = None
    try:
        # read connection parameters from credentials.py & connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(host = db_url, database = db_name, user = user, password = pw)
        # server running
        app.run(host='127.0.0.1', port=8080)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')