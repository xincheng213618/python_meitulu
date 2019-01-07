import requests,re,os

def xdowmload():
    url = "https://www.meitulu.com/t/xiameijiang/"
    r = requests.get(url)
    r.encoding = 'utf-8'
    reg1 = re.compile('<a href="(.*?)" target="_blank"><img')
    reg2 = re.compile('target="_blank">(.*?)</a></p>')
    urls1 = re.findall(reg1,r.text)
    urls2 = re.findall(reg2,r.text)
    z=0
# def get_img(urls):
    for u in urls1:
        imgid = u.split('/')[-1][:-5]
        for i in range(1,50):
            imgurl = "https://mtl.ttsqgs.com/images/img/{}/{}.jpg".format(imgid,i)
            headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0',
                    'Referer':'https://www.meitulu.com/img.html?img='+imgurl}
            r = requests.get(imgurl,headers=headers)
            path = "C:\搜狗高速下载\夏美酱\ "+urls2[z]+'/'
            if not os.path.exists(path):
                os.makedirs(path)
            with open(path+imgurl.split('/')[-1],'wb') as ff:
                ff.write(r.content)
        z = z + 1




if __name__ == '__main__':

    xdowmload()
