from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
root = Tk()
root.title('FAQs')
root.geometry('1062x700')
root.configure(bg="skyblue")
root.resizable(False, False)
img = PhotoImage(file='C:\\Users\\arpit\\Desktop\\sumit\\login1.png')
root.iconphoto(False, img)

# Define the questions and answers
questions = ['What does LMS mean for an organization?', 'What are the benefits of an LMS?', 'Why should I use an LMS?','What are the features of an LMS?','What is a Learning Management System?','Who is an LMS for?','Why Administrate LMS?']
answers = ['An LMS means you have an online tool to efficiently manage employee training, development, and engagement—your modern learning solution.An LMS is a website where your organization can put its training materials, frequently used documents, and communicate directly with your people. Plus, modern learning platforms are cloud-based. That allows your people access to critical information at the moment of need wherever they are.\nEach employee has their own individual profile in an LMS. Your LMS administrator operates the site. They make sure content is updated, organized, and easy-to-find.\n The admin is able to assign material to employees—individually or in groups,\norganized by profile fields like job title or location.\n', 
           'The primary benefits of using an LMS are in training and communication in one easily accessible platform.\n Content creation tools within the LMS power up course authoring for you to build learning paths, for things like onboarding and career development.\nCommunication-centric LMS features allow you to send updates to individuals, groups, and locations.\n Reporting tools confirm whether a person has read the message.\n An LMS empowers you to efficiently get the word out about anything, and be sure that the message was received.', 
           'You should use an LMS simply because it improves your people operations.\n The best LMS platforms fit the workflow of you and your people, making it easy to train,\n onboard new employees, and communicate consistently across the country in different locations.',
           'The key features of an LMS that empower you to accomplish all of those goals:Content \nmanagement tools\nAssessments and testingMobile\n optimization\nReporting\nCommunication\nGamification','A Learning Management System (LMS) is a tool designed to facilitate the administration, documentation, tracking, reporting, and delivery of online learning. Also called “e-learning”, the software provides a virtual classroom environment for trainers and training organisations that can be\n used by delegates to complete training courses.','Any organisation that provides training could make use of an LMS, particularly those organisations that\nNeed to provide lots of on-demand training to low numbers of students \nProvide classes or courses that are particularly well suited to e-learning such as employee initiations or internal training.\nWant to expand their business or offerings beyond their current geographic footprint\nWant to serve markets in languages that aren’t spoken by the trainers\nWant to design, build, and sell online content to other training organisations.\n',
           'We know there’s no shortage of Learning Management Systems out there, but there are some key differences between our offering and others out there\nAdministrate LMS is built to deeply integrate with the course management and training management functions of Administrate\nAdministrate LMS is a lower cost option than many LMS offerings out there\nAdministrate LMS provides extremely advanced customisation options that aren’t typical on many platforms']

# Create labels and buttons for each question and answer
for i in range(len(questions)):
    question_label = Label(root, text=questions[i], font=('Arial', 16), bg='white')
    question_label.pack(pady=10)
    answer_button = Button(root, text='Show Answer', command=lambda i=i: messagebox.showinfo('Answer', answers[i]))
    answer_button.pack(pady=5)
def open_main():
    root.destroy()
    import main
# Add a back button to return to the main page
def go_back():
    pass

back_button = Button(root, text="Back", font=('Arial', 16), width=20, height=2, command=open_main, activebackground="blue")
back_button.place(x=400, y=620)

root.mainloop()