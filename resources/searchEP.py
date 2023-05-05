from flask import request
from flask_smorest import Blueprint
from flask.views import MethodView
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
        file = request.files['image']
        if not file:
            return

        img = Image.open(file.stream)  # PIL image

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


