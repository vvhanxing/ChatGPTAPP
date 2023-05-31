from flask import Flask, send_file, Response, send_from_directory
from flask import jsonify,request,render_template
import io
import re
import json
import getGPTAPI 
# from baidu import  getbdaudio
import getAudio
import wave
app = Flask(__name__)

@app.route("/hello",methods = ["GET","POST"])
def sayhi():
    return "hello"

@app.route("/chat/",methods = ["GET","POST"])
def chat():
    getGPTAPI.messages =[
        {"role": "system", "content": "You are a helpful assistant."},
    ]
    return render_template("index.html")

@app.route("/openai/",methods = ["GET","POST"])
def openai():
    j = request.get_json()
    
    message = {"role": "user", "content": j["content"][0]}
    gptResponse = getGPTAPI.chat_response(message)["content"]
    print(gptResponse)
    #getbdaudio.read_text(gptResponse,1,'audio')
    getAudio.text2voice(gptResponse)
    print("return string")
    return  gptResponse.replace("\n","<br>")  

@app.route('/audio/mp3')
def stream_mp3():
    audio_file = 'static\\ioutput.mp3'
    return send_file(audio_file, mimetype='audio/mpeg')


@app.route('/upload', methods=['POST',"PUT"])
def upload():
    # audio_data = request.get_data()
    # print(audio_data)
    # #保存音频数据到WAV文件
    # with wave.open("audio.wav", "wb") as wav_file:
    #     wav_file.setnchannels(1)
    #     wav_file.setsampwidth(2)
    #     wav_file.setframerate(44100)
    #     wav_file.writeframes(audio_data)

    
    # with open('recorded_audio.wav', 'wb') as file:
    #     file.write(audio_data)
    # return 'Audio recorded and saved successfully'

    data  =request.data
    print(data)
    file_path = "received.wav"
    with open(file_path, 'wb') as file:
        file.write(data)
    # if 'file' not in request.files:
    #     return 'No file uploaded'
    
    # file = request.files['file']
    # if file.filename == '':
    #     return 'No file selected'
    
    # file.save('received.wav')
    return 'File uploaded successfully'

   

if __name__ == '__main__':
    app.run(host="192.168.43.185",port=5000 ,debug=True)

