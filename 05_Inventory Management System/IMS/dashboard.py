from tkinter import*
from PIL import Image, ImageTk    #pip install pillow
import os
from employee import employeeClass
from supplier import supplierClass
from category import categoryClass
from product import productClass
from sales import salesClass
class IMS:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Management System")
        self.root.config(bg="white")
        
        #===tittle===
        self.icon_title=PhotoImage(file="Inventory images/logo1.png")
        title=Label(self.root,text="Inventory Managemant System",font=("times new roman",40,"bold"),bg="#010c48",fg="white",padx=20).place(x=0,y=0,relwidth=1,height=70)
        
        #===button_logout===
        Button_logout=Button(self.root,text="Logout",command=self.logout,font=("Times new roman",15,"bold"),bg="yellow",cursor="hand2").place(x=1150,y=10,height=50,width=150)
        
         #===clock===
        self.lable_clock=Label(self.root,text="Welcome to Inventory Managemant System\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS",font=("times new roman",15),bg="#4d636d",fg="white")
        self.lable_clock.place(x=0,y=70,relwidth=1,height=30)

        #===Left Menu===
        self.MenuLogo=Image.open("Inventory images/menu_im.png")
        self.MenuLogo=self.MenuLogo.resize((200,200),Image.ANTIALIAS)
        self.MenuLogo=ImageTk.PhotoImage(self.MenuLogo)

        LeftMenu=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        LeftMenu.place(x=0,y=102,width=200,height=565)
    
        Label_MenuLogo=Label(LeftMenu,image=self.MenuLogo)
        Label_MenuLogo.pack(side=TOP,fill=X)
        
        self.icon_side=PhotoImage(file="Inventory Images/side.png")

        self.icon_side
        Label_Menu=Label(LeftMenu,text="Menu",font=("times new roman",20),bg="#009688").pack(side=TOP,fill=X)
        Label_MenuLogo=Label(LeftMenu,image=self.MenuLogo)


        
        Button_Employee=Button(LeftMenu,text="Employee",anchor="w",command=self.employee,font=("times new roman",19,"bold"),padx=5,bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        Button_Suplier=Button(LeftMenu,text="Suplier",command=self.supplier,font=("times new roman",19,"bold"),padx=5,anchor="w",bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        Button_Category=Button(LeftMenu,text="Category",command=self.category,font=("times new roman",19,"bold"),padx=5,anchor="w",bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        Button_Product=Button(LeftMenu,text="Product",command=self.product,font=("times new roman",19,"bold"),padx=5,anchor="w",bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        Button_Sales=Button(LeftMenu,text="Sales",command=self.sales,font=("times new roman",19,"bold"),padx=5,anchor="w",bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        Button_Exit=Button(LeftMenu,text="Exit",font=("times new roman",19,"bold"),padx=5,anchor="w",bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)

        #===content===
        self.lbl_Employee=Label(self.root,text="Total Employee\n[ 2 ]",bd=5,relief=RIDGE,background="#33bbf9",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_Employee.place(x=300,y=120,height=150,width=300)
        
        self.lbl_Suplier=Label(self.root,text="Total Suplier\n[ 0 ]",bd=5,relief=RIDGE,background="#ff5722",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_Suplier.place(x=650,y=120,height=150,width=300)

        self.lbl_Category=Label(self.root,text="Total Category\n[ 2 ]",bd=5,relief=RIDGE,background="#009688",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_Category.place(x=1000,y=120,height=150,width=300)

        self.lbl_Product=Label(self.root,text="Total Product\n[ 2 ]",bd=5,relief=RIDGE,background="#607d8b",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_Product.place(x=300,y=300,height=150,width=300)
        
        self.lbl_Sales=Label(self.root,text="Total Sales\n[ 6 ]",bd=5,relief=RIDGE,background="#ffc107",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_Sales.place(x=650,y=300,height=150,width=300)

        #===footer===
        lable_footer=Label(self.root,text="IMS-Inventory Managemant System\nFor any Technical Issue Contact: 987xxxxx01",font=("times new roman",12),bg="#4d636d",fg="white").pack(side=BOTTOM,fill=X)
 
 #===========================================================================================================================================================================================================================

    def employee(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=employeeClass(self.new_win)

    def supplier(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=supplierClass(self.new_win)    

    def category(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=categoryClass(self.new_win) 

    def product(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=productClass(self.new_win) 

    def sales(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=salesClass(self.new_win) 

    def logout(self):
        self.root.destroy()
        os.system("python login.py")    

if __name__=="__main__":       
    root=Tk()
    obj=IMS(root)
    root.mainloop()