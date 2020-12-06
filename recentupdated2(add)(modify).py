from tkinter import *
import pymongo
import tkinter.messagebox as MessageBox


class operations:

#____________________________menu_bar_and_top_labels____________________________

    def __init__(self,root):
        self.root = root
        self.root.title('Basic Operations')
        self.root.geometry('%dx%d+0+0' %(root.winfo_screenwidth() ,root. winfo_screenheight()))

        #menubar
        self.Mymenu = Menu(self.root)

        #File
        self.File = Menu(self.Mymenu, tearoff=0)
        self.File.add_command(label="New")
        self.File.add_command(label="Open")
        self.File.add_command(label="Save")
        self.File.add_command(label="Save as")
        self.File.add_command(label="Close")

        #Edit
        self.Edit = Menu (self.Mymenu,tearoff=0)
        self.Edit.add_command(label="Cut")
        self.Edit.add_command(label="Copy")
        self.Edit.add_command(label="Paste")
        self.Edit.add_command(label="Delete")
        self.Edit.add_command(label="Select All")

        # Account Menu
        self.Account = Menu(self.Mymenu,tearoff=0)
        self.Account.add_command(label='Add', command=self.add_acc)
        self.Account.add_command(label='Modify', command=self.modify_account)
        self.Account.add_command(label='List')

        # Account Group Menu
        self.Accountgrp = Menu(self.Mymenu,tearoff=0)
        self.Accountgrp.add_command(label='Add', command=self.acc_group_add)
        self.Accountgrp.add_command(label='Modify',command=self.modify_acc_group)
        self.Accountgrp.add_command(label='List')

        # Item Menu
        self.Item = Menu(self.Mymenu,tearoff=0)
        self.Item.add_command(label='Add',command=self.add_item)
        self.Item.add_command(label='Modify',command=self.modify_item)
        self.Item.add_command(label='List')

        # Item Group Menu
        self.Itemgrp = Menu(self.Mymenu,tearoff=0)
        self.Itemgrp.add_command(label='Add', command=self.add_item_group)
        self.Itemgrp.add_command(label='Modify',command = self.modify_item_group)
        self.Itemgrp.add_command(label='List')

        # stdnarration
        self.stdnarration = Menu(self.Mymenu,tearoff=0)
        self.stdnarration.add_command(label = "Entry")

        # materialcentre
        self.materialcentre = Menu(self.Mymenu,tearoff=0)
        self.materialcentre.add_command(label='Add', command=self.add_material_centre)
        self.materialcentre.add_command(label='Modify', command=self.modify_material_centre)
        self.materialcentre.add_command(label='List')

        # materialcentregroup
        self.materialcentregroup = Menu(self.Mymenu,tearoff=0)
        self.materialcentregroup.add_command(label = "Entry")

        #Unit
        self.unit = Menu(self.Mymenu,tearoff=0)
        self.unit.add_command(label = "Entry")

        #unitconversion
        self.unitconversion = Menu(self.Mymenu,tearoff=0)
        self.unitconversion.add_command(label = "Entry")

        #billsundry
        self.billsundry = Menu(self.Mymenu,tearoff=0)
        self.billsundry.add_command(label = "Entry")

        #billofmaterial

        self.billofmaterial = Menu(self.Mymenu,tearoff=0)
        self.billofmaterial.add_command(label = "Entry")

        #saletype

        self.saletype = Menu(self.Mymenu,tearoff=0)
        self.saletype.add_command(label = "Entry")

        #purchasetype
        self.purchasetype = Menu(self.Mymenu,tearoff=0)
        self.purchasetype.add_command(label = "Entry")

        #taxcategory
        self.tax = Menu(self.Mymenu,tearoff=0)
        self.tax.add_command(label = "Entry")

        #Help
        self.Help = Menu(self.Mymenu,tearoff=0)
        self.Help.add_command(label='About')
        self.Help.add_command(label='Contact us')

        #Account,Accountgropp,Item,Itemgroup cascades
        self.submenu = Menu(self.Mymenu,tearoff=0)
        self.submenu.add_cascade(label='Account',menu=self.Account)
        self.submenu.add_cascade(label='Account Group',menu=self.Accountgrp)
        self.submenu.add_cascade(label='Item',menu=self.Item)
        self.submenu.add_cascade(label='Item Group',menu=self.Itemgrp)
        self.submenu.add_cascade(label='Standard Narration',menu=self.stdnarration)
        self.submenu.add_cascade(label='Material Centre',menu=self.materialcentre)
        self.submenu.add_cascade(label='Material Centre Group',menu=self.materialcentregroup)
        self.submenu.add_cascade(label='Unit',menu=self.unit)
        self.submenu.add_cascade(label='Unit Conversion',menu=self.unitconversion)
        self.submenu.add_cascade(label='Bill Sundry',menu=self.billsundry)
        self.submenu.add_cascade(label='Bill of Material',menu=self.billofmaterial)
        self.submenu.add_cascade(label='Sale Type',menu=self.saletype)
        self.submenu.add_cascade(label='Purchase Type',menu=self.purchasetype)
        self.submenu.add_cascade(label='Tax',menu=self.tax)

        self.Mymenu.add_cascade(label='File',menu=self.File)
        self.Mymenu.add_cascade(label='Edit',menu=self.Edit)
        self.Mymenu.add_cascade(label='Help',menu=self.Help)


        self.master  = Menu(self.Mymenu,tearoff=0)
        self.master.add_cascade(label='Master',menu=self.submenu)

        self.submenu = Menu(self.Mymenu,tearoff=0)

        self.Mymenu.add_command(label='Company')

        self.Mymenu.add_cascade(label='Adminisration',menu=self.master)

        self.root.config(menu=self.Mymenu)




        #______Top Lable____
        self.title = Label(self.root,text="Select Option",bg='#0e2f44',fg='powder blue',font=('Tahoma',24,'bold'))
        self.title.pack()

        #_______________________________Buttons________________________________
        self.button1 = Button(self.root,text='Add Record',height=3,command=self.insert,width=24,bg='#8697a1',fg='black')
        self.button1.place(x = 550,y=150)

        self.button2 = Button(self.root,text='Update Record',command=self.update,height=3,width=24,bg='#8697a1',fg='black')
        self.button2.place(x = 550,y=300)

        self.button3 = Button(self.root,text='Delete Record',command=self.delete,height=3,width=24,bg='#8697a1',fg='black')
        self.button3.place(x = 550,y=450)

        self.button4 = Button(self.root,text='Search Record',command=self.search,height=3,width=24,bg='#8697a1',fg='black')
        self.button4.place(x = 550,y=600)



