from tkinter import *
from PIL import Image, ImageTk  # pip install pillow
from tkinter import messagebox
from tkinter import ttk
import pymysql
root=Tk()
img = PhotoImage(file='C:\\Users\\arpit\\Desktop\\sumit\\login1.png')
root.iconphoto(False, img)
def open_main():
    root.destroy()  # close the current window
    import main # import the admin_panel file
    
def go_back():
    root.destroy() # define the action to perform when the back button is clicked
    import main # for example, you can close the current window and open the previous window
    open_main()
    back_button = Button(root, text="Back", command=open_main)
    back_button.pack(side=LEFT, padx=10, pady=10)


class LMS:
        
    def __init__(self,root):
        self.root = root
        self.root.title("USER DETAILS")
        self.root.geometry("1350x700+0+0")
        self.root.resizable(False, False)

#### TITLE ####

        title=Label(self.root,text="User Details",bd=5,relief=GROOVE,font=("times new roman",30,"bold"),bg="paleturquoise",fg="black")
        title.pack(side=TOP, fill=X)

        # background
        root.MenuLogo = Image.open("bg1.jpg")
        root.MenuLogo = root.MenuLogo.resize((1350,720), Image.ANTIALIAS)
        root.MenuLogo = ImageTk.PhotoImage(root.MenuLogo)

        lbl_MenuLogo = Label(root, image=root.MenuLogo, bg="white")
        lbl_MenuLogo.pack(side=TOP, fill=X)

### All Variables ###

        self.nID_var=StringVar()
        self.Name_var=StringVar()
        self.Branch_var=StringVar()
        self.Semester_var=StringVar()
        self.Division_var=StringVar()
        self.Gender_var=StringVar()
        self.Dob_var=StringVar()
        self.Email_var=StringVar()


        self.search_by=StringVar()
        self.search_txt=StringVar()


