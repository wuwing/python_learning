#-*-coding:utf-8-*-
import Tkinter
from Tkinter import *
root = Tk()

widget = Label(root)
widget.config(text = 'Gui!')
widget.pack(side = LEFT, expand = YES, fill = BOTH)
root.mainloop()
#组件先创建然后在进行配置
