from flask import request, Flask
from flask_smorest import Blueprint, abort, Api
from flask.views import MethodView
from PIL import Image
from datetime import datetime
from Data import Data
import time
from search import Search
import numpy as np
import json

data = Data()
Search = Search()

blp = Blueprint("Search Endpoint", __name__, description="send image as input and return ID's of similarity photos.")


@blp.route("/image_search")
class SearchEP(MethodView):
    def post(self):
        file = request.files['image']
        if not file:
            return

        # Save query image
        st = time.time()

        img = Image.open(file.stream)  # PIL image
        # uploaded_img_path = data.uploaded_path + '/' + datetime.now().isoformat().replace(":",
        #                                                                                   ".") + "_" + file.filename
        # img.save(uploaded_img_path)

        # Run search
        try:
            ids, dists = Search.search(img)
            paths = [data.imgs_path + '/' + str(id) + '.jpg' for id in ids]
            scores = [x for x in zip(dists, paths, ids)]
            imgs_id = [i[2] for i in scores]

            et = time.time()
            return imgs_id, 201
        except:
            return 'make sure the image in .jpg format'
        # else:
        #     abort(404, message="upload a jpg photo with english name or number.")

