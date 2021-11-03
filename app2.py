from flask import Flask, Blueprint
from flask_restful import Api, Resource

app = Flask(__name__)


api = Api(app)

class Student(Resource):
    def get(self,name:str):
        return {'student':name.capitalize()}

api.add_resource(Student,'/student/<string:name>')

app.run(port=3333)