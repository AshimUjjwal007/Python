from tkinter import *

win = Tk()
win.title("Table")
win.geometry("200x200+600+150")


table = StringVar()







def MulTable():
    print('\n')
    for a in range(1,11):
        b = int(table.get())
        print('\t\t',(b),'x',(a),'=',(a*b))







label = Label(win, text = "Multiplication Table", font=30, fg="black", bg ='violet')
label.pack(fill = X)

label = Label(win,text = "                                           ")
label.pack()

entry = Entry(win, text=table, justify = 'center')
entry.pack()

label = Label(win,text = "                                           ")
label.pack()


button = Button(win, text = "Submit", command = MulTable)
button.pack()

label = Label(win, text = '                                          ')
label.pack()


button1 = Button(win, text = "Quit", command = win.destroy)
button1.pack()




win.mainloop()
