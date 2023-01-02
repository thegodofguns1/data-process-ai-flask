from flask import Blueprint
from flask_restful import Api
 

api_v1 = Blueprint('api_v1', __name__)

api = Api(api_v1)

from resources.api_v1.api_openpose import OpenPose
from resources.api_v1.api_SCHP import SCHP
from resources.api_v1.api_test import Test
api.add_resource(Test,'/')
api.add_resource(OpenPose, '/api/v1/OpenPose')
