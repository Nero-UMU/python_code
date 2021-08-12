import tkinter

top = tkinter.Tk()
top.title('thinking')
img = tkinter.PhotoImage(file='picture1.gif')
label1 = tkinter.Label(image=img, height=500, width=500)
label1.pack()
top.mainloop()
