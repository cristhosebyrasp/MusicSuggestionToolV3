from tkinter import *
from tkinter import messagebox
import sqlite3
import main

con = sqlite3.connect('userdata.db')
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS record(
                    name text, 
                    email text, 
                    contact number, 
                    gender text, 
                    country text,
                    password text
                )
            ''')
con.commit()
            
if __name__ == "__main__":
    ws = Tk()
    ws.title('Home Page')
    ws.geometry('940x565')
    ws.config(bg='#0bd67b')
    
f = ("Calibri", 14)

def nextPage():
    ws.destroy()
    import NEA_Navigation_Program_3

def prevPage():
    ws.destroy()
    import NEA_Navigation_Program_1
    
Label(
    ws,
    font = f,
    padx=250,
    pady=250,
    bg='#0bd67b'
    ).pack(expand=False, fill=X)

Button(
    ws, 
    text="Previous Page", 
    font=f,
    command=nextPage
    ).pack(fill=X, expand=True, side=LEFT)

Button(
    ws, 
    text="Next Page",
    font = f,
    command=prevPage
    ).pack(fill=X, expand=True, side=LEFT)

ws.resizable(False, False)
ws.mainloop()
