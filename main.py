# Import module 
from tkinter import *

def show_main_page():
    main_page_frame.pack()
    quiz_page_frame.pack_forget()

def show_quiz_page():
    main_page_frame.pack_forget()
    quiz_page_frame.pack()

# Create object 
root = Tk()

# Adjust size 
root.geometry("1920x1080") 

# Main Page
bg = PhotoImage(file="file.png") # Add image file
main_page_frame = Frame(root)
canvas1 = Canvas(main_page_frame, width=1920, height=1080)
canvas1.pack(fill="both", expand=True)
canvas1.create_image(0, 0, image=bg, anchor="nw")
canvas1.create_text( 220, 550, text = "Welcome", font=('Cascadia Code', 50), fill='white') 
canvas1.create_text( 520, 200, text = "Video Game", font=('Cascadia Code', 100, 'bold'), fill='white')
canvas1.create_text(240, 350, text="Quiz", font=('Cascadia Code', 100, 'bold'), fill='white')
start_button = Button(canvas1, text="Start", font=('Cascadia Code', 35), fg='white', bg='black', command=show_quiz_page)
start_button_canvas = canvas1.create_window(1700, 725, anchor="nw", window=start_button)
input_widget = Entry(root, font=('Cascadia Code', 40), bg='white', fg='black')
canvas1.create_window(60, 600, window=input_widget, anchor="nw")


# Quiz Page
quiz_page_frame = Frame(root)
quiz_canvas = Canvas(quiz_page_frame, width=960, height=540)
quiz_canvas.pack(fill="both", expand=True)

show_main_page()  # Show main page by default

# Execute tkinter 
root.mainloop() 
