import requests
# Flask服务器的URL
url = 'http://192.168.43.185:5000/upload'
def putvoice():
    file_path = "hello.wav"
    # 创建一个multipart/form-data格式的请求
    files = {'file': open(file_path, 'rb')}

    # 发送POST请求
    response = requests.post(url, files=files)
    print(response.headers)

    # 检查响应
    if response.status_code == 200:
        print('文件上传成功！')
    else:
        print('文件上传失败！')




import json

# Azure语音转文本服务的终结点和密钥
endpoint = 'https://eastasia.api.cognitive.microsoft.com/sts/v1.0/issuetoken'
subscription_key = 'f7d5f5c932f7444d9a93565ac5da672c'


# 发送音频文件进行语音转文本
def convert_audio_to_text(audio_file):
    url = endpoint 
    headers = {
        'Content-Type': 'audio/wav',
        'Ocp-Apim-Subscription-Key': subscription_key
    }

    with open(audio_file, 'rb') as file:
        audio_data = file.read()

    response = requests.post(url, headers=headers, data=audio_data)

    if response.status_code == 200:
        print(200)
        print("---------------",response.text)
        # response_json = response.json()
        # print("---------------",response_json)
        # return response_json['DisplayText']
    else:
        print(f"Request failed with status code {response.status_code}")
        return None
if __name__ =="__main__":
    # 执行语音转文本

# 待转换的音频文件路径
    audio_file_path ='output.wav'    
    transcribed_text = convert_audio_to_text(audio_file_path)
    if transcribed_text:
        print("转换结果：", transcribed_text)
    else:
        print("转换失败")

    