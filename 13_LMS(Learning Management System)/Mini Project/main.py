from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter import ttk

def logout():
    result = messagebox.askquestion("Logout", "Are you sure you want to logout?")
    if result == 'yes':
        root.destroy()
        import dairy
        open_dairy
        # Here you can add code to logout the user
    else:
        messagebox.destroy()
        open_dairy()

def open_dairy():
    root.destroy()
    import dairy


def open_realuser():
    root.destroy() # close the current window
    import realuser # import the admin_panel file



def open_combination():
    root.destroy()
    import combination

def open_realblog():
    root.destroy()
    import realblog


def open_faq():
    root.destroy()  # close the current window
    import faq # import the admin_panel file

def open_faq1():
    root.destroy()
    import faq1






root = Tk()
root.title('LMS')
root.geometry('1250x645')
root.configure(bg="#fff")
root.resizable(False,False)

# window photo
img = PhotoImage(file='C:\\Users\\arpit\\Desktop\\sumit\\login1.png')
root.iconphoto(False, img)

# background
root.MenuLogo = Image.open("bg1.jpg")
root.MenuLogo = root.MenuLogo.resize((1250,645), Image.ANTIALIAS)
root.MenuLogo = ImageTk.PhotoImage(root.MenuLogo)



# load the bell icon image

lbl_MenuLogo = Label(root, image=root.MenuLogo, bg="royalblue")
lbl_MenuLogo.pack(side=TOP, fill=X)

# title
title = Label(root, text="NeXUS", font=("goudy new style",20,"bold"), fg="white", bg="royalblue", anchor="w")
title.place(x=0, y=0, width=1350, height=50)

home_title = Label(root, text="APSIT",font=("times new roman",20,"bold"), bg="deepskyblue", anchor="w")
home_title.place(x=230, y=50, width=1350, height=60)

# left menu
LeftMenu = Frame(root, bd=2, relief=RIDGE, bg="darkorchid")
LeftMenu.place(x=0, y=50, width=230, height=750)

btn_hom = Button(LeftMenu, text="HOME", font=("times new roman",20,"bold"), height=2, fg="black",bg='cyan',cursor="hand2")
btn_hom.pack(side=TOP, fill=X)
btn_ap = Button(LeftMenu, text="USERS", font=("times new roman",20,"bold"), height=2, fg="black", bg='cyan', cursor="hand2", command=open_realuser)
btn_ap.pack(side=TOP, fill=X)
btn_cou = Button(LeftMenu, text="COURSES", font=("times new roman",20,"bold"), height=2, fg="black", bg='cyan', cursor="hand2", command=open_combination)
btn_cou.pack(side=TOP, fill=X)
btn_ud = Button(LeftMenu, text="BADGES", font=("times new roman",20,"bold"), height=2, fg="black", bg='cyan', cursor="hand2")
btn_ud.pack(side=TOP, fill=X)
btn_bad = Button(LeftMenu, text="BLOGS", font=("times new roman",20,"bold"), height=2, fg="black", bg='cyan', cursor="hand2",command=open_realblog)
btn_bad.pack(side=TOP, fill=X)
btn_blo = Button(LeftMenu, text="FAQ's", font=("times new roman",20,"bold"), height=2, fg="black", bg='cyan', cursor="hand2",command=open_faq1)
btn_blo.pack(side=TOP, fill=X)
btn_set = Button(LeftMenu, text="LOGOUT", font=("times new roman",20,"bold"), height=2, fg="black", bg='cyan', cursor="hand2",command=logout)
btn_set.pack(side=TOP, fill=X)



root.mainloop()