#____________________________Function for Insert Record_________________________

    #function for insert window                 ADD
    def insert(self):
        #window
        self.insert = Tk()
        self.insert.geometry('%dx%d+0+0' %(root.winfo_screenwidth() ,root. winfo_screenheight()))
        self.insert.title('Insert Window')
        self.insert['background']='#0e2f44'

        #lables
        self.title = Label(self.insert,text="Enter All Details",fg='powder blue',bg='#0e2f44',font=('Tahoma',24,'bold'))
        self.title.pack()

        self.id = Label(self.insert,text='Enter ID : ',font=('bold',10),bg='#0e2f44',fg='white')
        self.id.place(x=100,y=70)

        self.name = Label(self.insert,text='Enter Name : ',font=('bold',10),bg='#0e2f44',fg='white')
        self.name.place(x=100,y=110)

        self.phone = Label(self.insert,text='Enter Phone: ',font=('bold',10),bg='#0e2f44',fg='white')
        self.phone.place(x=100,y=150)

        #EntryBOxes

        self.c_id = Entry(self.insert,width=20)
        self.c_id.place(x=400,y=70)

        self.c_name = Entry(self.insert,width=20)
        self.c_name.place(x=400,y=110)

        self.c_phone = Entry(self.insert,width=20)
        self.c_phone.place(x=400,y=150)

        #Button
        self.button = Button(self.insert,text='SUBMIT',command=self.insertdata,height=2,width=12,bg='#8697a1',fg='black')
        self.button.place(x=400,y=230)

        self.insert.mainloop()

    #function for insert submit button command
    def insertdata(self):
        self._id = self.c_id.get()
        self.name = self.c_name.get()
        self.phone = self.c_phone.get()

        if(self._id=="" or self.name=="" or self.phone==""):
            MessageBox.showinfo("Insert Status","All fields are required")
        else:
            self.m = pymongo.MongoClient("mongodb://localhost:27017/")
            self.mydb = self.m["database"]
            self.mycol = self.mydb["customers"]
            self.mydict = {                         
                "_id" : self.c_id.get(),
                "name" : self.c_name.get(),
                "phone" : self.c_phone.get()                            
                }
            self.x = self.mycol.insert_one(self.mydict)

#____________________________Function for Delete Record_________________________

    def delete(self):
        #window
        self.delete = Tk()
        self.delete.geometry('%dx%d+0+0' %(root.winfo_screenwidth() ,root. winfo_screenheight()))
        self.delete.title('Delete Window')
        self.delete['background']='#0e2f44'

        #lable
        self.title = Label(self.delete,text="Enter Details",fg='powder blue',bg='#0e2f44',font=('Tahoma',20,'bold'))
        self.title.pack()

        self.id = Label(self.delete,text='Enter ID : ',font=('bold',10),fg='white',bg='#0e2f44')
        self.id.place(x=50,y=70)

        #EntryBOx
        self.c_id = Entry(self.delete,width=25)
        self.c_id.place(x=150,y=70)

        #Button
        self.button = Button(self.delete,text='SUBMIT',command=self.deletedata,height=2,width=12,bg='#8697a1',fg='black')
        self.button.place(x=150,y=150)

        self.delete.mainloop()

    #function for delete submit button command
    def deletedata(self):
        self._id = self.c_id.get()

        if(self._id==""):
            MessageBox.showinfo("Insert Status","This field is required")
        else:
            self.m = pymongo.MongoClient("mongodb://localhost:27017/")
            self.mydb = self.m["database"]
            self.mycol = self.mydb["customers"]
            self.myquery = {"_id" : self.c_id.get()}
            self.x = self.mycol.delete_one(self.myquery)

#____________________________Function for Update Record_________________________

    def update(self):
        #window
        self.update = Tk()
        self.update.geometry('%dx%d+0+0' %(root.winfo_screenwidth() ,root. winfo_screenheight()))
        self.update.title('Update Window')
        self.update['background']='#0e2f44'

        #lables
        self.title = Label(self.update,text="Enter All Details",fg='powder blue',bg='#0e2f44',font=('Tahoma',20,'bold'))
        self.title.pack()

        self.id = Label(self.update,text='Enter ID : ',font=('Tahoma',10),bg='#0e2f44',fg='white')
        self.id.place(x=50,y=70)

        self.name = Label(self.update,text='Enter Name : ',font=('Tahoma',10),bg='#0e2f44',fg='white')
        self.name.place(x=50,y=110)

        self.phone = Label(self.update,text='Enter Phone: ',font=('Tahoma',10),bg='#0e2f44',fg='white')
        self.phone.place(x=50,y=150)

        #EntryBOxes

        self.c_id = Entry(self.update,width=20)
        self.c_id.place(x=300,y=70)

        self.c_name = Entry(self.update,width=20)
        self.c_name.place(x=300,y=110)

        self.c_phone = Entry(self.update,width=20)
        self.c_phone.place(x=300,y=150)

        #Button
        self.button = Button(self.update,text='SUBMIT',command=self.updatedata,height=2,width=12,bg='#8697a1',fg='black')
        self.button.place(x=300,y=230)

        self.update.mainloop()

    #function for delete submit button command
    def updatedata(self):
        self._id = self.c_id.get()
        self.name = self.c_name.get()
        self.phone = self.c_phone.get()
        self.update.geometry('%dx%d+0+0' %(root.winfo_screenwidth() ,root. winfo_screenheight()))

        if(self._id==""):
           MessageBox.showinfo("Insert Status","Please enter valid id")
        else:
            self.m = pymongo.MongoClient("mongodb://localhost:27017/")
            self.mydb = self.m["database"]
            self.mycol = self.mydb["customers"]
            self.query = {"_id":self.c_id.get()}
            self.new_values = {"$set":{"name":self.c_name.get(),"phone":self.c_phone.get()}}

            x = self.mycol.update_one(self.query,self.new_values)

