from tkinter import *
from tkinter import messagebox

litha = Tk()
litha.geometry("700x500")
litha.title('Lotto App')
litha.configure(background='#212112')


# function
def age_limit():
    ent = entry_lim.get()
    ent1 = int(ent)
    if ent1 < 18:
        messagebox.showerror('YOUR TOO YOUNG TO PLAY', 'You cannot play Fuck Off!!')
        entry_lim.delete(0, END)
    else:
        messagebox.showinfo('WELCOME TO THE LOTTO WEEKLY DRAW', "Let's Play")
        litha.withdraw()
        import LOTTO
        LOTTO.popup()


# labels& entries
age = IntVar()

heading = Label(litha, text='- LOTTO DRAW LOGIN -', font='times 25 bold underline', fg='#f9f92f', bg='#212112')
heading.pack(pady=10)

entry_log = Label(litha, text="Are you 18 & Above Of Age?\n (Please enter your age)", font='arial 15 bold italic',
                  fg='white', bg='#212112')
entry_log.pack(pady=8)
entry_lim = Entry(width=17, textvariable=age)
entry_lim.pack(pady=15)

myButton = Button(litha, text="LOGIN", width=15, background='#f9f92f', command=age_limit)
myButton.pack(pady=30)

info = Label(litha, text="Litha Kane Holdings RF (Proprietary) Limited", font='arial 9 ',
             fg='white', bg='#212112')
info.pack(pady=5)

info1 = Label(litha,
              text="All rights herein are strictly reserved. If you use this Web site you agree to the terms and "
                   "conditions in this user agreement.\n "
                   "* Estimated Jackpot - is the estimated value of the jackpot which is estimated based on tickets "
                   "sold for the particular draw on a particular game.\n "
                   "** Guaranteed Jackpot - is a set value of the Jackpot which is guaranteed for the particular draw "
                   "on a particular game", font='arial 7 ',
              fg='white', bg='#212112')
info1.pack()


litha.mainloop()
