from flask_restful import Api, Resource, reqparse, request,fields, marshal_with
from flask import Response
from werkzeug.datastructures import FileStorage
import sys
import numpy as np
import cv2
import io
from io import StringIO,BytesIO
from PIL import Image
import imageio
import torch
sys.path.append("../../")
from common import code
import config
from extratool_package import api_loadImg

class LoadData(Resource):


    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('source_img', type=FileStorage, location='files',action='append')
        parser.add_argument('target_img', type=FileStorage, location='files',action='append')
        ip = request.remote_addr # "159.75.217.15"
        if ip in config.ALLOW_IPS:
            args = parser.parse_args()
            source_img_bytes = args.get('source_img')[0].read()
            target_img_bytes = args.get('target_img')[0].read() # '_io.BytesIO' object.read()
            source_img = cv2.imdecode(np.frombuffer(source_img_bytes, np.uint8), cv2.IMREAD_COLOR) # 以BGR顺序解码
            target_img = cv2.imdecode(np.frombuffer(target_img_bytes, np.uint8), cv2.IMREAD_COLOR) 
            # 查看图片
            source_img = BytesIO(source_img_bytes)
            target_img = BytesIO(target_img_bytes)
            source_img = Image.open(source_img)
            target_img = Image.open(target_img)
            source_img_test.save("./Imgs/source_img.jpg")
            
            print(source_img.shape) # h w c
            print(source_img.max()) 
            source_pimg,source_parse,source_kpt =  api_loadImg.load_img(source_img)
            target_pimg,target_parse,target_kpt = api_loadImg.load_img(target_img)
            # print(type(source_parse))
            return {'code':code.OK,'source_pimg':source_pimg.tolist(),'source_parse':source_parse.tolist(),'source_kpt':source_kpt.tolist(),'target_pimg':target_pimg.tolist(),'target_parse':target_parse.tolist(),'target_kpt':target_kpt.tolist()}

        else:
            return {'code':code.AUTHORIZATION_ERROR,'data':[],'message':"API未授权"}