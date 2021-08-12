import tkinter

top = tkinter.Tk()
img = tkinter.PhotoImage(file='pig.gif')
label1 = tkinter.Label(image=img, height=390, width=330)
label1.pack()
top.mainloop()
