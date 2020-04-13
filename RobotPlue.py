# -*- coding: utf-8 -*-
import requests
import json
import time
import hmac
import hashlib
import base64
from urllib import parse
class postmsg():   
    def setV(self):#初始化参数
        self.delaycc=True
    def txtwebhook(self,a,webhook,at1,at2,at3,atall,keyword):#发送函数
        if keyword!="":
            tex = "["+keyword+"]:"+a
        else: 
            tex=a
        message ={

            "msgtype": "text",
            "text": {
                "content": tex
            },
            "at": {
            "atMobiles": [#@的具体用户
                at1,at2,at3
            ],
            "isAtAll": atall  #此处为是否@所有人
            }

        }

        
        #构建请求头部
        header = {
            "Content-Type": "application/json",
            "Charset": "UTF-8"
        }
        
        #对请求的数据进行json封装
        message_json = json.dumps(message)
        #发送请求
        '''
        for x in range(b):
        
            c-=1
            print("Countdown:",c)
            time.sleep(1)
        '''
        info = requests.post(url=webhook,data=message_json,headers=header)
        #打印返回的结果
        print("错误信息:",info.text)
        self.Error=info.text
        

    def addticket(self,wh,secret):#加签验证函数
        print("加签中")
        timestamp= int(time.time() * 1000)
        secret_enc = bytes(secret.encode('utf-8'))
        string_to_sign = '{}\n{}'.format(timestamp, secret)
        string_to_sign_enc = bytes(string_to_sign.encode('utf-8'))
        hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
        sign = parse.quote(base64.b64encode(hmac_code), safe='')
        print("时间戳=",timestamp)
        print("签名=",sign)
        #https://oapi.dingtalk.com/robot/send?access_token=XXXXXX&timestamp=XXX&sign=XXX
        return wh+"&timestamp="+str(timestamp)+"&sign="+sign
    def delay(self,isevery,t):#延时发送
        b=t
        c=t
        if isevery:
            for x in range(b):
                c-=1
                print("Countdown:",c)
                time.sleep(1)
        elif self.delaycc:
            self.delaycc=False
            for x in range(b):
                c-=1
                print("Countdown:",c)
                time.sleep(1)

    def returnError(self):#错误信息解析
        if self.Error=='{"errcode":0,"errmsg":"ok"}':
            print("消息发送成功")
        elif self.Error=='{"errcode":310000,"errmsg":"invalid timestamp"}':
            print("消息发送失败:加签-timestamp 时间戳无效")
        elif self.Error=='{"errcode":310000,"errmsg":"sign not match"}':
            print("消息发送失败:加签-sign签名不匹配")
        elif self.Error=='{"errcode":310000,"errmsg":"keywords not in content"}':
            print("消息发送失败:消息内容中不包含任何关键词")
        elif self.Error=='{"errcode":400004,"errmsg":"群主已开启仅群主可@所有人功能"}':
            print("消息发送失败:群主已开启仅群主可@所有人功能")
        elif self.Error=='{"errcode":300001,"errmsg":"token is not exist"}':
            print("消息发送失败:Webhook接口不存在")
        else: 
            print("消息发送失败:IP地址不在白名单")
        
    
    def suo(self,longw,key,expDate) :
        
        if expDate=="":
            expDate="9999-12-31"
        
        API="http://suo.im/api.htm?url=" +parse.quote(longw) + "&key=" + key +"&expireDate=" + expDate
        info = requests.get(API)
        print(info.text)
        return info.text   
    def linkwebhook(self,title,text,webhook,PicUrl,MsgUrl,keyword):#发送函数
        header = {
            "Content-Type": "application/json",
            "Charset": "UTF-8"
        }
        if keyword!="":
            tex = "["+keyword+"]:"+text
        else: 
            tex=text
        message ={
            "msgtype": "link", 
            "link": {
            "text": tex, 
            "title": title, 
            "picUrl": PicUrl, 
            "messageUrl": MsgUrl
            }
        }
        #对请求的数据进行json封装
        message_json = json.dumps(message)
        #发送请求
        info = requests.post(url=webhook,data=message_json,headers=header)
        #打印返回的结果
        print("错误信息:",info.text)
        self.Error=info.text
        self.returnError()
        