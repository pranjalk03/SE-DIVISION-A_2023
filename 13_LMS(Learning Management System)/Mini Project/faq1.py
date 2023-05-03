from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
root=Tk()
root.MenuLogo = Image.open("lms.jpg")
root.MenuLogo = root.MenuLogo.resize((1250,645), Image.ANTIALIAS)
root.MenuLogo = ImageTk.PhotoImage(root.MenuLogo)

class MSG:
    def __init__(self,root):
        self.root = root
        self.root.title("FAQ's")
        self.root.geometry("1350x700+0+0")
        self.root.resizable(False, False)



        title=Label(self.root,text="FAQ's",bd=5,relief=GROOVE,font=("times new roman",30,"bold"),bg="paleturquoise",fg="black")
        title.pack(side=TOP, fill=X)

        Manage_Frame = Frame(self.root, bd=5, relief=RIDGE,bg="paleturquoise")
        Manage_Frame.place(x=10,y=65,width=1330,height=625)
        
        # Define the questions and answers
        questions = ['         What Is A LMS           ','    How To Add New Users   ','  How to Add New Courses  ',' How Can I Add C-Materials ','       Who Is An LMS For       ','     Why Administrate LMS     ']
        answers = ['LMS stands for Learning Management System, a software platform used by schools, universities, and businesses for online learning and training programs. It facilitates the management and delivery of educational content and courses, including features for creating and organizing course content, tracking student progress and performance, and communication and collaboration tools.',
                    'To add an user, select the user section and input the necessary details in the corresponding boxes. Once completed, click on the "add" button.',
                    'To add a course, select the course section and input the necessary details in the corresponding boxes. Once completed, click on the "add" button.',
                    'To upload your notes, simply click on the "add notes" button, which will redirect you to a Drive link. Here, you can create folders as needed and upload your notes to the appropriate folder.',
                    'An LMS (Learning Management System) is for anyone who wants to manage and deliver educational content and courses online, such as schools, universities, and businesses.',
                    'Administering an LMS (Learning Management System) allows organizations to efficiently manage and deliver educational content and courses online. This can improve the learning experience for students, reduce administrative workload, and increase organizational efficiency.']

        # Create labels and buttons for each question and answer
        for i in range(len(questions)):
                question_label = Label(Manage_Frame, text=questions[i], font=('Arial', 16), bg='turquoise')
                question_label.pack(pady=10)
                answer_button = Button(Manage_Frame, text='Show Answer', command=lambda i=i: messagebox.showinfo('Answer', answers[i]))
                answer_button.pack(pady=5)
        def open_main():
                root.destroy()
                import main
                # Add a back button to return to the main page
        def go_back():
                pass

        Table_Frame = Frame(self.root, bd=5, relief=RIDGE,bg="paleturquoise")
        Table_Frame.place(x=10,y=620,width=1330,height=70)



        back_button = Button(Table_Frame, text="Back", font=('Goudy', 16), width=7, height=1, command=open_main, activebackground="blue")
        back_button.place(x=613, y=10)






obj=MSG(root)
root.mainloop()
