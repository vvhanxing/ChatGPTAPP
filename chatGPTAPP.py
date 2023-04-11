from flask import Flask, send_file, Response, send_from_directory
from flask import jsonify,request,render_template
import io
import re
import json
import getGPTAPI 
app = Flask(__name__)

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
    
    return  getGPTAPI.chat_response(message)["content"] .replace("\n","<br>")  
if __name__ == '__main__':
    app.run()

