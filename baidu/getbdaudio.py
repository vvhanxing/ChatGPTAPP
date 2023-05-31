from baidu.aip import AipSpeech
from pydub import AudioSegment
from pydub.playback import play
import io
""" 你的 APPID AK SK """
APP_ID = '33978795'
API_KEY = '4cIRG2q9m89a7klXIQXKSuE9'
SECRET_KEY = 'D507O71kxxufSWuNklu9bbhC8XnOgUmX'
speech = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
"""----------------------------------------------
read_text函数
输入
    text：需要读的文本
    save：是否保存成音频
    name：如果保存那保存成什么名字

输出
    直接读出音频，成功返回1
----------------------------------------------"""
def read_text(text,save = 0,name ="audio"):
    result = speech.synthesis(
    text, # UTF-8编码的文本，小于1024字节
    "zh", # zh/en
    1,)
    if not isinstance(result, dict):
        print('识别成功，正在保存音频')
        #voice = AudioSegment.from_file(io.BytesIO(result), format="mp3")
        #play(voice)
        if save:
            with open("./static/"+name+'.mp3', 'wb') as f:
                f.write(result)
        return 1
if __name__ =="__main__":
    read_text('hello,everyone',1,'audio')
