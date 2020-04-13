# -*- coding: utf-8 -*-
from RobotPlue import * #


#定义类()
sent=postmsg()#???=postmsg()

#函数初始化
sent.setV()
#webhook地址
Robota="https://oapi.dingtalk.com/robot/send?access_token=XXXXXXXX"
#加签密钥
RobotaSEC="SECXXXXXXXXXXX"#选填

#循环发送(次数)
for x in range(1):
    
    #???.delay(是否在连续多次发送时每次都延时,延时的秒数)
    sent.delay(False,3)
    
    #发送模块
    #???.linkwebhook("*题目",“*文字”,*(可能需要加签)webhook地址,“图片地址”,“*链接文件地址”)
    #加签:???.addticket(Webhook地址,加签验证密钥)为加签验证发函数)
    sent.txtwebhook("TestMsg",sent.addticket(Robota,RobotaSEC),"135XXXX1732","133XXXX3114","137XXXX4314",False,"TestKeyword")
    
    #???.linkwebhook("*题目",“*文字”,*(可能需要加签)webhook地址,“图片地址”,“*链接文件地址”."关键词")
    #???.suo("*长网址",“*密钥:到suo.im注册申请”,“过期日期”)
    sent.linkwebhook("*题目","*文字",sent.addticket(Robota,RobotaSEC),sent.suo("https://xxx","XXXX","2030-3-3"),"https://xxx","TextKeyword")
    
    


    


