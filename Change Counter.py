from tkinter import *
import os
import sys

# create the entry fields
fields = ('Dollar Coin', 'Half Dollar', 'Quarter', 'Dime', 'Nickel', 'Penny', 'Dollar Coin Value $',
          'Half Dollar Value $', 'Quarter Value $', 'Dime Value $', 'Nickel Value $', 'Penny Value $', 'Total Value $')


# calculate the values
def final_values(entries):
    dc = (float(entries['Dollar Coin'].get()))
    hd = (float(entries['Half Dollar'].get()))
    q = (float(entries['Quarter'].get()))
    n = (float(entries['Nickel'].get()))
    d = (float(entries['Dime'].get()))
    p = (float(entries['Penny'].get()))
    tag = 1
    if q < 0:  # check for negative values
        entries['Quarter'].insert(0, 'Error! Negative value detected')
        q = 0
        tag = 0

    if d < 0:
        entries['Dime'].insert(0, 'Error! Negative value detected')
        d = 0
        tag = 0

    if n < 0:
        entries['Nickel'].insert(0, 'Error! Negative value detected')
        n = 0
        tag = 0

    if p < 0:
        entries['Penny'].insert(0, 'Error! Negative value detected')
        p = 0
        tag = 0

    if dc < 0:
        entries['Dollar Coin'].insert(0, 'Error! Negative value detected')
        dc = 0
        tag = 0

    if hd < 0:
        entries['Half Dollar'].insert(0, 'Error! Negative value detected')
        hd = 0
        tag = 0

    if (tag == 0):  # check whether any of the coin number is negative
        dc = hd = q = n = p = d = 0

    # Compute the values
    DollarCoin_value = 1.00 * dc
    HalfDoll_value = .5 * hd
    Quarter_value = .25 * q
    Penny_value = 0.01 * p
    Dime_value = 0.1 * d
    Nickel_value = 0.05 * n
    Total_value = Quarter_value + Penny_value + Dime_value + Nickel_value + DollarCoin_value + HalfDoll_value

    # insert the computed values
    entries['Dollar Coin Value $'].delete(0, END)
    entries['Dollar Coin Value $'].insert(0, DollarCoin_value)
    entries['Half Dollar Value $'].delete(0, END)
    entries['Half Dollar Value $'].insert(0, HalfDoll_value)
    entries['Quarter Value $'].delete(0, END)
    entries['Quarter Value $'].insert(0, Quarter_value)
    entries['Dime Value $'].delete(0, END)
    entries['Dime Value $'].insert(0, Dime_value)
    entries['Nickel Value $'].delete(0, END)
    entries['Nickel Value $'].insert(0, Nickel_value)
    entries['Penny Value $'].delete(0, END)
    entries['Penny Value $'].insert(0, Penny_value)
    entries['Total Value $'].delete(0, END)
    entries['Total Value $'].insert(0, Total_value)


# create entry form
def makeform(root, fields):
    entries = {}
    for field in fields:
        row = Frame(root)
        row.configure(background='lavender')
        lab = Label(row, width=22, text=field + ": ", anchor='w')
        lab.configure(background='lavender')
        ent = Entry(row)
        ent.configure(background='seagreen')
        ent.insert(0, "0")
        row.pack(side=TOP, fill=X, padx=5, pady=5)
        lab.pack(side=LEFT)
        ent.pack(side=RIGHT, expand=YES, fill=X)
        entries[field] = ent
    return entries


def fetch(variables):
    for variable in variables:
        print
        'Input => "%s"' % variable.get()


# Restart program
def restart():
    python = sys.executable
    os.execl(python, python, *sys.argv)


if __name__ == '__main__':
    root = Tk()
    root.wm_title("Pocket Change Counter")
    root.configure(background='orange')

    w = Label(root, text="Enter number of coin type, then hit Compute:")
    w.configure(background='blanched almond')
    w.pack()

    ents = makeform(root, fields)

    root.bind('<Return>', (lambda event, e=ents: fetch(e)))

    # Compute Button
    b1 = Button(root, fg='black', text='Compute',
                command=(lambda e=ents: final_values(e)))
    b1.pack(side=TOP, padx=5, pady=5)

    # Reset Button
    b2 = Button(root, fg='red', text='Restart', command=restart)
    b2.pack(side=BOTTOM, padx=5, pady=5)

    root.mainloop()
