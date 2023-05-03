from tkinter import*
from PIL import Image, ImageTk    #pip install pillow
from tkinter import messagebox
import sqlite3
import os

class Login_System:
    def __init__(self,root):
        self.root=root
        self.root.title("Login System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#fafafa")

        #====images==========
        self.phone_image=ImageTk.PhotoImage(file="Inventory images/phone.png")
        self.lbl_phone_image=Label(self.root,image=self.phone_image,bd=0).place(x=200,y=50)

        #====login frame=====
        self.employee_id=StringVar()
        self.password=StringVar()
        login_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        login_frame.place(x=650,y=90,width=350,height=460)

        title=Label(login_frame,text="Login System",font=("Elephant",30,"bold"),bg="white").place(x=0,y=30,relwidth=1)

        lbl_user=Label(login_frame,text="Employee_id",font=("Andalus",15,),bg="white",fg="#767171").place(x=50,y=100)
        txt_employee_id=Entry(login_frame,textvariable=self.employee_id,font=("times new roman",15),bg="#ECECEC").place(x=50,y=140,width=250)

        lbl_pass=Label(login_frame,text="Password",font=("Andalus",15,),bg="white",fg="#767171").place(x=50,y=200)
        txt_pass=Entry(login_frame,textvariable=self.password,show="*",font=("times new roman",15),bg="#ECECEC").place(x=50,y=240,width=250)

        btn_login=Button(login_frame,command=self.login,text="Log In",font=("Arial Rounded MT Bold",15),bg="#00B0F0",activebackground="#00B0F0",fg="white",activeforeground="white",cursor="hand2").place(x=50,y=300,width=250,height=35)

        hr=Label(login_frame,bg="lightgray").place(x=50,y=370,width=250,height=2)
        or_=Label(login_frame,text="OR",bg="white",fg="lightgray",font=("times new roman",15,"bold")).place(x=145,y=355)

        btn_forget=Button(login_frame,text="Forget Password?",command=self.forget_window,font=("times new roman",13),bg="white",fg="#00759E",bd=0,activebackground="white",activeforeground="#00759E").place(x=100,y=390)

        #====frame2======
        register_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        register_frame.place(x=650,y=570,width=350,height=60)
        lbl_reg=Label(register_frame,text="SUBSCRIBE | LIKE | SHARE",font=("times new roman",13),bg="white").place(x=60,y=0,relheight=1)

        #===Animation Images====
        self.im1=ImageTk.PhotoImage(file="Inventory images/im1.png")
        self.im2=ImageTk.PhotoImage(file="Inventory images/im2.png")
        self.im3=ImageTk.PhotoImage(file="Inventory images/im3.png")

        self.lbl_change_image=Label(self.root,bg="white")
        self.lbl_change_image.place(x=367,y=153,width=240,height=428)

        self.animate()

    def animate(self):
        self.im=self.im1
        self.im1=self.im2
        self.im2=self.im3
        self.im3=self.im
        self.lbl_change_image.config(image=self.im)
        self.lbl_change_image.after(2000,self.animate)


    def login(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.employee_id.get()=="" or self.password.get()=="":
                messagebox.showerror("Error","All fields are required",parent=self.root)
            else:    
                cur.execute("select utype from employee where eid=? AND pass=?",(self.employee_id.get(),self.password.get()))
                user=cur.fetchone()
                if user==None:
                    messagebox.showerror('Error',"Invalid USERNAME/PASSWORD",parent=self.root)
                else:
                    self.root.destroy()
                    os.system("python dashboard.py")    
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)    

    def forget_window(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        try:
            if self.employee_id.get()=="":
                messagebox.showerror('Error','Employee ID must be required',parent=self.root)
            else:
                cur.execute("select email from employee where eid=?",(self.employee_id.get(),))
                email=cur.fetchone()
                if email==None:
                    messagebox.showerror('Error',"Invalid Employee ID, Try again",parent=self.root)
                else: 
                    self.var_otp=StringVar()
                    self.var_new_pass=StringVar()
                    self.var_conf_pass=StringVar()

                    self.forget_win=Toplevel(self.root)
                    self.forget_win.title("RESET PASSWORD")
                    self.forget_win.geometry('400x350+500+100')
                    self.forget_win.focus_force()

                    title=Label(self.forget_win,text="Reset Password",font=("goudy old style",15,"bold"),bg="#3f51b5",fg="white").pack(side=TOP,fill=X)  

                    Label_new_pass=Label(self.forget_win,text="New Password",font=("times new roman",15)).place(x=35,y=60)
                    txt_new_pass=Entry(self.forget_win,textvariable=self.var_new_pass,show="*",font=("times new roman",15),bg="lightyellow").place(x=25,y=100,width=250,height=30)
                   
                    Label_conf_pass=Label(self.forget_win,text="Confirm Password",font=("times new roman",15)).place(x=35,y=150)
                    txt_conf_pass=Entry(self.forget_win,textvariable=self.var_conf_pass,show="*",font=("times new roman",15),bg="lightyellow").place(x=25,y=190,width=250,height=30)

                    self.btn_update=Button(self.forget_win,command=self.update,text="Update",font=("times new roman",15),bg="lightblue")
                    self.btn_update.place(x=150,y=270,width=100,height=30)   

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)    

    def update(self): 
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
                    con.commit()
                    messagebox.showinfo("Success","Password Updated Successfully",parent=self.root)
                    
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
            

root=Tk()
obj=Login_System(root)
root.mainloop()


