from tkinter import *
import cv2
import os
import datetime

#使用前請先確認imgFolderPath是圖片放置區／carinfoobject取的路徑是資訊放置處

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
    def reset(self):
        self.e1.delete(0,END)
    def searchagain(self):
        self.l2.pack_forget()
        self.b3.pack_forget()
        self.l3.pack_forget()
        self.l4.pack_forget()
        
    def confirm(self):
        boardnum = self.board.get()
        if not os.path.exists(imgFolderPath+boardnum+".jpg"):
            print("找不到您的車牌！請重新輸入！")
        if os.path.exists(imgFolderPath+boardnum+".jpg"):
            self.l2 = Label(self.checkout, text = "\n您的車牌號碼是 " + boardnum)
            self.l2.pack()
            self.l3 = Label(self.checkout, text = "入場時間: " + carinfodict[boardnum])
            self.l3.pack()
            self.currentTime = datetime.datetime.now().time()
            self.l4 = Label(self.checkout, text = "離場時間: " + str(self.currentTime))
            self.l4.pack()
            fee = self.fee()
            self.l5 = Label(self.checkout, text = "費用" + str(fee) + "元")
            self.l5.pack()
            self.b3 = Button(self.checkout, text = "重新查詢", command = self.searchagain)
            self.b3.pack()
    def fee(self):##########################################################
        fee = 0
        boardnum = self.board.get()
        entertime = carinfodict[boardnum] #str
        entertimelist = entertime.split(":")
        leavetime = str(self.currentTime) #str
        leavetimelist = leavetime.split(":")
        hour = eval(leavetimelist[0]) - eval(entertimelist[0])
        minute = eval(leavetimelist[1]) - eval(entertimelist[1])
        if abs(minute) > 30:
            hour = abs(hour) +1
            fee = hour* 40
        else:
            fee = abs(hour) * 40
        return fee
        
        
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
    
