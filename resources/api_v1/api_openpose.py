from flask_restful import Api, Resource, reqparse, request,fields, marshal_with
from flask import Response
from werkzeug.datastructures import FileStorage
import sys
import numpy as np
import cv2
sys.path.append("../../")
from common import code
import config
# jsonify(pretty_result(code.PARAM_ERROR, data=message))
class OpenPose(Resource):
    def get(self):
        ip = request.remote_addr # "159.75.217.15"
        if ip in config.ALLOW_IPS:
            
            return {'code':code.OK,'data':ip}
        else:
            return {'code':code.AUTHORIZATION_ERROR,'data':[],'message':"API未授权"}
    def post(self):
        ip = request.remote_addr # "159.75.217.15"
        if ip in config.ALLOW_IPS:
            
            return {'code':code.OK,'data':ip}
        else:
            return {'code':code.AUTHORIZATION_ERROR,'data':[],'message':"API未授权"}
    def delete(self):
        pass    