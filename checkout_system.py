from tkinter import *
import cv2
import os
import datetime
from dateutil.parser import parse

#待優化項目： 按確認不會一直跑東西出來QQ
#使用前請先確認imgFolderPath是圖片放置區／carinfoobject取的路徑是資訊放置處
#時間格式範例： 2019-05-08 23:58:09

imgFolderPath = "C:\\Users\\ASUS\Pictures\\"   #放檔案資料夾路徑
    #---------------------處理車牌TXT資料-----------#
carinfoobject = open(r"C:\Users\ASUS\Documents\CARINFO\carinfo.txt","r")
carinfodict = {}
carinfo = carinfoobject.readline()

while carinfo != "":
    carinfolist = carinfo.split(",")
    carinfolist[1] = carinfolist[1].replace("\n","")
    carinfodict[carinfolist[0]] = carinfolist[1]
    carinfo = carinfoobject.readline()
carinfoobject.close()
print(carinfodict)
print("carinfo檔案處理完成")


class Checkout():
    def reset(self):#
        self.e1.delete(0,END)
    def searchagain(self):
        self.l2.pack_forget()
        self.b3.pack_forget()
        self.l3.pack_forget()
        self.l4.pack_forget()
        
    def confirm(self):#
        boardnum = self.board.get()
        if not os.path.exists(imgFolderPath+boardnum+".jpg"):
            print("找不到您的車牌！請重新輸入！")
        if os.path.exists(imgFolderPath+boardnum+".jpg"):
            self.l2 = Label(self.checkout, text = "\n您的車牌號碼是 " + boardnum)
            self.l2.pack()
            self.l3 = Label(self.checkout, text = "入場時間: " + carinfodict[boardnum])
            self.l3.pack()
            now = datetime.datetime.now()
            self.currentTime = str(now.strftime("%Y-%m-%d %H:%M:%S"))
            self.l4 = Label(self.checkout, text = "離場時間: " + self.currentTime)
            self.l4.pack()
            fee = self.fee()
            self.l5 = Label(self.checkout, text = "費用" + str(fee) + "元")
            self.l5.pack()
            self.b3 = Button(self.checkout, text = "重新查詢", command = self.searchagain)
            self.b3.pack()
            
    def fee(self):###########################################
        fee = 0
        boardnum = self.board.get()
        #========分析入場時間==========#
        entertime = carinfodict[boardnum]###########
        tmpe = entertime.split(" ")
        eyear,emonth,eday = self.parseDate(tmpe[0])#tmp[0]放的是日期
        ehour,eminute,esecond = self.parseTime(tmpe[1])
        
        #=========擷取離場時間========#
        tmpl= self.currentTime.split(" ")
        lyear, lmonth, lday = self.parseDate(tmpl[0])
        lhour, lminute, lsecond = self.parseTime(tmpl[1])
        
        #==========計算費用============#
        
        enter = datetime.datetime(eyear, emonth, eday, ehour, eminute, esecond)
        leave = datetime.datetime(lyear, lmonth, lday, lhour, lminute, lsecond)
        
        
        hour = int(lhour) - int(ehour)
        minute = int(lminute) - int(eminute)
        second = int(lsecond) - int(esecond)
        
        day = (leave - enter).days
        if (day > 0):
            fee = day * 24 * 40 + (24-int(ehour))*40 + int(lhour)*40
        elif (day == 0):
            fee = hour*40
        return fee
        
    def parseDate(self,date):
        tmp = date.split("-")
        year = tmp[0]
        month = tmp[1]
        day = tmp[2]
        return int(year), int(month), int(day)
    def parseTime(self,time):
        tmp = time.split(":")
        hour = tmp[0]
        minute = tmp[1]
        second = tmp[2]
        return int(hour), int(minute), int(second)
        
        
    def __init__(self):
        self.checkout = Tk()
        self.checkout.geometry("700x450")
        self.checkout.maxsize(700,450)
        self.checkout.title("停車繳費系統")
    
        self.l1 = Label(self.checkout, text = "\n\n請輸入您的車牌號碼\n")
        self.l1.pack()
        self.board = StringVar()
        self.e1 = Entry(self.checkout,textvariable = self.board)
        self.e1.pack()
        
        self.b1 = Button(self.checkout, text = "確認",command = self.confirm)
        self.b1.pack()
        self.b2 = Button(self.checkout, text = "重設", command = self.reset)
        self.b2.pack()
        self.checkout.mainloop()
        


ck = Checkout()
    
