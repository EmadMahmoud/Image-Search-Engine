import os

from flask import request, send_file, Flask
from flask_smorest import Blueprint
from flask.views import MethodView
import requests
from io import BytesIO
from PIL import Image
from Data import Data
import time
from search import Search


data = Data()
Search = Search()

blp = Blueprint("Search Endpoint", __name__, description="send image as input and return ID's of similarity photos.")


@blp.route("/image_search")
class SearchEP(MethodView):
    def post(self):
        datas = request.get_json()
        image_url = datas['url']

        # to save the image locally
        response = requests.get(image_url)
        with open('image.jpg', 'wb') as file:
            file.write(response.content)



        # send the image in the request
        # file = request.files['image']
        # if not file:
        #     return
        # img = Image.open(file.stream)  # PIL image

        # Run search
        try:
            img_path = "image.jpg"
            pil_image = Image.open(img_path)
            ids, dists = Search.search(pil_image)
            paths = [data.imgs_path + '/' + str(id) + '.jpg' for id in ids]
            scores = [x for x in zip(dists, paths, ids)]
            imgs_id = [i[2] for i in scores]

            et = time.time()
            os.remove(img_path)
            return imgs_id, 201

        except:
            return 'make sure the image in .jpg format'


