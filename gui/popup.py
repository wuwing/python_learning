#-*- coding:utf-8-*-
#自定义对话窗口
import sys
from Tkinter import *
popupper = (len(sys.argv) > 1)

def dialog():
	win = Toplevel()
	Label(win,text = 'Do You Always Do What You Are Told?').pack()
	Button(win,text = 'Now click this one',command = win.destroy).pack()
	if popupper:
		win.focus_set()
		win.grab_set()
		win.wait_window()
	print 'You better obey me...'

root = Tk()
Button(root,text = 'Click me',command = dialog).pack()
root.mainloop()
