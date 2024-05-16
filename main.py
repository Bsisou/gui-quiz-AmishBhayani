# Import module 
from tkinter import *

def show_main_page():
    main_page_frame.pack(side="left", fill="both", expand=True)
    quiz_page_frame.pack_forget()

def show_quiz_page():
    main_page_frame.pack_forget()
    quiz_page_frame.pack(side="left", fill="both", expand=True)

# Main Page
def create_main_page_widgets(canvas):
    canvas.create_image(0, 0, image=bg, anchor="nw")
    canvas.create_text(400, 650, text="Enter Your Name:", font=('Cascadia Code', 50), fill='white')
    canvas.create_text(640, 250, text="Video Game", font=('Cascadia Code', 120, 'bold'), fill='white')
    canvas.create_text(300, 400, text="Quiz", font=('Cascadia Code', 120, 'bold'), fill='white')
    start_button = Button(canvas, text="Start", font=('Cascadia Code', 45), fg='white', bg='black', command=show_quiz_page)
    canvas.create_window(1650, 900, anchor="nw", window=start_button)
    input_widget = Entry(root, font=('Cascadia Code', 50), bg='white', fg='black')
    canvas.create_window(90, 700, window=input_widget, anchor="nw")

# Quiz Page
def create_quiz_page_widgets(canvas):
    canvas.create_image(0, 0, image=bg1, anchor="nw")
    canvas.create_text(480, 270, text="Quiz Page", font=('Cascadia Code', 30), fill='black')
    back_button = Button(canvas, text="Back to Main Page", font=('Cascadia Code', 15), fg='white', bg='black', command=show_main_page)
    canvas.create_window(850, 475, anchor="nw", window=back_button)

root = Tk() # Create object 
root.geometry("1920x1080") # Adjust size 

bg = PhotoImage(file="file.png") # Add image file
bg1 = PhotoImage(file="quizpage.png") # Add image file

main_page_frame = Frame(root)
quiz_page_frame = Frame(root)

main_canvas = Canvas(main_page_frame, width=1920, height=1080)
quiz_canvas = Canvas(quiz_page_frame, width=1920, height=1080)

create_main_page_widgets(main_canvas)
create_quiz_page_widgets(quiz_canvas)

create_main_page_widgets(main_canvas)
create_quiz_page_widgets(quiz_canvas)

show_main_page()  # Show main page by default

main_canvas.pack(fill="both", expand=True)
quiz_canvas.pack(fill="both", expand=True)

# Execute tkinter 
root.mainloop() 