#____________________________Function for Search Record_________________________

    def search(self):
        #window
        self.search = Tk()
        self.search.geometry('%dx%d+0+0' %(root.winfo_screenwidth() ,root. winfo_screenheight()))
        self.search.title('Search Window')
        self.search['background']='#0e2f44'


        #lable
        self.title = Label(self.search,text="Enter Details",bg='#0e2f44',fg='powder blue',font=('dense',20,'bold'))
        self.title.pack()

        self.id = Label(self.search,text='Enter ID : ',bg='#0e2f44',fg='white',font=('bold',10))
        self.id.place(x=50,y=70)

        #EntryBOx
        self.c_id = Entry(self.search,width=20)
        self.c_id.place(x=300,y=70)

        #Button
        self.button = Button(self.search,text='SUBMIT',command=self.searchdata,height=2,width=12,bg='#8697a1',fg='black')
        self.button.place(x=300,y=130)

        self.search.mainloop()

    #Function for search submit button
    def searchdata(self):
        self._id = self.c_id.get()

        if(self._id==""):
           MessageBox.showinfo("Insert Status","Insert Valid ID")
        else:
            self.m = pymongo.MongoClient("mongodb://localhost:27017/")
            self.mydb = self.m["database"]
            self.mycol = self.mydb["customers"]
            fro
            self.query = {"_id":self.c_id.get()}
            self.result = self.mycol.find(self.query)
            for x in self.result:
                print(x)

#____________________________add_account_master_____________________________

    def add_acc(self):
        self.root = Tk()
        self.root.title("Add Account Master")
        self.root['background'] = '#0e2f44'
        self.root.geometry("900x600")

        self.name = Label(self.root, text="Name", bg='#0e2f44', fg='white')
        self.name.place(x=20, y=40)

        self.alias = Label(self.root, text="Alias", bg='#0e2f44', fg='white')
        self.alias.place(x=20, y=80)

        self.group = Label(self.root, text="Group", bg='#0e2f44', fg='white')
        self.group.place(x=20, y=120)

        self.Address = Label(self.root, text="Address", bg='#0e2f44', fg='white')
        self.Address.place(x=20, y=160)

        self.Prev_balance = Label(self.root, text="Prev. Year Balance", bg='#0e2f44', fg='white')
        self.Prev_balance.place(x=20, y=200)

        self.Aadhaar = Label(self.root, text="Aadhaar No.", bg='#0e2f44', fg='white')
        self.Aadhaar.place(x=20, y=240)

        self.itspan = Label(self.root, text="IT PAN",bg='#0e2f44', fg='white')
        self.itspan.place(x=20, y=280)

        self.mobile_no = Label(self.root, text="Mobile No.", bg='#0e2f44', fg='white')
        self.mobile_no.place(x=20, y=320)

        self.GST = Label(self.root, text="GST IN/UIN", bg='#0e2f44', fg='white')
        self.GST.place(x=20, y=360)


        #entry_box

        self.name = Entry(self.root, width=30)
        self.name.place(x=260, y=40)

        self.alias = Entry(self.root, width=30)
        self.alias.place(x=260, y=80)

        self.group = Entry(self.root, width=30)
        self.group.place(x=260, y=120)

        self.Address = Entry(self.root, width=60)
        self.Address.place(x=260, y=160)

        self.Prev_balance = Entry(self.root, width=30)
        self.Prev_balance.place(x=260, y=200)

        self.Aadhaar = Entry(self.root, width=30)
        self.Aadhaar.place(x=260, y=240)

        self.itspan = Entry(self.root, width=30)
        self.itspan.place(x=260, y=280)

        self.mobile_no = Entry(self.root, width=30)
        self.mobile_no.place(x=260, y=320)

        self.GST = Entry(self.root, width=30)
        self.GST.place(x=260, y=360)

        #Save_button
        self.my_button = Button(self.root, text="Save", height=2, command=self.insert_add, width=12, bg='#8697a1', fg='black')
        self.my_button.place(x=120, y=400)

        self.root.mainloop()

#____________________________function_to_insert_record_in_add_account_______

    def insert_add(self):
        self.n = self.name.get()
        self.ali = self.alias.get()
        self.gr = self.group.get()
        self.ad = self.Address.get()
        self.pvb = self.Prev_balance.get()
        self.adhr = self.Aadhaar.get()
        self.itp = self.itspan.get()
        self.mobn = self.mobile_no.get()
        self.tax = self.GST.get()

        if(self.n == "" or self.ali == "" or self.gr == "" or self.ad=="" or self.pvb=="" or self.adhr=="" or self.itp=="" or self.mobn=="" or self.tax==""):
            MessageBox.showinfo("Insert Status","All fields are required")
        else:
            self.m = pymongo.MongoClient("mongodb://localhost:27017/")
            self.mydb = self.m["database"]
            self.mycol = self.mydb["account_add"]
            self.mydict = {
                "name" : self.name.get(),
                "alias" : self.alias.get(),
                "group" : self.group.get(),
                "address" : self.Address.get(),
                "prevbal" : self.Prev_balance.get(),
                "aadhar" : self.Aadhaar.get(),
                "itpan" : self.itspan.get(),
                "mobile" : self.mobile_no.get(),
                "gst" : self.GST.get()
                    }
            self.x = self.mycol.insert_one(self.mydict)

