import os
from flask import Flask, request, jsonify
from flask_cors import CORS

from thresholding import apply_adpt_thr


app = Flask(__name__)
CORS(app)


@app.route('/index', methods=['GET'])
def main():
    return 'Up and Running'


@app.route('/adaptive', methods=['POST'])
def adaptive_thresholding():
    if request.data:
        data = request.json['imageData']
        _, img = data.split(',')
        # call function for adaptive thresholding
        resp_img = apply_adpt_thr(img)

    return jsonify({'outputImage': resp_img.decode('utf-8')})


if __name__ == '__main__':
    app.run()
