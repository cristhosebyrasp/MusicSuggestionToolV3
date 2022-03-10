# ---------------------------------------------|
# NEA PROJECT - 2022
# Project name: "Music Suggestion Tool"
# Candidate: Abdulai Yusuf
# ---------------------------------------------|

# calling modules

import tkinter
from tkinter import *
import tkinter as tk
import sqlite3
from tkinter import messagebox
from tkinter.messagebox import showerror

# --------------Font format--------------------|

f = ("Calibri", 14)

#-------------------------------------------------------------------|
p1 = ()
p2 = ()
p3 = ()
p4 = ()
left_frame = ()
right_frame = ()

# --------Creating userdata database---------|

con = sqlite3.connect('dbases/userdata.db')
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

# -----Connecting to the track database------|

con = sqlite3.connect('dbases/track_metadata.db')
cur = con.cursor()

cur.execute('SELECT * FROM songs WHERE TITLE = "Scream"')
songs = cur.fetchall()

print(songs[0])
print(songs[0][1])


# --------Function Database---------|

def Database():
    global conn, cursor
    con = sqlite3.connect('dbases/userdata.db')
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS record(
                      name text, 
                      email text, 
                      contact number, 
                      gender text, 
                      password text
                  )
              ''')
    con.commit()


# ----------------Classe Page----------------------|

class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__()
        tk.Frame.__init__(self, *args, **kwargs)
        tk.Label(self, text='Music Suggestion Tool', fg="#FFFFFF", width=60, bg="#000000").pack()

    def show(self):
        self.lift()


# ----------------Classe Page1----------------------|

class Page1(Page):
    def __init__(self, *args, **kwargs):
        Page1 = p1
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="This is a main page")
        label.pack(side="top", fill="both", expand=True)


# ----------------Classe Page2----------------------|

class Page2(Page):
    def __init__(self, *args, **kwargs):
        Page2 = p2
        Page.__init__(self, *args, **kwargs)
        Label(
            self,
            font=f,
            padx=250,
            pady=250,
            bg='#0bd67b'
        ).pack(expand=False, fill=X)

    def insert_record():
        check_counter = 0
        warn = ""
        if register_name.get() == "":
            warn = "Name can't be empty"
        else:
            check_counter += 1

        if register_email.get() == "":
            warn = "Email can't be empty"
        else:
            check_counter += 1

        if register_mobile.get() == "":
            warn = "Contact can't be empty"
        else:
            check_counter += 1

        if var.get() == "":
            warn = "Gender"
        else:
            check_counter += 1
        if variable.get() == "":
            warn = "Select Country"
        else:
            check_counter += 1
        if register_pwd.get() == "":
            warn = "Password can't be empty"
        else:
            check_counter += 1
        if pwd_again.get() == "":
            warn = "Re-enter password can't be empty"
        else:
            check_counter += 1

        if register_pwd.get() != pwd_again.get():
            warn = "Passwords didn't match!"
        else:
            check_counter += 1

        if check_counter == 8:
            try:
                con = sqlite3.connect('dbases/userdata.db')
                cur = con.cursor()
                cur.execute("INSERT INTO record VALUES (:name, :email, :contact, :gender, :country, :password)", {
                    'name': register_name.get(),
                    'email': register_email.get(),
                    'contact': register_mobile.get(),
                    'gender': var.get(),
                    'country': variable.get(),
                    'password': register_pwd.get()
                })
                con.commit()
                messagebox.showinfo('confirmation', 'Record Saved')
            except Exception as ep:
                messagebox.showerror('', ep)
        else:
            messagebox.showerror('Error', warn)

    def login_response():
        try:
            con = sqlite3.connect('dbases/userdata.db')
            c = con.cursor()
            for row in c.execute("Select * from record"):
                username = row[1]
                pwd = row[5]

        except Exception as ep:
            messagebox.showerror('', ep)

        uname = email_tf.get()
        upwd = pwd_tf.get()
        check_counter = 0
        if uname == "":
            warn = "Username can't be empty"
        else:
            check_counter += 1
        if upwd == "":
            warn = "Password can't be empty"
        else:
            check_counter += 1
        if check_counter == 2:
            if (uname == username and upwd == pwd):
                messagebox.showinfo('Login Status', 'Logged in Successfully!')
                nextPage()

            else:
                messagebox.showerror('Login Status', 'invalid username or password')
        else:
            messagebox.showerror('', warn)

        # widgets placement
        email_tf.grid(row=0, column=1, pady=10, padx=20)
        pwd_tf.grid(row=1, column=1, pady=10, padx=20)
        login_btn.grid(row=2, column=1, pady=10, padx=20)
        left_frame.place(x=50, y=50)

        register_name.grid(row=0, column=1, pady=10, padx=20)
        register_email.grid(row=1, column=1, pady=10, padx=20)
        register_mobile.grid(row=2, column=1, pady=10, padx=20)
        register_country.grid(row=4, column=1, pady=10, padx=20)
        register_pwd.grid(row=5, column=1, pady=10, padx=20)
        pwd_again.grid(row=6, column=1, pady=10, padx=20)
        register_btn.grid(row=7, column=1, pady=10, padx=20)
        right_frame.place(x=500, y=50)

        gender_frame.grid(row=3, column=1, pady=10, padx=20)
        male_rb.pack(expand=False, side=LEFT)
        female_rb.pack(expand=False, side=LEFT)
        others_rb.pack(expand=False, side=LEFT)

        label = tk.Label(self, text="This is a login / register page")
        label.pack(side="top", fill="both", expand=False)

    # ----------------Classe Page3----------------------|


class Page3(Page):
    def __init__(self, *args, **kwargs):
        Page3 = p3
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="This is Control Panel page")
        label.pack(side="top", fill="both", expand=True)


# ----------------Classe Page4----------------------|

class Page4(Page):
    def __init__(self, *args, **kwargs):
        Page4 = p4
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="This is the control panel page")
        label.pack(side="top", fill="both", expand=True)


# ----------------Classe MainView----------------------|

class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

        p1 = Page1(self)
        p2 = Page2(self)
        p3 = Page3(self)
        p4 = Page4(self)

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p4.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = tk.Button(buttonframe, text="Main", bg= '#92d050', relief=FLAT, command=p1.show)
        b2 = tk.Button(buttonframe, text="Login", bg= '#92d050', relief=FLAT, command=p2.show)
        b3 = tk.Button(buttonframe, text="Panel", bg= '#92d050',relief=FLAT, command=p3.show)
        b4 = tk.Button(buttonframe, text="Quit", bg= '#92d050', relief=FLAT, command=exit)

        b1.pack(side="left", pady= 10, padx=20)
        b2.pack(side="left", pady= 10, padx=20)
        b3.pack(side="left", pady= 10, padx=20)
        b4.pack(side="left", pady= 10, padx=20)

        p1.show()


# ----------------End of de Classe MainView-------------------|

if __name__ == "__main__":
    root = tk.Tk()  # Makes the window
    root.title('Music Suggestion Tool')
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("940x500")
    root.config(bg="#92d050")

# ----------------------------------------------|
    # left_frame
    left_frame = Frame(root, bg="black", width=100, height=100)
    left_frame.pack(side="left",pady=0, padx=0)

    # right_frame
    right_frame = Frame(root, bg="#92d050", width=100, rown=100, height=200)
    right_frame.pack(pady=20, padx=20)
# ----------------------------------------------|
    root.mainloop()  # start monitoring and updating the GUI

# -------------------Page1 Page------------------|

if __name__ == "__main__":
    def Page1(self):
        Page1 = p1(self)
        ControlFrame(p1)
        p1 = Tk()
        frame = Frame(p1)
        p1.geometry('940x500')
        p1.config(background='#0bd67b')
        frame.pack()

        p1.mainloop()

# -------------------Page2 Page------------------|

if __name__ == "__main__":
    def Page2(self):
        Page2 = p2(self)
        ControlFrame(p2)
        p2 = Tk()
        frame = Frame(p2)
        p2.geometry('940x500')
        p2.config(background='#0bd67b')
        frame.pack()

        def insert_record():
            check_counter = 0
            warn = ""
            if register_name.get() == "":
                warn = "Name can't be empty"
            else:
                check_counter += 1

            if register_email.get() == "":
                warn = "Email can't be empty"
            else:
                check_counter += 1

            if register_mobile.get() == "":
                warn = "Contact can't be empty"
            else:
                check_counter += 1

            if var.get() == "":
                warn = "Gender"
            else:
                check_counter += 1

            if variable.get() == "":
                warn = "Select Country"
            else:
                check_counter += 1

            if register_pwd.get() == "":
                warn = "Password can't be empty"
            else:
                check_counter += 1

            if pwd_again.get() == "":
                warn = "Re-enter password can't be empty"
            else:
                check_counter += 1

            if register_pwd.get() != pwd_again.get():
                warn = "Passwords didn't match!"
            else:
                check_counter += 1

            if check_counter == 8:
                try:
                    con = sqlite3.connect('/dbases/userdata.db')
                    cur = con.cursor()
                    cur.execute(
                        "INSERT INTO record VALUES (:name, :email, :contact, :gender, :country, :password)",
                        {
                            'name': register_name.get(),
                            'email': register_email.get(),
                            'contact': register_mobile.get(),
                            'gender': var.get(),
                            'country': variable.get(),
                            'password': register_pwd.get()
                        })
                    con.commit()
                    messagebox.showinfo('confirmation', 'Record Saved')

                except Exception as ep:  # exception handling
                    messagebox.showerror('', ep)
            else:
                messagebox.showerror('Error', warn)

        def login_response():
            try:
                con = sqlite3.connect('dbases/userdata.db')
                c = con.cursor()
                for row in c.execute("Select * from record"):
                    username = row[1]
                    pwd = row[5]
            except Exception as ep:
                messagebox.showerror('', ep)
            uname = email_tf.get()
            upwd = pwd_tf.get()
            check_counter = 0
            if uname == "":
                warn = "Username can't be empty"
            else:
                check_counter += 1
            if upwd == "":
                warn = "Password can't be empty"
            else:
                check_counter += 1
            if check_counter == 2:
                if (uname == username and upwd == pwd):
                    messagebox.showinfo('Login Status', 'Logged in Successfully!')
                else:
                    messagebox.showerror('Login Status',
                                         'invalid username or password')
            else:
                messagebox.showerror('', warn)

        var = StringVar()
        var.set('male')

        countries = []
        variable = StringVar()
        world = "United Kingdom"
        for country in world:
            country = country.rstrip('\n')
            countries.append(country)
        variable.set(countries[1])

# ---------- widgets

        left_frame = Frame(root, bd=2, bg='#CCCCCC', relief=SOLID, padx=10, pady=10)

        Label(left_frame, text="Enter Email", bg='#CCCCCC', font=f).grid(row=0,
                                                                         column=0,
                                                                         sticky=W,
                                                                         pady=10)

        Label(left_frame, text="Enter Password", bg='#CCCCCC', font=f).grid(row=1,
                                                                            column=0,
                                                                            pady=10)

        email_tf = Entry(left_frame, font=f)
        pwd_tf = Entry(left_frame, font=f, show='*')
        login_btn = Button(left_frame,
                           width=15,
                           text='Login',
                           font=f,
                           relief=FLAT,
                           cursor='hand2',
                           command=login_response)

        right_frame = Frame(login, bd=2, bg='#a1b5a3', relief=SOLID, padx=10, pady=10)

        Label(right_frame, text="Enter Name", bg='#a1b5a3', font=f).grid(row=0,
                                                                         column=0,
                                                                         sticky=W,
                                                                         pady=10)

        Label(right_frame, text="Enter Email", bg='#a1b5a3', font=f).grid(row=1,
                                                                          column=0,
                                                                          sticky=W,
                                                                          pady=10)

        Label(right_frame, text="Contact Number", bg='#a1b5a3', font=f).grid(row=2,
                                                                             column=0,
                                                                             sticky=W,
                                                                             pady=10)

        Label(right_frame, text="Select Gender", bg='#a1b5a3', font=f).grid(row=3,
                                                                            column=0,
                                                                            sticky=W,
                                                                            pady=10)

        Label(right_frame, text="Select Country", bg='#a1b5a3', font=f).grid(row=4,
                                                                             column=0,
                                                                             sticky=W,
                                                                             pady=10)

        Label(right_frame, text="Enter Password", bg='#a1b5a3', font=f).grid(row=5,
                                                                             column=0,
                                                                             sticky=W,
                                                                             pady=10)

        Label(right_frame, text="Re-Enter Password", bg='#a1b5a3',
              font=f).grid(row=6, column=0, sticky=W, pady=10)

        gender_frame = LabelFrame(
            right_frame,
            bg='#a1b5a3',
            padx=10,
            pady=10,
        )

        register_name = Entry(right_frame, font=f)

        register_email = Entry(right_frame, font=f)

        register_mobile = Entry(right_frame, font=f)

        male_rb = Radiobutton(
            gender_frame,
            text='Male',
            bg='#a1b5a3',
            variable=var,
            value='male',
            font=('Times', 10),
        )

        female_rb = Radiobutton(
            gender_frame,
            text='Female',
            bg='#a1b5a3',
            variable=var,
            value='female',
            font=('Times', 10),
        )

        others_rb = Radiobutton(gender_frame,
                                text='Others',
                                bg='#a1b5a3',
                                variable=var,
                                value='others',
                                font=('Times', 10))

        register_country = OptionMenu(right_frame, variable, *countries)

        register_country.config(width=15, font=('Times', 12))
        register_pwd = Entry(right_frame, font=f, show='*')
        pwd_again = Entry(right_frame, font=f, show='*')

        register_btn = Button(right_frame,
                              width=15,
                              text='Register',
                              font=f,
                              relief=SOLID,
                              cursor='hand2',
                              command=insert_record)

        # ---------widgets placement

        email_tf.grid(row=0, column=1, pady=10, padx=20)
        pwd_tf.grid(row=1, column=1, pady=10, padx=20)
        login_btn.grid(row=2, column=1, pady=10, padx=20)
        left_frame.place(x=50, y=50)

        register_name.grid(row=0, column=1, pady=10, padx=20)
        register_email.grid(row=1, column=1, pady=10, padx=20)
        register_mobile.grid(row=2, column=1, pady=10, padx=20)
        register_country.grid(row=4, column=1, pady=10, padx=20)
        register_pwd.grid(row=5, column=1, pady=10, padx=20)
        pwd_again.grid(row=6, column=1, pady=10, padx=20)
        register_btn.grid(row=7, column=1, pady=10, padx=20)
        right_frame.place(x=500, y=50)

        gender_frame.grid(row=3, column=1, pady=10, padx=20)
        male_rb.pack(expand=True, side=LEFT)
        female_rb.pack(expand=True, side=LEFT)
        others_rb.pack(expand=True, side=LEFT)

        p2.mainloop()

# -------------------Page3 Page------------------|

if __name__ == "__main__":
    def Page3(self):
        Page3 = p3(self)
        ControlFrame(p3)
        p3 = Tk()
        frame = Frame(p3)
        p3.geometry('940x500')
        p3.config(background='#0bd67b')
        frame.pack()

        p3.mainloop()

# -------------------Page4 Page------------------|

if __name__ == "__main__":
    def Page4(self):
        Page4 = p4(self)
        ControlFrame(p4)
        p4 = Tk()
        frame = Frame(p4)
        p4.geometry('940x500')
        p4.config(background='#0bd67b')
        frame.pack()

        p4.mainloop()