#-*-coding:utf-8-*-
import sys
from Tkinter import *
widget = Button(None,text = 'Exit',command = sys.exit)
#Button指定组件类型, command为单击按钮时产生的事件
widget.pack()
widget.mainloop()
