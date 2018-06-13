'''
    2 request 请求模块
    1 创建对象request
    2 定义函数，获的所搜中输入的关键z字
    3 将关键字进行字典话，加入到百度请求中
    4 将返回结果输出到一个html文件中

'''

import requests

class my_request(object):
    def __init__(self,key_word,count="10"):
        '''初始化，并开始请求数据'''
        self.key_word=key_word
        self.count=count
        self.payload={"wd":key_word,"pn":self.count}
        self.repon=requests.get("http://www.baidu.com/s",params=self.payload)
        self.repon.encoding="utf-8"

    def write_html(self):
        '''将请求的数据写到文件中'''
        with open("response_baidu.html","w",encoding="utf-8") as f:
            for text in self.repon.text.split():
                if  not text.isspace():
                    f.write(text+"\n")




if __name__ =="__main__":
    mr=my_request("王昭君","10")
    mr.write_html()