#____________________________modify_account_________________________________
    def modify_account(self):
        self.root = Tk()
        self.root.title("Add Account Master")
        self.root['background'] = '#0e2f44'
        self.root.geometry("900x600")

        self.name = Label(self.root, text="Name", bg='#0e2f44', fg='white')
        self.name.place(x=20, y=40)

        self.alias = Label(self.root, text="Alias", bg='#0e2f44', fg='white')
        self.alias.place(x=20, y=80)

        self.group = Label(self.root, text="Group", bg='#0e2f44', fg='white')
        self.group.place(x=20, y=120)

        self.Address = Label(self.root, text="Address",bg='#0e2f44', fg='white')
        self.Address.place(x=20, y=160)

        self.Prev_balance = Label(self.root, text="Prev. Year Balance", bg='#0e2f44', fg='white')
        self.Prev_balance.place(x=20, y=200)

        self.Aadhaar = Label(self.root, text="Aadhaar No.",bg='#0e2f44', fg='white')
        self.Aadhaar.place(x=20, y=240)

        self.itspan = Label(self.root, text="IT PAN", bg='#0e2f44', fg='white')
        self.itspan.place(x=20, y=280)

        self.mobile_no = Label(self.root, text="Mobile No.", bg='#0e2f44', fg='white')
        self.mobile_no.place(x=20, y=320)

        self.GST = Label(self.root, text="GST IN/UIN",bg='#0e2f44', fg='white')
        self.GST.place(x=20, y=360)

        #entry_box

        self.name = Entry(self.root, width=30)
        self.name.place(x=260, y=40)

        self.alias = Entry(self.root, width=30)
        self.alias.place(x=260, y=80)

        self.group = Entry(self.root, width=30)
        self.group.place(x=260, y=120)

        self.Address = Entry(self.root, width=60)
        self.Address.place(x=260, y=160)

        self.Prev_balance = Entry(self.root, width=30)
        self.Prev_balance.place(x=260, y=200)

        self.Aadhaar = Entry(self.root, width=30)
        self.Aadhaar.place(x=260, y=240)

        self.itspan = Entry(self.root, width=30)
        self.itspan.place(x=260, y=280)

        self.mobile_no = Entry(self.root, width=30)
        self.mobile_no.place(x=260, y=320)

        self.GST = Entry(self.root, width=30)
        self.GST.place(x=260, y=360)

        #Save_button
        self.my_button = Button(self.root, text="Modify", height=2,command=self.insert_add, width=12, bg='#8697a1', fg='black')
        self.my_button.place(x=120, y=400)

        self.root.mainloop()

#____________________________update_modify_account__________________________
    def update_modify_account(self):
        self.n = self.name.get()
        self.ali = self.alias.get()
        self.gr = self.group.get()
        self.ad = self.Address.get()
        self.pvb = self.Prev_balance.get()
        self.adhr = self.Aadhaar.get()
        self.itp = self.itspan.get()
        self.mobn = self.mobile_no.get()
        self.tax = self.GST.get()

        if(self.n == "" or self.ali == ""):
           MessageBox.showinfo("Insert Status","Please enter valid id")
        else:
            self.m = pymongo.MongoClient("mongodb://localhost:27017/")
            self.mydb = self.m["database"]
            self.mycol = self.mydb["account_add"]
            self.query = {"_id":self.name.get()}
            self.new_values = {"$set": {"alias": self.alias.get(), "group": self.group.get(), "Address": self.Address.get(
            ), "prev_bal": self.Prev_balance.get(), "Aadhaar": self.Aadhaar.get(), "IT": self.itspan.get(), "Mobile": self.mobile_no.get(), "GST":self.GST.get()}}

            x = self.mycol.update_one(self.query,self.new_values)

#____________________________add_account_group______________________________


    def acc_group_add(self):
        self.root = Tk()
        self.root.title("Add Account Group Master")
        self.root['background'] = '#0e2f44'
        self.root.geometry("900x600")

        # Labels
        self.group = Label(self.root, text="Group", bg='#0e2f44', fg='white')
        self.group.place(x=20, y=40)

        self.alias = Label(self.root, text="Alias", bg='#0e2f44', fg='white')
        self.alias.place(x=20, y=80)

        self.under_group = Label(self.root, text="Under Group", bg='#0e2f44', fg='white')
        self.under_group.place(x=20, y=120)

        self.primary_group = Label(self.root, text="Primary Group", bg='#0e2f44', fg='white')
        self.primary_group.place(x=20, y=160)

        self.radio_primary_group = Radiobutton(self.root, value=2, text="YES")
        self.radio_primary_group.place(x=260, y=160)

        self.radio_primary_group = Radiobutton(self.root, value=1, text="NO")
        self.radio_primary_group.place(x=320, y=160)


        #entry_box

        self.group = Entry(self.root, width=30)
        self.group.place(x=260, y=40)

        self.alias = Entry(self.root, width=30)
        self.alias.place(x=260, y=80)

        self.under_group = Entry(self.root, width=30)
        self.under_group.place(x=260, y=120)

        #Save_button

        self.my_button = Button(self.root, text="Save", height=2,command=self.insert_add_account_group, width=12, bg='#8697a1', fg='black')
        self.my_button.place(x=260, y=200)
        self.root.mainloop()

