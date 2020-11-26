from tkinter import *
from tkinter import messagebox

litha = Tk()
litha.geometry("600x250")
litha.title('Lotto App')
litha.configure(background='#3E464A')


# function
def age_limit():
    ent = entry_lim.get()
    ent1 = int(ent)
    if ent1 < 18:
        messagebox.showerror('YOUR TOO YOUNG TO PLAY', 'You cannot play Fuck Off!!')
        entry_lim.delete(0, END)
    else:
        messagebox.showinfo('WELCOME TO THE LOTTO WEEKLY DRAW', "Let's Play")
        litha.destroy()
        import LOTTO
        LOTTO.popup()


# labels& entries
age = IntVar()

heading = Label(litha, text='LOTTO DRAW LOGIN', font='arial 20 bold', fg='white', bg='#3E464A')
heading.pack(pady=5)

entry_log = Label(litha, text="Are you 18 & Above Of Age?\n (Please enter your age)", font='arial 15 bold',
                  fg='#3190C7', bg='#3E464A')
entry_log.pack(pady=5)
entry_lim = Entry(width=17, textvariable=age)
entry_lim.pack(pady=10)

myButton = Button(litha, text="LOGIN", width=15, background='#f2c831', command=age_limit)
myButton.pack()

litha.mainloop()
