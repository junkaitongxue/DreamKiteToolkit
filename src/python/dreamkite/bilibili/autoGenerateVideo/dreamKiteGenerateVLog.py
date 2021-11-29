import os
import sys
import uuid

from moviepy.audio.fx.audio_fadein import audio_fadein
from moviepy.audio.fx.audio_fadeout import audio_fadeout
from moviepy.audio.io.AudioFileClip import AudioFileClip
from moviepy.editor import VideoFileClip, concatenate_videoclips
from moviepy.video.VideoClip import TextClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from moviepy.video.fx.fadein import fadein
from moviepy.video.fx.fadeout import fadeout

AUDIO_FADE_TIME_DURATION = 2
VIDEO_SEGMENT_FADE_TIME_DURATION = 1


def generate_video(dir_path, video_name, title=None):
    video_paths = sorted([os.path.join(dir_path, f) for f in os.listdir(dir_path) if f.endswith('.mp4')])
    print('发现视频： ', [os.path.basename(name) for name in video_paths])
    final_clip = concatenate_videoclips([fade_in_video(fade_out_video(VideoFileClip(path))) for path in video_paths[0:1]]) # 这里取一段

    audio_clip = get_audio_clip(dir_path)
    tmp_path = ''
    if audio_clip:
        sub_audio_clip = audio_clip.subclip(0, final_clip.duration)
        print("插入音频特效")
        faded_audio_clip = audio_fadein(audio_fadeout(sub_audio_clip, AUDIO_FADE_TIME_DURATION),
                                        AUDIO_FADE_TIME_DURATION)
        tmp_path = f"./{str(uuid.uuid1())}.mp3"
        faded_audio_clip.write_audiofile(tmp_path)

        sub_audio_clip.close()
        audio_clip.close()
        faded_audio_clip.close()
    audio_clip = AudioFileClip(tmp_path)

    if audio_clip:
        final_clip = final_clip.set_audio(audio_clip)

    if title:
        txt_clip = TextClip(txt=title, font='simfang.ttf', fontsize=70, color='white')
        txt_clip = txt_clip.set_position('center').set_duration(final_clip.duration)
        final_clip = CompositeVideoClip([final_clip, txt_clip])
        print('插入自定义标题成功')

    print('开始渲染出片')
    final_clip.write_videofile(f"{os.path.join(dir_path, 'output', video_name)}.mp4", threads=4)
    print('自动化剪辑成功')

    if tmp_path:
        audio_clip.close()
        os.remove(tmp_path)


def fade_out_video(video_file_clip):
    print("插入视频转场")
    return fadeout(video_file_clip, VIDEO_SEGMENT_FADE_TIME_DURATION)


def fade_in_video(video_file_clip):
    return fadein(video_file_clip, VIDEO_SEGMENT_FADE_TIME_DURATION)


def get_audio_clip(dir_path):
    for f in os.listdir(dir_path):
        if f.endswith(".mp3"):
            print('发现音频： ', f)
            return AudioFileClip(os.path.join(dir_path, f))


if __name__ == '__main__':
    if len(sys.argv) >= 2 and sys.argv[1]:
        path = sys.argv[1]
    else:
        path = r"D:\Media\bilili\myProject\自动剪辑视频\自动剪辑视频（输出）"
    generate_video(path, 'DreamKite使用代码自动剪辑的视频', "DreamKite使用代码自动剪辑的视频")
    # generate_video(r"D:\Media\bilili\myProject\自动剪辑视频", 'DreamKite自动化剪视频的延时摄影')
