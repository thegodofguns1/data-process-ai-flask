from flask_restful import Api, Resource, reqparse, request,fields, marshal_with
from flask import Response
from werkzeug.datastructures import FileStorage
import sys
import numpy as np
import cv2

class LoadData(Resource):
    def post(self):
        pass