from tkinter import *
# tkinter.NoDefaultRoot()

win1 = Tk()        
frame1=Frame(win1)

def functions(gui):
	win2 = Tk()
	frame2=Frame(win2)
	Button(frame2, text='Button 2', command=print(gui)).grid(row=0, column=0)
	frame2.pack()

Button(frame1, text='Button 1', command=functions("cas")).grid(row=0, column=0)

frame1.pack()

	

win1.mainloop()