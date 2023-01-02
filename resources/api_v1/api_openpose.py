from flask_restful import Api, Resource, reqparse, request,fields, marshal_with
from flask import Response
from werkzeug.datastructures import FileStorage
import sys
import numpy as np
import cv2
# sys.path.append("../../")

class OpenPose(Resource):
    def get(self):
        ip = request.remote_addr # "159.75.217.15"
        return {'code':200,'data':ip}
    def post(self):
        ip = request.remote_addr
        
        return {'code':200,'data':ip}
    def delete(self):
        pass    