from tkinter import *
import pymongo
import sys


class login:
    def __init__(self,log):
        self.log = log
        self.log.title('Login')
        self.log.geometry('%dx%d+0+0' %(log.winfo_screenwidth() ,log.winfo_screenheight()))

        self.title = Label(self.log,text="Please login",bg='#355C7D',fg='white',font=('dense',24,'bold'))
        self.title.pack()

        #label username and password
        self.username = Label(self.log,text='Username',font=('Tahoma','10','bold'),bg='#355C7D',fg='white')
        self.username.place(x=120,y=110)

        self.password = Label(self.log,text='Password',font=('Tahoma','10','bold'),bg='#355C7D',fg='white')
        self.password.place(x=120,y=170)

        #entry box for above label
        self.c_username = Entry(self.log,width=20)
        self.c_username.place(x=300,y=110)

        self.c_password = Entry(self.log,width=20,show='*')
        self.c_password.place(x=300,y=170)

        #login button
        self.button = Button(self.log,text='Log In',height=2,width=12,bg='#d77337', command=self.login_button)
        self.button.place(x=300,y=230)

        #  function for login button command
    
    def login_button(self):
        # connecting to mongodb preferable database
        self.mc = pymongo.MongoClient("mongodb://localhost:27017/")
        self.mydb = self.mc["database"]
        self.mycol = self.mydb["custidpass"]
        self.query = {"username":self.c_username.get()}
        self.doc = self.mycol.find(self.query)

        #  finding username and pass
        for x in self.doc:
            self.l = x

        if(self.c_username.get() == self.l["username"] and self.c_password.get() == self.l["password"]):
            self.close()
            import Recentupdated2
        elif(self.c_username.get() != self.l["username"] or self.c_password.get() != self.l["password"]):
            MessageBox.showinfo("Insert status","Invalid username or password")
        else:
            MessageBox.showinfo("Insert status","All field are required")

        
        #function for Exit from app
    def close(self):
        self.log.destroy()



log = Tk()
log['background']='#355C7D'
obj = login(log)
log.mainloop()
