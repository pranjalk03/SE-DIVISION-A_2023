from tkinter import *
from PIL import Image, ImageTk  # pip install pillow
from tkinter import messagebox
from tkinter import ttk
import pymysql
import webbrowser
root=Tk()
img = PhotoImage(file='C:\\Users\\arpit\\Desktop\\sumit\\login1.png')
root.iconphoto(False, img)
def open_url():
    webbrowser.open_new("https://drive.google.com/drive/folders/1l-t55M7JeFT1oFBUXhUGfvWjVRru0ph0")

def open_main():
      root.destroy()
      import main
def go_back():
    # define the action to perform when the back button is clicked
    # for example, you can close the current window and open the previous window

    back_button = Button(root, text="Back", command=go_back)
    back_button.pack(side=LEFT, padx=10, pady=10)


class LMS:    
    def __init__(self,root):
        self.root = root
        self.root.title("COURSE DETAILS")
        self.root.geometry("1350x700+0+0")
        self.root.resizable(False, False)

#### TITLE ####

        title=Label(self.root,text="Course Details",bd=5,relief=GROOVE,font=("times new roman",30,"bold"),bg="paleturquoise",fg="black")
        title.pack(side=TOP, fill=X)

# background
        root.MenuLogo = Image.open("bg1.jpg")
        root.MenuLogo = root.MenuLogo.resize((1350,720), Image.ANTIALIAS)
        root.MenuLogo = ImageTk.PhotoImage(root.MenuLogo)

        lbl_MenuLogo = Label(root, image=root.MenuLogo, bg="white")
        lbl_MenuLogo.pack(side=TOP, fill=X)


### All Variables ###

        self.cID_var=StringVar()
        self.Name_var=StringVar()
        self.Branch_var=StringVar()
        self.Semester_var=StringVar()
        self.Division_var=StringVar()
        self.Year_var=StringVar()
        self.cFaculty_var=StringVar()
        self.cMaterial_var=StringVar()


        self.search_by=StringVar()
        self.search_txt=StringVar()


