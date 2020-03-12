import json
from flask import Flask, request, make_response, render_template, Response, send_from_directory
from flask_cors import cross_origin, CORS
from music_remover.music_remover import remove_video_music
from threading import Thread, Event
from time import sleep
from google.cloud import storage
from firebase import firebase
from music_remover.video_mngmnt import *

app = Flask(__name__)

CORS(app)

@app.route('/', methods=['GET'])
def hello_world():
    return render_template("index.html")

@app.route('/videos/<path:video_path>', methods=['GET'])
def render_video(video_path):
    print(video_path)
    return send_from_directory("videos", video_path)


@app.route('/video', methods=['POST'])
@cross_origin()
def addVideo():
    dir_name = random_name()
    print(request.files)
    video = request.files['video']
    (video_name, video_ext) = get_video_name(video.filename)
    video_path = gen_video_path(video, dir_name)
    (output_video_path, output_dir) = gen_output_path(
        video_name, video_ext, dir_name)
    print(type(video_path))
    video.save(str(video_path))
    remove_video_music(video_name, video_path, output_video_path, output_dir)
    response = Response(response=json.dumps({"video_path": output_video_path}), status=200, mimetype='application/json')
    return response


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
