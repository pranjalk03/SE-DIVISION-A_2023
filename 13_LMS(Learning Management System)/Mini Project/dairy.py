from tkinter import  *
from tkinter import messagebox
import ast
from flask import Flask, render_template, request, redirect
from getpass import getpass

root=Tk()
root.title('Login')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False,False)
def open_main():
    root.destroy()
    import main


def signin():
    username=user.get()
    password=code.get()
    
    if not username or not password:
        messagebox.showerror('Invalid', 'Please enter both username and password')
        return  

    file=open('datasheet.txt','r')
    d=file.read()
    r=ast.literal_eval(d)
    file.close()

   # print(r.keys())
    # print(r.values())

    if username in r.keys() and password==r[username]:
        def open_main():
            root.destroy()
            import main
        open_main()
    else:
        messagebox.showerror('Invalid','invalid username or password')

def signup_command():
    window=Toplevel(root)
    window.title("SignUp")
    window.geometry('925x500+300+200')
    window.configure(bg='#fff')
    window.resizable(False,False)
    img = PhotoImage(file='C:\\Users\\arpit\\Desktop\\sumit\\login1.png')
    root.iconphoto(False, img)
    def signup():
        username=user.get()
        password=code.get()
        conform_password=conform_code.get()

        if password==conform_password:
           





            
            try:
                file=open('datasheet.txt','r+')
                d=file.read()
                r=ast.literal_eval(d)

                dict2={username:password}
                r.update(dict2)
                file.truncate(0)
                file.close()
    
                file=open('datasheet.txt','w')
                w=file.write(str(r))

                messagebox.showinfo('Signup','Sucessfully sign up')

            except:
                file=open('datasheet.txt','w')
                pp=str({'Username':'password'})
                file.write(pp)
                file.close()

        else:
            messagebox.showerror('Invalid', "Both password should match")

              
    def sign():
        window.destroy()
    img = PhotoImage(file='login1.png')
    Label(window,image=img,border=0,bg='white').place(x=50,y=90)

    frame=Frame(window,width=350,height=390,bg='white')
    frame.place(x=490,y=55)

    heading=Label(frame,text='Sign up',fg="#57a1f8",bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
    heading.place(x=140,y=5)

    def on_enter(e):
       user.delete(0, 'end')
    def on_leave(e):
        if user.get()=='':
            user.insert(0,'Username')
    user= Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11,))
    user.place(x=34,y=85)
    user.insert(0, 'Username')
    user.bind('<FocusIn>',on_enter)
    user.bind('<FocusOut>',on_leave)

    Frame(frame,width=240,height=2,bg='black').place(x=35,y=107)

    def on_enter(e):
        code.delete(0, 'end')
    def on_leave(e):
        if code.get()=='':
            code.insert(0,'Password')
    code= Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11,))
    code.place(x=34,y=150)
    code.insert(0, 'Password')
    code.bind('<FocusIn>',on_enter)
    code.bind('<FocusOut>',on_leave)

    Frame(frame,width=240,height=2,bg='black').place(x=35,y=177)

    def on_enter(e):
        conform_code.delete(0, 'end')
    def on_leave(e):
        if conform_code.get()=='':
            conform_code.insert(0,'Confirm Password')
    conform_code= Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11,))
    conform_code.place(x=34,y=225)
    conform_code.insert(0, 'Confirm Password')
    conform_code.bind('<FocusIn>',on_enter)
    conform_code.bind('<FocusOut>',on_leave)

    Frame(frame,width=240,height=2,bg='black').place(x=35,y=247)



    Button(frame,width=39,pady=7,text='Sign up',bg='#57a1f8',fg='white',border=0,command=signup).place(x=35,y=280)
    label=Label(frame,text="I have an account?",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
    label.place(x=90,y=340)

    signin= Button(frame,width=6,text="Sign in",border=0,bg='white',cursor='hand2',fg='#57a1f8',command=sign)
    signin.place(x=200,y=340)


    window.mainloop()



img = PhotoImage(file='C:\\Users\\arpit\\Desktop\\sumit\\login1.png')
root.iconphoto(False, img)

img=PhotoImage(file='login1.png')
Label(root,image=img,bg='white').place(x=50,y=50)

frame=Frame(root,width=350,height=350,bg='white')
frame.place(x=480,y=70)

heading=Label(frame,text='Sign in',fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
heading.place(x=120,y=10)
#############------------------------------
def on_enter(e):
    user.delete(0, 'end')
def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'Username')
user = Entry(frame,width=25,fg='black',border=0,bg="white",font=('Microsoft YaHei UI Light',11,))
user.place(x=60,y=110)
user.insert(0,'Username')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)

Frame(frame,width=280,height=2,bg='black').place(x=40,y=130)

#################-----------------------------
def on_enter(e):
    code.delete(0, 'end')
def on_leave(e):
    name=code.get()
    if name=='':
        code.insert(0,'Password')
code = Entry(frame,width=25,fg='black',border=0,bg="white",font=('Microsoft YaHei UI Light',11,))
code.place(x=60,y=166)
code.insert(0,'Password')
code.bind('<FocusIn>',on_enter)
code.bind('<FocusOut>',on_leave)

Frame(frame,width=280,height=2,bg='black').place(x=40,y=185)

Button(frame,width=39,pady=7,text='Sign-in',bg='#57a1f8',fg='white',border=0,command=signin).place(x=35,y=224)
label=Label(frame,text="Don't have an account?",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
label.place(x=75,y=270)



sign_up= Button(frame,width=6,text="Sign-Up",border=0,bg='white',cursor='hand2',fg='#57a1f8',command=signup_command)
sign_up.place(x=215,y=270)




root.mainloop()