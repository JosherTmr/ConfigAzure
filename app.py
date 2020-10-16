from os import abort
from flask import Flask
from flask import jsonify
from flask import request
app = Flask(__name__)
studentsDB = [
 {
 'id':'T00055671',
 'name':'Juan Perez',
 'course':'Machine Learning'
 },
 {
 'id':'T00045678',
 'name':'Maria Martinez',
 'course':'Software Engineer'
 }
 ]
@app.route('/')
def home():
    return '''<!DOCTYPE html>
            <html>
            <head>
            <style>
            h1 {
              color: blue;
              font-family: verdana;
              font-size: 300%;
            }
            p {
              color: red;
              font-family: courier;
              font-size: 160%;
            }
            </style>
            </head>
            <body>

            <h1>Bienvenido</h1>
            <p>Esta es mi página Web</p>

            </body>
            </html>'''
@app.route('/students/' or '/students' ,methods=['GET'])
def get_all_students():
    return jsonify({'students': studentsDB})

@app.route('/students/<stdId>',methods=['GET'])
def get_students(stdId):
    usr = [std for std in studentsDB if (std['id'] == stdId)]
    return jsonify({'est': usr})

@app.route('/students/<stdId>',methods=['PUT'])
def update_students(stdId):
    row = [est for est in studentsDB if (est['id'] == stdId)]
    if 'name' in request.json:
        row[0]['name'] = request.json['name']
    if 'course' in request.json:
        row[0]['course'] = request.json['course']
    return jsonify({'est': row[0]})

@app.route('/students/',methods=['POST'])
def create_student():
    dat = {
    'id': request.json['id'],
    'name': request.json['name'],
    'course': request.json['course']
    }
    studentsDB.append(dat)
    return jsonify(dat)

@app.route('/students/<stdId>',methods=['DELETE'])
def delete_student(stdId):
    row = [est for est in studentsDB if (est['id'] == stdId)]
    if len(row) == 0:
        abort(404)
    studentsDB.remove(row[0])
    return jsonify({'response': 'Success'})

if __name__ == '__main__':
    app.run()