#____________________________function_to_insert_record_in_add_account_group

    def insert_add_account_group(self):
        self.n = self.group.get()
        self.ali = self.alias.get()
        self.grp = self.under_group.get()

        if(self.n == "" or self.ali == "" or self.grp == ""):
            MessageBox.showinfo("Insert Status", "All fields are required")
        else:
            self.m = pymongo.MongoClient("mongodb://localhost:27017/")
            self.mydb = self.m["database"]
            self.mycol = self.mydb["add_acc_grp"]
            self.mydict = {
                "group": self.group.get(),
                "alias": self.alias.get(),
                "under_group": self.under_group.get()
                    }
            self.x = self.mycol.insert_two(self.mydict)

#____________________________modify_account_group___________________________

    def modify_acc_group(self):
        self.root = Tk()
        self.root.title("Add Account Group Master")
        self.root['background'] = '#0e2f44'
        self.root.geometry("900x600")

        # Labels
        self.group = Label(self.root, text="Group", bg='#0e2f44', fg='white')
        self.group.place(x=20, y=40)

        self.alias = Label(self.root, text="Alias", bg='#0e2f44', fg='white')
        self.alias.place(x=20, y=80)

        self.under_group = Label(self.root, text="Under Group", bg='#0e2f44', fg='white')
        self.under_group.place(x=20, y=120)

        self.primary_group = Label(self.root, text="Primary Group", bg='#0e2f44', fg='white')
        self.primary_group.place(x=20, y=160)

        self.radio_primary_group = Radiobutton(self.root, value=2, text="YES")
        self.radio_primary_group.place(x=260, y=160)

        self.radio_primary_group = Radiobutton(self.root, value=1, text="NO")
        self.radio_primary_group.place(x=320, y=160)


        #entry_box

        self.group = Entry(self.root, width=30)
        self.group.place(x=260, y=40)

        self.alias = Entry(self.root, width=30)
        self.alias.place(x=260, y=80)

        self.under_group = Entry(self.root, width=30)
        self.under_group.place(x=260, y=120)

        #Save_button

        self.my_button = Button(self.root, text="Modify", height=2,command=self.insert_add_account_group, width=12, bg='#8697a1', fg='black')
        self.my_button.place(x=260, y=200)
        self.root.mainloop()

#____________________________function_to_modify_account_group_______________
    
    def update_modify_item_group(self):
        self.grp = self.group.get()
        self.ali = self.alias.get()
        self.under_group = self.under_group.get()

        if(self.grp == ""):
           MessageBox.showinfo("Insert Status","Please enter valid id")
        else:
            self.m = pymongo.MongoClient("mongodb://localhost:27017/")
            self.mydb = self.m["database"]
            self.mycol = self.mydb["add_acc_grp"]
            self.query = {"_id":self.name.get()}
            self.new_values = {"$set":{"Group":self.group.get(),"Alias":self.alias.get(),"Under Group":self.under_group.get()}}

            x = self.mycol.update_one(self.query,self.new_values)

#____________________________add_item_______________________________________
            
    def add_item(self):
        self.root = Tk()
        self.root.title("Add Item Master")
        self.root['background'] = '#0e2f44'
        self.root.geometry("900x600")

        self.name = Label(self.root, text="Name", bg='#0e2f44', fg='white')
        self.name.place(x=20, y=40)

        self.alias = Label(self.root, text="Alias", bg='#0e2f44', fg='white')
        self.alias.place(x=20, y=80)

        self.group = Label(self.root, text="Group", bg='#0e2f44', fg='white')
        self.group.place(x=20, y=120)

        self.sales_price = Label(self.root, text="Sales Price", bg='#0e2f44', fg='white')
        self.sales_price.place(x=20, y=160)

        self.purc_price = Label(self.root, text="Purc. Price", bg='#0e2f44', fg='white')
        self.purc_price.place(x=20, y=200)

        self.mrp = Label(self.root, text="M.R.P", bg='#0e2f44', fg='white')
        self.mrp.place(x=20, y=240)

        self.min_sales_price = Label(self.root, text="Min Sales Price", bg='#0e2f44', fg='white')
        self.min_sales_price.place(x=20, y=280)

        self.unit = Label(self.root, text="Unit", bg='#0e2f44', fg='white')
        self.unit.place(x=20, y=320)

        self.op_stock = Label(self.root, text="Op Stock(qty)", bg='#0e2f44', fg='white')
        self.op_stock.place(x=20, y=360)

        #entry_box

        self.name = Entry(self.root, width=30)
        self.name.place(x=260, y=40)

        self.alias = Entry(self.root, width=30)
        self.alias.place(x=260, y=80)

        self.group = Entry(self.root, width=30)
        self.group.place(x=260, y=120)

        self.sales_price = Entry(self.root, width=30)
        self.sales_price.place(x=260, y=160)

        self.purc_price = Entry(self.root, width=30)
        self.purc_price.place(x=260, y=200)

        self.mrp = Entry(self.root, width=30)
        self.mrp.place(x=260, y=240)

        self.min_sales_price = Entry(self.root, width=30)
        self.min_sales_price.place(x=260, y=280)

        self.unit = Entry(self.root, width=30)
        self.unit.place(x=260, y=320)

        self.op_stock = Entry(self.root, width=30)
        self.op_stock.place(x=260, y=360)

        # save_button
        
        self.my_button = Button(self.root, text="Save", height=2,command=self.insert_add_item, width=12, bg='#8697a1', fg='black')
        self.my_button.place(x=120, y=400)

        self.root.mainloop()

