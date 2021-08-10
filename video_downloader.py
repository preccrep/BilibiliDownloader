import requests
import re
import json

bvid = "1iU4y1a7LC"  # bvid of the video

headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36","referer": "https://message.bilibili.com/"
}

def send_request(url):
    response = requests.get(url=url, headers=headers)
    return response

def get_video_data(html_data):
    title = re.findall('<title data-vue-meta="true">(.*?)</title>',html_data)[0].replace("_哔哩哔哩 (゜-゜)つロ 干杯~-bilibili","")
    json_data = re.findall(r'<script>window.__playinfo__=(.*?)</script>',html_data)[0]
    json_data = json.loads(json_data)
    audio_url = json_data["data"]["dash"]["audio"][0]["backupUrl"][0]
    video_url = json_data["data"]["dash"]["video"][0]["backupUrl"][0]
    video_data = [title, audio_url, video_url]
    return video_data

def save_data(file_name,audio_url,video_url):
    print("正在下载 " + file_name + "的音频...")
    audio_data = send_request(audio_url).content
    print("完成下载 " + file_name + "的音频！")
    print("正在下载 " + file_name + "的视频...")
    video_data = send_request(video_url).content
    print("完成下载 " + file_name + "的视频！")
    with open(file_name + ".mp3", "wb") as f:
        f.write(audio_data)
    with open(file_name + ".mp4", "wb") as f:
        f.write(video_data)

html_data = send_request("https://www.bilibili.com/video/BV" + bvid).text
video_data = get_video_data(html_data)
save_data(video_data[0],video_data[1],video_data[2])
