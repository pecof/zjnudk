# coding=utf-8
import time
import requests
import datetime
import os
import logging
import sys
if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')

FILE = os.getcwd()
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(filename=os.path.join(FILE,'log.txt'),level=logging.INFO, format=LOG_FORMAT)

def main():
    # sign_time = 30   # 表示 十点十分 开始发起签到
    # time_now = int(str_time("%H%M"))
    # print(time_now)
    # while time_now < sign_time:
    #     logging.info('未到指定的签到时间')
    #     time.sleep(3600)
    #     time_now = int(str_time("%H%M"))
    username = ('peco')
    data = "你抓的post内容"
    cookies = '''你抓的cookie'''

    sign_res = sign_in(data,cookies)
    logging.info(username+"开始提交")
    if sign_res != "":
        if sign_res.find("提交成功！已经返校师生，若腋下体温≥37.3℃，请到“体温填报”模块填写具体体温！")!=-1:
            logging.info(username+"提交成功")

def sign_in(data,cookie):
    url = "http://zyt.zjnu.edu.cn/H5/ZJSFDX/CheckFillIn.aspx"
    url = "http://zyt.zjnu.edu.cn/H5/ZJSFDX/FillIn.aspx"
    try:
        headers = {
            "Cookie": cookie,
            "content-type": "application/x-www-form-urlencoded",
            "Referer": "http://zyt.zjnu.edu.cn/H5/ZJSFDX/FillIn.aspx"
        }
        response=requests.post(url,headers=headers,data=data,timeout=(2, 30))  #timeout(2, 30)表示的连接时间是2，响应时间是30
        response.encoding = response.apparent_encoding
        print(response.text)
        return response.text
    except requests.exceptions.ReadTimeout:
        print("requests.exceptions.ReadTimeout:[%s]" % url)
        return ""
    except requests.exceptions.ConnectionError:
        print("requests.exceptions.ConnectionError:[%s]" % url)
        return ""

def str_time(pattern='%Y-%m-%d %H:%M:%S'):
    return time.strftime(pattern, time.localtime(time.time()))
if __name__ == "__main__":
    main()
