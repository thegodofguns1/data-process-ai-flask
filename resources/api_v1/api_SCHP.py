from flask_restful import Api, Resource, reqparse, request,fields, marshal_with
from flask import Response
from werkzeug.datastructures import FileStorage
import sys
import numpy as np
import cv2
sys.path.append("../../../../")

class SCHP(Resource):
    def get(self):
        pass 
    def post(self):
        ip = request.remote_addr
        print(ip)
        pass
    def delete(self):
        pass    