#____________________________function_to_insert_record_of_add_item__________
    def insert_add_item(self):
        self.n = self.name.get()
        self.ali = self.alias.get()
        self.gr = self.group.get()
        self.salesprice = self.sales_price.get()
        self.purcprice = self.purc_price.get()
        self.MRP = self.mrp.get()
        self.minsales = self.min_sales_price.get()
        self.unt = self.unit.get()
        self.stock = self.op_stock.get()

        if(self.n == "" or self.ali == "" or self.gr == "" or self.salesprice == "" or self.purcprice == "" or
        self.MRP == "" or self.minsales == "" or self.unt == "" or self.stock == ""):
            MessageBox.showinfo("Insert Status", "All fields are required")

        else:
            self.m = pymongo.MongoClient("mongodb://localhost:27017/")
            self.mydb = self.m["database"]
            self.mycol = self.mydb["additem"]
            self.mydict = {
                "name": self.name.get(),
                "alias": self.alias.get(),
                "group": self.group.get(),
                "sales_price": self.sales_price.get(),
                "purc_price": self.purc_price.get(),
                "mrp": self.mrp.get(),
                "min_sales_price": self.min_sales_price.get(),
                "unit": self.unit.get(),
                "op_stock": self.op_stock.get()
                    }
            self.x = self.mycol.insert_three(self.mydict)

# ___________________________modify_item____________________________________
    
    def modify_item(self):
        self.root = Tk()
        self.root.title("Modify Item Master")
        self.root['background'] = '#0e2f44'
        self.root.geometry("900x600")

        self.name = Label(self.root, text="Name", bg='#0e2f44', fg='white')
        self.name.place(x=20, y=40)

        self.alias = Label(self.root, text="Alias", bg='#0e2f44', fg='white')
        self.alias.place(x=20, y=80)

        self.group = Label(self.root, text="Group", bg='#0e2f44', fg='white')
        self.group.place(x=20, y=120)

        self.sales_price = Label(self.root, text="Sales Price", bg='#0e2f44', fg='white')
        self.sales_price.place(x=20, y=160)

        self.purc_price = Label(self.root, text="Purc. Price", bg='#0e2f44', fg='white')
        self.purc_price.place(x=20, y=200)

        self.mrp = Label(self.root, text="M.R.P", bg='#0e2f44', fg='white')
        self.mrp.place(x=20, y=240)

        self.min_sales_price = Label(self.root, text="Min Sales Price", bg='#0e2f44', fg='white')
        self.min_sales_price.place(x=20, y=280)

        self.unit = Label(self.root, text="Unit", bg='#0e2f44', fg='white')
        self.unit.place(x=20, y=320)

        self.op_stock = Label(self.root, text="Op Stock(qty)", bg='#0e2f44', fg='white')
        self.op_stock.place(x=20, y=360)


        #entry_box
        self.name = Entry(self.root, width=30)
        self.name.place(x=260, y=40)

        self.alias = Entry(self.root, width=30)
        self.alias.place(x=260, y=80)

        self.group = Entry(self.root, width=30)
        self.group.place(x=260, y=120)

        self.sales_price = Entry(self.root, width=30)
        self.sales_price.place(x=260, y=160)

        self.purc_price = Entry(self.root, width=30)
        self.purc_price.place(x=260, y=200)

        self.mrp = Entry(self.root, width=30)
        self.mrp.place(x=260, y=240)

        self.min_sales_price = Entry(self.root, width=30)
        self.min_sales_price.place(x=260, y=280)

        self.unit = Entry(self.root, width=30)
        self.unit.place(x=260, y=320)

        self.op_stock = Entry(self.root, width=30)
        self.op_stock.place(x=260, y=360)

        # save_button
        
        self.my_button = Button(self.root, text="Modify", height=2,command=self.modify_item, width=12, bg='#8697a1', fg='black')
        self.my_button.place(x=120, y=400)

        self.root.mainloop()

# ___________________________function_to_modify_item________________________
    def modify_item(self):
        self.n = self.name.get()
        self.ali = self.alias.get()
        self.grp = self.group.get()
        self.sal_pr = self.sales_price.get()
        self.pur_pr = self.purc_price.get()
        self.rate = self.mrp.get()
        self.msp = self.min_sales_price.get()
        self.unt = self.unit.get()
        self.op = self.op_stock.get()

        if(self.n == ""):
            MessageBox.showinfo("Insert Status","Please enter valid id")
        else:
            self.m = pymongo.MongoClient("mongodb://localhost:27017/")
            self.mydb = self.m["database"]
            self.mycol = self.mydb["additem"]
            self.query = {"_id":self.name.get()}
            self.new_values = {"$set": {"Alias": self.alias.get(), "Group": self.group.get(), "Sales Price": self.sales_price.get(), "Purchase Price": self.purc_price.get(
            ), "MRP": self.mrp.get(), "Min Sales Price": self.min_sales_price.get(), "Unit": self.unit.get(), "OP stock": self.op_stock.get()}}

            x = self.mycol.update_one(self.query,self.new_values)

