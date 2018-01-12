from PIL import ImageGrab
from PIL import Image
import win32gui
import pytesseract
import requests
import webbrowser
from lxml import etree
import threading

def getWindowCapture(title,filename):#需要加入异常处理 窗口未打开等
    Parent_title = title
    Parent_class = None
    Phandle = win32gui.FindWindow(Parent_class,Parent_title)
    ChildHandleList = []
    win32gui.EnumChildWindows(Phandle, lambda Phandle, param: param.append(Phandle),ChildHandleList)
    Chandle = ChildHandleList[0]
    location = win32gui.GetWindowRect(Chandle)
    im = ImageGrab.grab(bbox=location)
    im.save(filename)

def cutPicture(filename):
    img = Image.open(filename)

    questionRegion=(30,130,490,220)
    newpic = img.crop(questionRegion)
    newpic.save(filename.split(".")[0]+"Q.png")

    option1Reagion=(50,250,450,290)
    option1Pic = img.crop(option1Reagion)
    option1Pic.save(filename.split(".")[0]+"S1.png")

    option2Reagion = (50,310, 450, 350)
    option2Pic = img.crop(option2Reagion)
    option2Pic.save(filename.split(".")[0] + "S2.png")

    option3Reagion = (50, 370, 450, 410)
    option3Pic = img.crop(option3Reagion)
    option3Pic.save(filename.split(".")[0] + "S3.png")

def picToText(filename):
    pytesseract.pytesseract.tesseract_cmd = r''#设置ORC程序位置
    tessdata_dir_config = '--tessdata-dir ""'#设置词包的位置
    Q_rawstr = pytesseract.image_to_string(Image.open(filename.split(".")[0]+"Q.png"), lang='chi_sim',
                                        config=tessdata_dir_config)
    S1_rawstr = pytesseract.image_to_string(Image.open(filename.split(".")[0]+"S1.png"), lang='chi_sim',
                                        config=tessdata_dir_config)
    S2_rawstr = pytesseract.image_to_string(Image.open(filename.split(".")[0]+"S2.png"), lang='chi_sim',
                                        config=tessdata_dir_config)
    S3_rawstr = pytesseract.image_to_string(Image.open(filename.split(".")[0]+"S3.png"), lang='chi_sim',
                                        config=tessdata_dir_config)
    Q_str=S1_str=S2_str=S3_str=''
    for i in range(len(Q_rawstr)):
        if Q_rawstr[i] != ' ' and Q_rawstr[i] != '\n':
            Q_str += Q_rawstr[i]
    for i in range(len(S1_rawstr)):
        if S1_rawstr[i] != ' ' and S1_rawstr[i] != '\n':
            S1_str += S1_rawstr[i]
    for i in range(len(S2_rawstr)):
        if S2_rawstr[i] != ' ' and S2_rawstr[i] != '\n':
            S2_str += S2_rawstr[i]
    for i in range(len(S3_rawstr)):
        if S3_rawstr[i] != ' ' and S3_rawstr[i] != '\n':
            S3_str += S3_rawstr[i]
    return (Q_str.split('.')[1],S1_str,S2_str,S3_str)

def search(question):
    print(question)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
    }
    url1 = "https://www.baidu.com/s?wd="
    url2="https://www.baidu.com/s?wd=allintitle:"#多关键词精确搜索
    # chrome = webbrowser.get('chrome')
    webbrowser.open(url1+question[0])
    for i in range(3):
        response = requests.get(url=url1+question[0]+' '+question[1+i],headers=headers)
        html = etree.HTML(response.text)
        result = html.xpath('//*[@id="container"]/div[2]/div/div[2]/text()')
        print(question[1+i],result[0])
        # print(url1+question[0]+' '+question[1+i])

if __name__ == '__main__':
    picname = "a.png"
    getWindowCapture("",picname)#程序窗口标题
    cutPicture(picname)
    question = picToText(picname)
    search(question)