#### Manage Frame ####

        Manage_Frame = Frame(self.root, bd=5, relief=RIDGE,bg="paleturquoise")
        Manage_Frame.place(x=10,y=65,width=430,height=625)

        m_title=Label(Manage_Frame,text="Manage Users",font=("times new roman",20,"bold"),bg="paleturquoise",fg="black")
        m_title.grid(row=0,columnspan=2,pady=20)


        lbl_nID=Label(Manage_Frame,text="Nex-ID",font=("times new roman",20,"bold"),bg="paleturquoise",fg="black")
        lbl_nID.grid(row=1,column=0,pady=10,padx=20,sticky="w")

        txt_nID=Entry(Manage_Frame,textvariable=self.nID_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_nID.grid(row=1,column=1,pady=10,padx=20,sticky="w")


        lbl_Name=Label(Manage_Frame,text="Name",font=("times new roman",20,"bold"),bg="paleturquoise",fg="black")
        lbl_Name.grid(row=2,column=0,pady=10,padx=20,sticky="w")

        txt_Name=Entry(Manage_Frame,textvariable=self.Name_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Name.grid(row=2,column=1,pady=10,padx=20,sticky="w")


        lbl_Branch=Label(Manage_Frame,text="Branch",font=("times new roman",20,"bold"),bg="paleturquoise",fg="black")
        lbl_Branch.grid(row=3,column=0,pady=10,padx=20,sticky="w")

        txt_Branch=Entry(Manage_Frame,textvariable=self.Branch_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Branch.grid(row=3,column=1,pady=10,padx=20,sticky="w")


        lbl_Semester=Label(Manage_Frame,text="Semester",font=("times new roman",20,"bold"),bg="paleturquoise",fg="black")
        lbl_Semester.grid(row=4,column=0,pady=10,padx=20,sticky="w")

        txt_Semester=Entry(Manage_Frame,textvariable=self.Semester_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Semester.grid(row=4,column=1,pady=10,padx=20,sticky="w")


        lbl_Division=Label(Manage_Frame,text="Division",font=("times new roman",20,"bold"),bg="paleturquoise",fg="black")
        lbl_Division.grid(row=5,column=0,pady=10,padx=20,sticky="w")

        txt_Division=Entry(Manage_Frame,textvariable=self.Division_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Division.grid(row=5,column=1,pady=10,padx=20,sticky="w")


        lbl_Gender=Label(Manage_Frame,text="Gender",font=("times new roman",20,"bold"),bg="paleturquoise",fg="black")
        lbl_Gender.grid(row=6,column=0,pady=10,padx=20,sticky="w")

        combo_gender=ttk.Combobox(Manage_Frame,textvariable=self.Gender_var,font=("times new roman",13,"bold"),state='readonly')
        combo_gender['values']=("Male","Female")
        combo_gender.grid(row=6,column=1,pady=10,padx=20,sticky="w")


        lbl_DOB=Label(Manage_Frame,text="DOB",font=("times new roman",20,"bold"),bg="paleturquoise",fg="black")
        lbl_DOB.grid(row=7,column=0,pady=10,padx=20,sticky="w")

        txt_DOB=Entry(Manage_Frame,textvariable=self.Dob_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_DOB.grid(row=7,column=1,pady=10,padx=20,sticky="w")


        lbl_Email=Label(Manage_Frame,text="Email",font=("times new roman",20,"bold"),bg="paleturquoise",fg="black")
        lbl_Email.grid(row=8,column=0,pady=10,padx=20,sticky="w")

        txt_Email=Entry(Manage_Frame,textvariable=self.Email_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Email.grid(row=8,column=1,pady=10,padx=20,sticky="w")



### Button Frame ###

        btn_Frame=Frame(Manage_Frame,bd=5,relief=RIDGE,bg="turquoise")
        btn_Frame.place(x=5,y=550,width=410)


        Addbtn=Button(btn_Frame,text="Add",width=10,command=self.add_users,cursor="hand2").grid(row=0,column=0,padx=10,pady=10)
        Delbtn=Button(btn_Frame,text="Delete",width=10,command=self.delete_data,cursor="hand2").grid(row=0,column=1,padx=10,pady=10)
        Updbtn=Button(btn_Frame,text="Update",width=10,command=self.update_data,cursor="hand2").grid(row=0,column=2,padx=10,pady=10)
        Clrbtn=Button(btn_Frame,text="Back",width=10,command=go_back,cursor="hand2").grid(row=0,column=3,padx=10,pady=10)
        


#### Detail Frame ####


        Detail_Frame=Frame(self.root,bd=5,relief=RIDGE,bg="paleturquoise")
        Detail_Frame.place(x=460,y=65,width=875,height=625)



        lbl_search=Label(Detail_Frame,text="Search-By",font=("times new roman",20,"bold"),bg="paleturquoise",fg="black")
        lbl_search.grid(row=0,column=0,pady=10,padx=20,sticky="w")

        combo_search=ttk.Combobox(Detail_Frame,textvariable=self.search_by,width=12,font=("times new roman",13,"bold"),state='readonly')
        combo_search['values']=("nID","Name","Branch")
        combo_search.grid(row=0,column=1,pady=10,padx=20,sticky="w")


        txt_search=Entry(Detail_Frame,textvariable=self.search_txt,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_search.grid(row=0,column=2,pady=10,padx=20,sticky="w")


        searchbtn=Button(Detail_Frame,text="Search",width=15,pady=8,command=self.search_data,cursor="hand2").grid(row=0,column=3,padx=10,pady=10)
        showbtn=Button(Detail_Frame,text="Show All",width=15,pady=8,command=self.fetch_data,cursor="hand2").grid(row=0,column=4,padx=10,pady=10)



### Table Frame ###

        Table_Frame=Frame(Detail_Frame,bd=5,relief=RIDGE,bg='paleturquoise')
        Table_Frame.place(x=10,y=70,width=845,height=535)


        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
        self.User_Table=ttk.Treeview(Table_Frame,columns=("nID","Name","Branch","Semester","Division","Gender","DOB","Email"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.User_Table.xview)
        scroll_y.config(command=self.User_Table.yview)
        self.User_Table.heading("nID",text="nID")
        self.User_Table.heading("Name",text="Name")
        self.User_Table.heading("Branch",text="Branch")
        self.User_Table.heading("Semester",text="Semester")
        self.User_Table.heading("Division",text="Division")
        self.User_Table.heading("Gender",text="Gender")
        self.User_Table.heading("DOB",text="DOB")
        self.User_Table.heading("Email",text="Email")
        self.User_Table['show']='headings'
        self.User_Table.column("nID",width=100)
        self.User_Table.column("Name",width=150)
        self.User_Table.column("Branch",width=100)
        self.User_Table.column("Semester",width=100)
        self.User_Table.column("Division",width=100)
        self.User_Table.column("Gender",width=100)
        self.User_Table.column("DOB",width=100)
        self.User_Table.column("Email",width=200)
        self.User_Table.pack(fill=BOTH,expand=1)
        self.User_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()


### ADD ###

    def add_users(self):
        if self.nID_var.get()=="" or self.Name_var.get()=="" or self.Branch_var.get()=="" or self.Semester_var.get()=="" or self.Division_var.get()=="" or self.Gender_var.get()=="" or self.Dob_var.get()=="" or self.Email_var.get()=="":
                messagebox.showerror("Error!!","All Fields Are Mandatory")
        else:        
                conn=pymysql.connect(host="localhost",user="root",password="",database="ua")
                cur=conn.cursor()
                cur.execute("insert into users values(%s, %s, %s, %s, %s, %s, %s, %s)",(self.nID_var.get(),
                                                                                self.Name_var.get(),
                                                                                self.Branch_var.get(),
                                                                                self.Semester_var.get(),
                                                                                self.Division_var.get(),
                                                                                self.Gender_var.get(),
                                                                                self.Dob_var.get(),
                                                                                self.Email_var.get()
                                                                                ))
                conn.commit()
                self.fetch_data()
                self.clear()
                conn.close()    
                messagebox.showinfo("Success!!","Records Has Been Inserted")

### FETCH ###

    def fetch_data(self):
        conn=pymysql.connect(host="localhost",user="root",password="",database="ua")
        cur=conn.cursor()
        cur.execute("select * from users")
        rows = cur.fetchall()
        if len(rows)!=0:
                self.User_Table.delete(*self.User_Table.get_children())
                for rows in rows:
                        self.User_Table.insert('',END,values=rows)
                conn.commit()
        conn.close()        

### CLEAR ###

    def clear(self):
        self.nID_var.set(""),
        self.Name_var.set(""),
        self.Branch_var.set(""),
        self.Semester_var.set(""),
        self.Division_var.set(""),
        self.Gender_var.set(""),
        self.Dob_var.set(""),
        self.Email_var.set("")


### GET ###

    def get_cursor(self,ev):
        cursor_row = self.User_Table.focus()
        contents=self.User_Table.item(cursor_row)
        row=contents['values']
        self.nID_var.set(row[0]),
        self.Name_var.set(row[1]),
        self.Branch_var.set(row[2]),
        self.Semester_var.set(row[3]),
        self.Division_var.set(row[4]),
        self.Gender_var.set(row[5]),
        self.Dob_var.set(row[6]),
        self.Email_var.set(row[7])



### UPDATE ###

    def update_data(self):
        conn=pymysql.connect(host="localhost",user="root",password="",database="ua")
        cur=conn.cursor()
        cur.execute("update users set Name=%s,Branch=%s,Semester=%s,Division=%s,Gender=%s,Dob=%s,Email=%s where nID=%s",(     
                                                                        self.Name_var.get(),
                                                                        self.Branch_var.get(),
                                                                        self.Semester_var.get(),
                                                                        self.Division_var.get(),
                                                                        self.Gender_var.get(),
                                                                        self.Dob_var.get(),
                                                                        self.Email_var.get(),
                                                                        self.nID_var.get()
                                                                        ))
        conn.commit()
        self.fetch_data()
        self.clear()
        conn.close() 


### DELETE ###

    def delete_data(self):
        conn=pymysql.connect(host="localhost",user="root",password="",database="ua")
        cur=conn.cursor()
        cur.execute("delete from users where nID=%s",self.nID_var.get())
        conn.commit()
        conn.close()
        self.fetch_data()
        self.clear()


### SEARCH ###

    def search_data(self):
        if self.search_by.get()=="":
                messagebox.showerror("Error!!","Field Not Choosen")
        elif self.search_txt.get()=="":
                messagebox.showerror("Error!!","No Filters Applied")      
        else:        
                conn=pymysql.connect(host="localhost",user="root",password="",database="ua")
                cur=conn.cursor()
                cur.execute("select * from users where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
                rows = cur.fetchall()
                if len(rows)!=0:
                        self.User_Table.delete(*self.User_Table.get_children())
                        for rows in rows:
                                self.User_Table.insert('',END,values=rows)
                        conn.commit()
                conn.close()




obj=LMS(root)
root.mainloop()