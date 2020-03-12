import os
import random
import string
from pathlib import Path

def get_video_name(video: str):
    video_ext_index = video.rfind('.')
    video_name = video[0:video_ext_index ]
    video_ext = video[video_ext_index + 1:]
    video_details = (video_name, video_ext)
    return video_details

def gen_video_path(video, dir_name):
    if not os.path.isdir('./videos'):
        os.mkdir('./videos')
        os.mkdir('./videos/user')
        os.mkdir('./videos/output')

    os.mkdir('./videos/user/' + dir_name)
    os.mkdir('./videos/output/' + dir_name)
    video_path = './videos/user/' +  dir_name + '/' + video.filename
    print('video_path' + video_path)
    return video_path

def gen_output_path(video_name, video_ext, dir_name): 
    output_video_path = './videos/output/' +  dir_name + '/' + video_name + '_no_music.' + video_ext
    output_dir = './videos/output/' +  dir_name + '/'
    return (output_video_path, output_dir)

def random_name(name_len=5):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(name_len))
