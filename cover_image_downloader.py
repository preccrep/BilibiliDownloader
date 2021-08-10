import requests
import os


bvid = '1oL411p7at'  # bvid of the video
pic = '/Users/preccrep/Downloads/1.png'  # path and filename to store the image

url = 'https://api.bilibili.com/x/web-interface/view?bvid=BV' + bvid
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 \
    (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'}


html = requests.get(url=url, headers=headers).text

str = html.split(',')

flag = 0

s = ''

for i in str:
    if i[1:4] == 'pic':
        s = i[7:-1]
        # print(s)
        flag = 1
        break

def download_img(url):
    print (url)
    r = requests.get(url, headers=headers, stream=True)
    print(r.status_code) # 返回状态码
    if r.status_code == 200:
        if not os.path.exists(pic):
            os.system(r"touch {}".format(pic))
        # open(pic, 'wb').write(r.content) # 将内容写入图片
        with open(pic, 'wb') as f:
            f.write(r.content)
            f.close()
        print("done")
    del r

if flag == 0:
    print('Check your link! There appears to be some problems.')
else:
    download_img(s)

