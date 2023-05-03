from tkinter import *
from PIL import Image, ImageTk  # pip install pillow
from tkinter import messagebox
from tkinter import ttk
import pymysql
root=Tk()
def open_main():
    root.destroy()
        # close the current window
    import main
    open_main# import the admin_panel file

def go_back():
    root.destroy()# define the action to perform when the back button is clicked
    import main
    open_main()
    back_button = Button(root, text="Back", command=open_main)
    back_button.pack(side=LEFT, padx=10, pady=10)
img = PhotoImage(file='C:\\Users\\arpit\\Desktop\\sumit\\login1.png')
root.iconphoto(False, img)





class LMS:
    def fetch_data(self):
        conn=pymysql.connect(host="localhost",user="root",password="",database="blogs")
        cur=conn.cursor()
        cur.execute("select * from blogs")
        rows = cur.fetchall()
        
        conn.close()  
        return rows      

    
    def open_main():
        root.destroy()
        import main
        rows = obj.fetch_data()
        main.display_data(rows)



        
    def __init__(self,root):
        self.root = root
        self.root.title("BLOGS")
        self.root.geometry("720x720+0+0")
        self.root.resizable(False, False)

#### TITLE ####

        title=Label(self.root,text="BLOGS",bd=5,relief=GROOVE,font=("times new roman",30,"bold"),bg="paleturquoise",fg="black")
        title.pack(side=TOP, fill=X)

### Background ###
        root.MenuLogo = Image.open("bg1.jpg")
        root.MenuLogo = root.MenuLogo.resize((1350,720), Image.ANTIALIAS)
        root.MenuLogo = ImageTk.PhotoImage(root.MenuLogo)

        lbl_MenuLogo = Label(root, image=root.MenuLogo, bg="white")
        lbl_MenuLogo.pack(side=TOP, fill=X)

#### Manage Frame ####

        Manage_Frame = Frame(self.root, bd=5, relief=RIDGE,bg="paleturquoise")
        Manage_Frame.place(x=10,y=65,width=695,height=640)



        lbl_b=Label(Manage_Frame,text="Write Here....",font=("times new roman",20,"bold"),bg="paleturquoise",fg="black")
        lbl_b.place(x=15,y=25)

        txt_b=Text(Manage_Frame,font=("times new roman",15,"bold"),bd=5,relief=RIDGE)
        txt_b.place(x=15,y=75,width=655,height=485)

### Button Frame ###

        btn_Frame=Frame(Manage_Frame,bd=5,relief=RIDGE,bg="turquoise")
        btn_Frame.place(x=205,y=560,width=320)

        Addbtn=Button(btn_Frame,text="Post",width=15,height=2,cursor="hand2")
        Addbtn.grid(row=1,column=0,pady=10,padx=20)    

        Addbtn=Button(btn_Frame,text="Back",width=15,height=2,cursor="hand2",command=go_back)
        Addbtn.grid(row=1,column=1,pady=10,padx=20)

def post_blog():
    # get the blog text from the Text widget
        blog_text = conn.get('1.0', 'end-1c')
    
    # insert the blog into the database
        conn = pymysql.connect(host="localhost", user="root", password="", database="blogs")
        cur = conn.cursor()
        cur.execute("INSERT INTO blogs (blog_text) VALUES (%s)", (blog_text,))
        conn.commit()
        conn.close()

    # show success message
        messagebox.showinfo("Success", "Blog posted successfully.")      

obj=LMS(root)
root.mainloop()        