#### Manage Frame ####

        Manage_Frame = Frame(self.root, bd=5, relief=RIDGE,bg="paleturquoise")
        Manage_Frame.place(x=10,y=65,width=430,height=625)

        m_title=Label(Manage_Frame,text="Manage Courses",font=("times new roman",20,"bold"),bg="paleturquoise",fg="black")
        m_title.grid(row=0,columnspan=2,pady=20)


        lbl_cID=Label(Manage_Frame,text="C-ID",font=("times new roman",20,"bold"),bg="paleturquoise",fg="black")
        lbl_cID.grid(row=1,column=0,pady=10,padx=20,sticky="w")

        txt_cID=Entry(Manage_Frame,textvariable=self.cID_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_cID.grid(row=1,column=1,pady=10,padx=20,sticky="w")


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


        lbl_Year=Label(Manage_Frame,text="Year",font=("times new roman",20,"bold"),bg="paleturquoise",fg="black")
        lbl_Year.grid(row=6,column=0,pady=10,padx=20,sticky="w")

        txt_Year=Entry(Manage_Frame,textvariable=self.Year_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Year.grid(row=6,column=1,pady=10,padx=20,sticky="w")


        lbl_cFaculty=Label(Manage_Frame,text="C-Faculty",font=("times new roman",20,"bold"),bg="paleturquoise",fg="black")
        lbl_cFaculty.grid(row=7,column=0,pady=10,padx=20,sticky="w")

        txt_cFaculty=Entry(Manage_Frame,textvariable=self.cFaculty_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_cFaculty.grid(row=7,column=1,pady=10,padx=20,sticky="w")


        lbl_cMaterial=Label(Manage_Frame,text="Drive-Link",font=("times new roman",20,"bold"),bg="paleturquoise",fg="black")
        lbl_cMaterial.grid(row=8,column=0,pady=10,padx=20,sticky="w")



### Button Frame ###

        btn_Frame=Frame(Manage_Frame,bd=5,relief=RIDGE,bg="turquoise")
        btn_Frame.place(x=5,y=550,width=410)


        Addbtn=Button(btn_Frame,text="Add",width=10,command=self.add_courses,cursor="hand2").grid(row=0,column=0,padx=10,pady=10)
        Delbtn=Button(btn_Frame,text="Delete",width=10,command=self.delete_data,cursor="hand2").grid(row=0,column=1,padx=10,pady=10)
        Updbtn=Button(btn_Frame,text="Update",width=10,command=self.update_data,cursor="hand2").grid(row=0,column=2,padx=10,pady=10)
        Clrbtn=Button(btn_Frame,text="Back",width=10,cursor="hand2",command=open_main).grid(row=0,column=3,padx=10,pady=10)


#### Detail Frame ####


        Detail_Frame=Frame(self.root,bd=5,relief=RIDGE,bg="paleturquoise")
        Detail_Frame.place(x=460,y=65,width=875,height=625)


        lbl_search=Label(Detail_Frame,text="Search-By",font=("times new roman",20,"bold"),bg="paleturquoise",fg="black")
        lbl_search.grid(row=0,column=0,pady=10,padx=20,sticky="w")

        combo_search=ttk.Combobox(Detail_Frame,textvariable=self.search_by,width=12,font=("times new roman",13,"bold"),state='readonly')
        combo_search['values']=("cID","Name","Branch")
        combo_search.grid(row=0,column=1,pady=10,padx=20,sticky="w")


        txt_search=Entry(Detail_Frame,textvariable=self.search_txt,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_search.grid(row=0,column=2,pady=10,padx=20,sticky="w")


        searchbtn=Button(Detail_Frame,text="Search",width=15,pady=8,command=self.search_data,cursor="hand2").grid(row=0,column=3,padx=10,pady=10)
        showbtn=Button(Detail_Frame,text="Show All",width=15,pady=8,command=self.fetch_data,cursor="hand2").grid(row=0,column=4,padx=10,pady=10)



### Table Frame ###

        Table_Frame=Frame(Detail_Frame,bd=5,relief=RIDGE,bg='paleturquoise')
        Table_Frame.place(x=10,y=70,width=845,height=535)



        link_label = Label(root, text="Upload Notes",font=("goudy",12),bd=4,relief=RIDGE, bg="white",fg="black", cursor="hand2")
        link_label.place(x=211,y=557,width=212,height=35)
        link_label.bind("<Button-1>", lambda e: open_url())



        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
        self.Course_Table=ttk.Treeview(Table_Frame,columns=("cID","Name","Branch","Semester","Division","Year","cFaculty"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Course_Table.xview)
        scroll_y.config(command=self.Course_Table.yview)
        self.Course_Table.heading("cID",text="C-ID")
        self.Course_Table.heading("Name",text="Name")
        self.Course_Table.heading("Branch",text="Branch")
        self.Course_Table.heading("Semester",text="Semester")
        self.Course_Table.heading("Division",text="Division")
        self.Course_Table.heading("Year",text="Year")
        self.Course_Table.heading("cFaculty",text="C-Faculty")
        self.Course_Table['show']='headings'
        self.Course_Table.column("cID",width=100)
        self.Course_Table.column("Name",width=150)
        self.Course_Table.column("Branch",width=100)
        self.Course_Table.column("Semester",width=100)
        self.Course_Table.column("Division",width=100)
        self.Course_Table.column("Year",width=100)
        self.Course_Table.column("cFaculty",width=100)
        self.Course_Table.pack(fill=BOTH,expand=1)
        self.Course_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()


### ADD ###

    def add_courses(self):
        if self.cID_var.get()=="" or self.Name_var.get()=="" or self.Branch_var.get()=="" or self.Semester_var.get()=="" or self.Division_var.get()=="" or self.Year_var.get()=="" or self.cFaculty_var.get()=="":
                messagebox.showerror("Error!!","All Fields Are Mandatory")
        else:        
                conn=pymysql.connect(host="localhost",user="root",password="",database="ua")
                cur=conn.cursor()
                cur.execute("insert into courses values(%s, %s, %s, %s, %s, %s, %s)",(self.cID_var.get(),
                                                                                self.Name_var.get(),
                                                                                self.Branch_var.get(),
                                                                                self.Semester_var.get(),
                                                                                self.Division_var.get(),
                                                                                self.Year_var.get(),
                                                                                self.cFaculty_var.get()
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
        cur.execute("select * from courses")
        rows = cur.fetchall()
        if len(rows)!=0:
                self.Course_Table.delete(*self.Course_Table.get_children())
                for rows in rows:
                        self.Course_Table.insert('',END,values=rows)
                conn.commit()
        conn.close()        

### CLEAR ###

    def clear(self):
        self.cID_var.set(""),
        self.Name_var.set(""),
        self.Branch_var.set(""),
        self.Semester_var.set(""),
        self.Division_var.set(""),
        self.Year_var.set(""),
        self.cFaculty_var.set("")


### GET ###

    def get_cursor(self,ev):
        cursor_row = self.Course_Table.focus()
        contents=self.Course_Table.item(cursor_row)
        row=contents['values']
        self.cID_var.set(row[0]),
        self.Name_var.set(row[1]),
        self.Branch_var.set(row[2]),
        self.Semester_var.set(row[3]),
        self.Division_var.set(row[4]),
        self.Year_var.set(row[5]),
        self.cFaculty_var.set(row[6])



### UPDATE ###

    def update_data(self):
        conn=pymysql.connect(host="localhost",user="root",password="",database="ua")
        cur=conn.cursor()
        cur.execute("update courses set Name=%s,Branch=%s,Semester=%s,Division=%s,Year=%s,cFaculty=%s where cID=%s",(     
                                                                        self.Name_var.get(),
                                                                        self.Branch_var.get(),
                                                                        self.Semester_var.get(),
                                                                        self.Division_var.get(),
                                                                        self.Year_var.get(),
                                                                        self.cFaculty_var.get(),
                                                                        self.cID_var.get()
                                                                        ))
        conn.commit()
        self.fetch_data()
        self.clear()
        conn.close() 


### DELETE ###

    def delete_data(self):
        conn=pymysql.connect(host="localhost",user="root",password="",database="ua")
        cur=conn.cursor()
        cur.execute("delete from courses where cID=%s",self.cID_var.get())
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
                cur.execute("select * from courses where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
                rows = cur.fetchall()
                if len(rows)!=0:
                        self.Course_Table.delete(*self.Course_Table.get_children())
                        for rows in rows:
                                self.Course_Table.insert('',END,values=rows)
                        conn.commit()
                conn.close()



obj=LMS(root)
root.mainloop()