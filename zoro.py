from tkinter import *

#Tk
def winTk(title,bg,w,h):
    root = Tk()
    root.title(title)
    root.config(bg=bg)
    root.geometry(str(w) + "x" + str(h))
    return root
def titleTk(root,title):
    root.title(title)
def bgTk(root,bg):
    root.config(bg=bg)
def geoTk(root,w,h):
    root.geometry(str(w) + "x" + str(h))
def labelTk(root,text,bg,fg,font,row,col):
    lbl = Label(root,text=text,bg=bg,fg=fg,font=font)
    lbl.grid(row=row,column=col)
    return lbl
def textLblTk(lbl,text):
    lbl["text"] = text
def bgLblTk(lbl,bg):
    lbl["bg"] = bg
def fgLblTk(lbl,fg):
    lbl["fg"] = fg
def fontLblTk(lbl,font):
    lbl["font"] = font
def posLblTk(lbl,row,col):
    lbl.grid(row=row,column=col)
def buttonTk(root,text,bg,fg,font,width,height,row,col,com):
    btn = Button(root,text=text,bg=bg,fg=fg,font=font,command=com)
    btn.config(width=width,height=height)
    btn.grid(row=row,column=col)
    return btn
def textBtnTk(btn,text):
    btn["text"] = text
def bgBtnTk(btn,bg):
    btn["bg"] = bg
def fgBtnTk(btn,fg):
    btn["fg"] = fg
def fontBtnTk(btn,font):
    btn["font"] = font
def posBtnTk(btn,row,col):
    btn.grid(row=row,column=col)
def commandBtnTk(btn,com):
    btn["command"] = com
def inputTk(root,bg,fg,font,width,row,col):
    inp = Entry(root,bg=bg,fg=fg,font=font,width=width)
    inp.grid(row=row,column=col)
    return inp
def bgInpTk(inp,bg):
    inp["bg"] = bg
def fgInpTk(inp,fg):
    inp["fg"] = fg
def fontInpTk(inp,font):
    inp["font"] = font
def widthInpTk(inp,width):
    inp["width"] = width
def posInpTk(inp,row,col):
    inp.grid(row=row,column=col)
def getInpTk(inp):
    inp.get()

#Data
def openData(file):
    ofd = open(file,"r").read()
    return ofd
    








    



    
