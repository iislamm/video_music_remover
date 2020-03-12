import sys
import os
from pathlib import Path
from moviepy.editor import VideoFileClip, AudioFileClip, AudioClip
from spleeter.separator import Separator

def remove_video_music(video_name, video_path, output_video_path, output_dir):
    '''
    @argument video_name: video name without extension
    @argument video_path: the path to the video
    @argument output_video_path: the path to including the new name of the video
    @argument output_dir: the output directory
    '''

    output_dir = str(output_dir)
    # print('*************video path: ' + video_path)
    separator = Separator('spleeter:2stems') # Setup spleeter
    video = VideoFileClip(str(video_path)) # Get the input video
    audio = video.audio # extract the audio from the input video
    # os.makedirs(output_dir) # create the directory of the output
    # write the audio file on the output directory to be used in the separtor function
    audio.write_audiofile(output_dir + video_name + '.wav')
    # seperate the music from the video 
    separator.separate_to_file(output_dir + video_name + '.wav', output_dir)
    #get the audio without music
    new_audio = AudioFileClip(output_dir + video_name + '/vocals.wav')
    # # set the new music-free audio to the video
    new_video = video.set_audio(new_audio)
    # # audio_file_name = output_dir + video_name + '/vocals.wav'
    new_video.write_videofile(str(output_video_path), audio=True)
    # video.write_videofile(str(output_video_path), temp_audiofile=audio_file_name, remove_temp=True, codec="libx264", audio_codec="aac")

if __name__ == "__main__":
    pass