# ___________________________add_item_grp___________________________________
            
    def add_item_group(self):
        self.root = Tk()
        self.root.title("Add Item Group Master")
        self.root['background'] = '#0e2f44'
        self.root.geometry("900x600")

        self.name = Label(self.root, text="Name", bg='#0e2f44', fg='white')
        self.name.place(x=20, y=40)

        self.alias = Label(self.root, text="Alias", bg='#0e2f44', fg='white')
        self.alias.place(x=20, y=80)

        self.group = Label(self.root, text="Group", bg='#0e2f44', fg='white')
        self.group.place(x=20, y=120)

        self.stock_acc = Label(self.root, text="Stock Account", bg='#0e2f44', fg='white')
        self.stock_acc.place(x=20, y=160)

        self.sales_acc = Label(self.root, text="Sales Account", bg='#0e2f44', fg='white')
        self.sales_acc.place(x=20, y=200)

        self.purchase_acc = Label(self.root, text="Purchase Account", bg='#0e2f44', fg='white')
        self.purchase_acc.place(x=20, y=240)

        self.primary_group = Label(self.root, text="Primary Group", bg='#0e2f44', fg='white')
        self.primary_group.place(x=20, y=280)

        self.radio_primary_group = Radiobutton(self.root, value=2, text="YES")
        self.radio_primary_group.place(x=260, y=280)

        self.radio_primary_group = Radiobutton(self.root, value=1, text="NO")
        self.radio_primary_group.place(x=320, y=280)


        # entry_box
        self.name = Entry(self.root, width=30)
        self.name.place(x=260, y=40)

        self.alias = Entry(self.root, width=30)
        self.alias.place(x=260, y=80)

        self.group = Entry(self.root, width=30)
        self.group.place(x=260, y=120)

        self.stock_acc = Entry(self.root, width=30)
        self.stock_acc.place(x=260, y=160)

        self.sales_acc = Entry(self.root, width=30)
        self.sales_acc.place(x=260, y=200)

        self.purchase_acc = Entry(self.root, width=30)
        self.purchase_acc.place(x=260, y=240)

        self.my_button = Button(self.root, text="Save", height=2, command=self.insert_add_item_group, width=12, bg='#8697a1', fg='black')
        self.my_button.place(x=120, y=400)

        self.root.mainloop()

#____________________________function_to_insert_record_in_add_item_group______

    def insert_add_item_group(self):
        self.n = self.name.get()
        self.ali = self.alias.get()
        self.gr = self.group.get()
        self.stockacc = self.stock_acc.get()
        self.salesacc = self.sales_acc.get()
        self.purchaseacc = self.purchase_acc.get()

        if(self.n == "" or self.ali == "" or self.gr == "" or self.stockacc == "" or self.salesacc == "" or
            self.purchaseacc == ""):
            MessageBox.showinfo("Insert Status", "All fields are required")

        else:
            self.m = pymongo.MongoClient("mongodb://localhost:27017/")
            self.mydb = self.m["database"]
            self.mycol = self.mydb["itemgroupadd"]
            self.mydict = {
                "name": self.name.get(),
                "alias": self.alias.get(),
                "group": self.group.get(),
                "stock_acc": self.stock_acc.get(),
                "salesacc": self.salesacc.get(),
                "purchaseacc": self.purchaseacc.get()
            }
            self.x = self.mycol.insert_four(self.mydict)

# ___________________________modify_item_group______________________________
    
    def modify_item_group(self):
        self.root = Tk()
        self.root.title("Modify Item Group Master")
        self.root['background'] = '#0e2f44'
        self.root.geometry("900x600")

        self.name = Label(self.root, text="Name", bg='#0e2f44', fg='white')
        self.name.place(x=20, y=40)

        self.alias = Label(self.root, text="Alias", bg='#0e2f44', fg='white')
        self.alias.place(x=20, y=80)

        self.group = Label(self.root, text="Group", bg='#0e2f44', fg='white')
        self.group.place(x=20, y=120)

        self.stock_acc = Label(self.root, text="Stock Account", bg='#0e2f44', fg='white')
        self.stock_acc.place(x=20, y=160)

        self.sales_acc = Label(self.root, text="Sales Account", bg='#0e2f44', fg='white')
        self.sales_acc.place(x=20, y=200)

        self.purchase_acc = Label(self.root, text="Purchase Account", bg='#0e2f44', fg='white')
        self.purchase_acc.place(x=20, y=240)

        self.primary_group = Label(self.root, text="Primary Group", bg='#0e2f44', fg='white')
        self.primary_group.place(x=20, y=280)

        self.radio_primary_group = Radiobutton(self.root, value=2, text="YES")
        self.radio_primary_group.place(x=260, y=280)

        self.radio_primary_group = Radiobutton(self.root, value=1, text="NO")
        self.radio_primary_group.place(x=320, y=280)


        # entry_box
        self.name = Entry(self.root, width=30)
        self.name.place(x=260, y=40)

        self.alias = Entry(self.root, width=30)
        self.alias.place(x=260, y=80)

        self.group = Entry(self.root, width=30)
        self.group.place(x=260, y=120)

        self.stock_acc = Entry(self.root, width=30)
        self.stock_acc.place(x=260, y=160)

        self.sales_acc = Entry(self.root, width=30)
        self.sales_acc.place(x=260, y=200)

        self.purchase_acc = Entry(self.root, width=30)
        self.purchase_acc.place(x=260, y=240)

        self.my_button = Button(self.root, text="Save", height=2,command=self.update_modify_item_group, width=12, bg='#8697a1', fg='black')
        self.my_button.place(x=120, y=400)

        self.root.mainloop()

# ___________________________function_to_modify_item_group__________________
    def update_modify_item_group(self):
        self.n = self.name.get()
        self.ali = self.alias.get()
        self.grp = self.group.get()
        self.st_acc = self.stock_acc.get()
        self.sal_acc = self.sales_acc.get()
        self.pur_acc = self.purchase_acc.get()

        if(self.n == ""):
           MessageBox.showinfo("Insert Status","Please enter valid id")
        else:
            self.m = pymongo.MongoClient("mongodb://localhost:27017/")
            self.mydb = self.m["database"]
            self.mycol = self.mydb["itemgroupadd"]
            self.query = {"_id":self.name.get()}
            self.new_values = {"$set":{"alias":self.alias.get(),"group":self.group.get(),"stkacc":self.stock_acc.get(),"salseacc":self.salaes_acc.get(),"purcacc":self.purchase_acc.get()}}

            x = self.mycol.update_one(self.query,self.new_values)

