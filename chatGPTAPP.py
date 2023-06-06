from flask import Flask, send_file, Response, send_from_directory
from flask import jsonify,request,render_template
import io
import re
import json
import getGPTAPI 
# from baidu import  getbdaudio
import getAudio
import speak
import voice2text
import wave
import requests
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
    #getAudio.text2voice(gptResponse)
    print("return string")
    return  gptResponse#.replace("<br>","")  


@app.route("/copilot/",methods = ["GET","POST"])
def copilot():
    j = request.get_json()
    print()
    message = {"role": "user", "content": j["content"][0]}
    url = 'https://semantickernalapi.azurewebsites.net/Chat'
    data = {
    "content": j["content"][0]
    }
    print('data',data)
    headers = {"Content-Type": "application/json"}
    #dic["info"]=  " "*i+"""ChatGPT4 is great,I love openAI !"""
    response = requests.post(url, json=data,headers= headers)
    print(response.json())
    print("return string")
    content  = response.json()["content"]
    return  content


@app.route('/audio/mp3')
def stream_mp3():
    audio_file = 'static\\music2.mp3'
    return send_file(audio_file, mimetype='audio/mpeg')


@app.route('/file')
def stream_file():
    audio_file = 'static\\record_voice.py'
    return send_file(audio_file, mimetype='audio/mpeg')


@app.route('/esp32upload', methods=['POST',"PUT"])
def esp32upload():


    data  =request.data
    print(data)
    file_path = "static\\received.wav"
    with open(file_path, 'wb') as file:
        file.write(data)

@app.route('/upload', methods=['POST',"PUT"])
def upload():


    data  =request.data
    print(data)
    print(">>>>>>>>>>>>1")
    file_path = "static\\received.wav"
    file = request.files['file']
    print(">>>>>>>>>>>>2")
    file.save(file_path)
    print(">>>>>>>>>>>>3")
    converted_text = speak.recognize_from_voice(file_path)
    print(">>>>>>>>>>>>4")
    print("-------------",converted_text)
    url = "http://192.168.43.185:5000/openai/"
    headers = {"Content-Type":"application/json"}
    response = requests.post(url = url,headers=headers,json = {"content":[converted_text]})#询问GPT
    gptResponseText = response.text
    print(gptResponseText)
    audio_file = getAudio.text2voice(gptResponseText)
    print(audio_file)
    return send_file(audio_file, mimetype='audio/mpeg')

   

if __name__ == '__main__':
    app.run(host="192.168.43.185",port=5000 ,debug=True)  # 172.20.10.7
    #app.run(host="172.20.10.7",port=5000 ,debug=True) 

