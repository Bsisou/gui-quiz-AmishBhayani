# Import module 
from tkinter import *

def show_main_page():
    main_page_frame.pack(side="left", fill="both", expand=True)
    quiz_page_frame.pack_forget()

def show_quiz_page():
    main_page_frame.pack_forget()
    quiz_page_frame.pack(side="left", fill="both", expand=True)
    load_question()

def end_quiz():
    quiz_page_frame.pack_forget()
    
# Dictiory of questions and answers
quiz_data = {
    "In which year was the iconic game, 'Super Mario Bros.' released?": ["1983", "1985", "1987", "1989"],
    "Which video game has a battle royale mode called, 'Warzone'?": ["Fortnite", "Apex Legends", "Call of Duty", "Warzone"],
    "What is the highest-selling video game of all time?": ["Minecraft", "GTA 5", "Tetris", "Fortnite"],
    "In the game 'Minecraft', what material must players mine to obtain diamonds?": ["Dirt", "Stone", "Iron", "Coal"],
    "What is the most popular console in the world?": ["PS2", "PS4", "XBox 360", "PS5"],
    "What is the name of the city in the game 'Grand Theft Auto V'?": ["Liberty City", "Los Santos", "Vice City", "San Andreas"],
    "What is the primary objective in the game 'Fortnite'?": ["Build structures", "Collect coins", "Solve puzzles", "Survive"],
    "Which Professor provides players with their first Pokémon?": ["Professor Oak", "Professor Birch", "Professor Elm", "Professor Curry"],
    "Which game is played by people that don't take showers?": ["Valorant", "Fortnite", "Minecraft", "Tetris"],
    "Which game was responsible for about 145,000 car accidents?": ["GTA 5", "Genshin Impact", "Pokémon GO", "Tetris"],
}

# Correct answers corresponding to the questions
correct_answers = {
    "In which year was the iconic game, 'Super Mario Bros.' released?": "1985",
    "Which video game has a battle royale mode called, 'Warzone'?": "Call of Duty",
    "What is the highest-selling video game of all time?": "Minecraft",
    "In the game 'Minecraft', what material must players mine to obtain diamonds?": "Iron",
    "What is the most popular console in the world?": "PS2",
    "What is the name of the city in the game 'Grand Theft Auto V'?": "Los Santos",
    "What is the primary objective in the game 'Fortnite'?": "Survive",
    "Which Professor provides players with their first Pokémon?": "Professor Oak",
    "Which game is played by people that don't take showers?": "Valorant",
    "Which game was responsible for about 145,000 car accidents?": "Pokémon GO",
}

#list of questions extracted from the dictionary keys
questions = list(quiz_data.keys())

#create variable to keep track of the current question
current_question_index = 0

#variable to keep track of the score
score = 0

def load_question():
    global current_question_index
    question = questions[current_question_index]
    answers = quiz_data[question]

    quiz_canvas.itemconfig(question_text_item, text=question)
    
    option1.config(text=answers[0], command=lambda: check_answer(answers[0]))
    option2.config(text=answers[1], command=lambda: check_answer(answers[1]))
    option3.config(text=answers[2], command=lambda: check_answer(answers[2]))
    option4.config(text=answers[3], command=lambda: check_answer(answers[3]))


def check_answer(selected_answer):
    global score
    question = questions[current_question_index]
    if selected_answer == correct_answers[question]:
        score += 1
    score_label.config(text=f"Score: {score}")
    next_question()

def next_question():
    global current_question_index
    current_question_index += 1
    if current_question_index < len(questions):
        load_question()
    else:
        end_quiz()

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
    back_button = Button(canvas, text="Back", font=('Cascadia Code', 45), fg='white', bg='black', command=show_main_page)
    canvas.create_window(100, 900, anchor="nw", window=back_button)

    global option1, option2, option3, option4
    option1 = Button(canvas, text="", font=('Cascadia Code', 60), fg='black', bg='light gray', width=12)
    option1.place(x=375, y=600)  
    option2 = Button(canvas, text="", font=('Cascadia Code', 60), fg='black', bg='light gray', width=12)
    option2.place(x=1025, y=600)  
    option3 = Button(canvas, text="", font=('Cascadia Code', 60), fg='black', bg='light gray', width=12)
    option3.place(x=375, y=750) 
    option4 = Button(canvas, text="", font=('Cascadia Code', 60), fg='black', bg='light gray', width=12)
    option4.place(x=1025, y=750)  
    
    global question_text_item
    question_text_item = canvas.create_text(1000, 350, text="", font=('Cascadia Code', 60), fill='white')

    global score_label
    score_label = Label(canvas, text=f"Score: {score}", font=('Cascadia Code', 45), fg='white', bg='black')
    score_label.place(x=1650, y=50)


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