#____________________________add material centre____________________________
    
    def add_material_centre(self):
        self.root = Tk()
        self.root.title("Add Material Centre Master")
        self.root['background'] = '#0e2f44'
        self.root.geometry("900x600")

        self.name = Label(self.root, text="Name", bg='#0e2f44', fg='white')
        self.name.place(x=20, y=40)

        self.alias = Label(self.root, text="Alias", bg='#0e2f44', fg='white')
        self.alias.place(x=20, y=80)

        self.print_name = Label(self.root, text="Print Name", bg='#0e2f44', fg='white')
        self.print_name.place(x=20, y=120)

        self.stock_acc = Label(self.root, text="Stock Account", bg='#0e2f44', fg='white')
        self.stock_acc.place(x=20, y=160)

        self.group = Label(self.root, text="Group", bg='#0e2f44', fg='white')
        self.group.place(x=20, y=200)

        self.primary_group = Label(self.root, text="Reflect the Stock in Balance Sheet", bg='#0e2f44',fg='white')
        self.primary_group.place(x=20, y=280)

        self.radio_primary_group = Radiobutton(self.root, value=2, text="YES")
        self.radio_primary_group.place(x=260, y=280)

        self.radio_primary_group = Radiobutton(self.root, value=1, text="NO")
        self.radio_primary_group.place(x=320, y=280)

        # entry_box
        self.name = Entry(self.root, width=30)
        self.name.place(x=260, y=40)

        self.alias = Entry(self.root, width=30)
        self.alias.place(x=260, y=80)

        self.print_name = Entry(self.root, width=30)
        self.print_name.place(x=260, y=120)

        self.stock_acc = Entry(self.root, width=30)
        self.stock_acc.place(x=260, y=160)

        self.group = Entry(self.root, width=30)
        self.group.place(x=260, y=200)

        self.my_button = Button(self.root, text="Save", height=2,command=self.update_modify_item_group, width=12, bg='#8697a1', fg='black')
        self.my_button.place(x=260, y=400)

        self.root.mainloop()

#____________________________function_to_insert_record_in_material_centre___

    def insert_add_item_group(self):
        self.n = self.name.get()
        self.ali = self.alias.get()
        self.gr = self.group.get()
        self.stockacc = self.stock_acc.get()

        if(self.n == "" or self.ali == "" or self.gr == "" or self.stockacc == ""):
            MessageBox.showinfo("Insert Status", "All fields are required")

        else:
            self.m = pymongo.MongoClient("mongodb://localhost:27017/")
            self.mydb = self.m["database"]
            self.mycol = self.mydb["Add Material Centre"]
            self.mydict = {
                "name": self.name.get(),
                "alias": self.alias.get(),
                "group": self.group.get(),
                "print name": self.print_name.get(),
                "stock_acc": self.stock_acc.get(),
            }
            self.x = self.mycol.insert_five(self.mydict)

#____________________________modify_Material_centre_________________________
    def modify_material_centre(self):
        self.root = Tk()
        self.root.title("Add Modify Centre Master")
        self.root['background'] = '#0e2f44'
        self.root.geometry("900x600")

        self.name = Label(self.root, text="Name", bg='#0e2f44', fg='white')
        self.name.place(x=20, y=40)

        self.alias = Label(self.root, text="Alias", bg='#0e2f44', fg='white')
        self.alias.place(x=20, y=80)

        self.print_name = Label(self.root, text="Print Name", bg='#0e2f44', fg='white')
        self.print_name.place(x=20, y=120)

        self.stock_acc = Label(self.root, text="Stock Account", bg='#0e2f44', fg='white')
        self.stock_acc.place(x=20, y=160)

        self.group = Label(self.root, text="Group", bg='#0e2f44', fg='white')
        self.group.place(x=20, y=200)

        self.primary_group = Label(self.root, text="Reflect the Stock in Balance Sheet", bg='#0e2f44', fg='white')
        self.primary_group.place(x=20, y=280)

        self.radio_primary_group = Radiobutton(self.root, value=2, text="YES")
        self.radio_primary_group.place(x=260, y=280)

        self.radio_primary_group = Radiobutton(self.root, value=1, text="NO")
        self.radio_primary_group.place(x=320, y=280)

        # entry_box
        self.name = Entry(self.root, width=30)
        self.name.place(x=260, y=40)

        self.alias = Entry(self.root, width=30)
        self.alias.place(x=260, y=80)

        self.print_name = Entry(self.root, width=30)
        self.print_name.place(x=260, y=120)

        self.stock_acc = Entry(self.root, width=30)
        self.stock_acc.place(x=260, y=160)

        self.group = Entry(self.root, width=30)
        self.group.place(x=260, y=200)

        self.my_button = Button(self.root, text="Save", height=2,command=self.update_modify_item_group, width=12, bg='#8697a1', fg='black')
        self.my_button.place(x=260, y=400)

        self.root.mainloop()
        
#____________________________function_to_modify_record_in_material_centre___

    def insert_add_item_group(self):
        self.n = self.name.get()
        self.ali = self.alias.get()
        self.gr = self.group.get()
        self.stockacc = self.stock_acc.get()

        if(self.n == "" or self.ali == "" or self.gr == "" or self.stockacc == ""):
            MessageBox.showinfo("Insert Status", "All fields are required")

        else:
            self.m = pymongo.MongoClient("mongodb://localhost:27017/")
            self.mydb = self.m["database"]
            self.mycol = self.mydb["Add Material Centre"]
            self.mydict = {
                "name": self.name.get(),
                "alias": self.alias.get(),
                "group": self.group.get(),
                "print name": self.print_name.get(),
                "stock_acc": self.stock_acc.get(),
            }
            self.x = self.mycol.insert_six(self.mydict)


#____________________________class object and main window___________________
root = Tk()
root['background']='#0e2f44'
#icon = PhotoImage(file = 'diagram.png')
#root.iconphoto(False,icon)
obj = operations(root)
root.mainloop()






