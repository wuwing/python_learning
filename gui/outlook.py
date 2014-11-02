#-*- coding:utf-8-*-
import Tkinter
from Tkinter import *
root = Tk()
labelfont = ('times',24,'italic') # set the familiy,size and style

widget = Label(root, text = 'Eat At Joes')
#widget.config(bg = 'black', fg = 'red')
widget.config(bg = 'black', fg = 'red', bd = 5,relief = 'raised', cursor = 'cross')
#bd:border 边框宽度 relief 边框样式 cursor 光标悬浮时显示的形状 

widget.pack(expand = YES, fill = BOTH)
root.mainloop()
