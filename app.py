from PIL import Image
from datetime import datetime
from flask import Flask, request, render_template
from flask_smorest import Api
from resources.searchEP import blp as Searchblueprint
from Data import Data
import time

from search import Search

app = Flask(__name__)
data = Data()
Search = Search()

# flask-smorest configuration
app.config["API_TITLE"] = "Image Search Engine"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config[
        "OPENAPI_SWAGGER_UI_URL"
    ] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(app)
api.register_blueprint(Searchblueprint)


# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         file = request.files['query_img']
#
#         if not file:
#             return
#
#         # Save query image
#         st = time.time()
#
#         img = Image.open(file.stream)  # PIL image
#         # uploaded_img_path = data.uploaded_path+'/' +datetime.now().isoformat().replace(":", ".") + "_" + file.filename
#         # img.save(uploaded_img_path) # uncomment this if you want to save the file into uploaded file
#
#         # Run search
#         try:
#             ids, dists = Search.search(img)
#             paths = [data.imgs_path+'/'+str(id)+'.jpg' for id in ids]
#             scores = [x for x in zip(dists, paths, ids)]
#
#             et = time.time()
#             print(f'Excution time = {et - st} Seconds')
#             return render_template('index.html',
#                                    # query_path=uploaded_img_path,
#                                    scores=scores)
#         except:
#             return render_template('index.html',
#                                    scores=[])
#     else:
#         return render_template('index.html')
#
#
# if __name__=="__main__":
#     app.run("0.0.0.0")
