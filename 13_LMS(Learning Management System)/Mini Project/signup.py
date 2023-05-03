from tkinter import *
from tkinter import messagebox
import ast

root=Tk()
root.title("SignUp")
root.geometry('925x500+300+200')
root.configure(bg='#fff')
root.resizable(False,False)
def open_main():
    root.destroy()
    import main
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
img = PhotoImage(file='C:\\Users\\arpit\\Desktop\\sumit\\login1.png')
root.iconphoto(False, img)
              
def sign():
    root.destroy()
img = PhotoImage(file='login1.png')
Label(root,image=img,border=0,bg='white').place(x=50,y=90)

frame=Frame(root,width=350,height=390,bg='white')
frame.place(x=490,y=55)

heading=Label(frame,text='Sign up',fg="#57a1f8",bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
heading.place(x=100,y=5)

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
def open_dairy():
    root.destroy()
    import dairy

Button(frame,width=39,pady=7,text='Sign up',bg='#57a1f8',fg='white',border=0,command=signup).place(x=35,y=280)
label=Label(frame,text="I have an account!",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
label.place(x=95,y=340)

signin= Button(frame,width=6,text="Sign in",border=0,bg='white',cursor='hand2',fg='#57a1f8',command=open_dairy)
signin.place(x=215,y=340)


root.mainloop()



