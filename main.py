from tkinter import *

class QuizApplication:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080")

        # Load images
        self.bg = PhotoImage(file="file.png")
        self.bg1 = PhotoImage(file="quizpage.png")

        # Initialize frames
        self.main_page_frame = Frame(self.root)
        self.quiz_page_frame = Frame(self.root)
        self.result_frame = Frame(self.root)

        # Initialize canvases
        self.main_canvas = Canvas(self.main_page_frame, width=1920, height=1080)
        self.quiz_canvas = Canvas(self.quiz_page_frame, width=1920, height=1080)
        self.result_canvas = Canvas(self.result_frame, width=1920, height=1080)

        # Global variables
        self.quiz_data = {
            "In which year was the iconic game, 'Super Mario Bros', first released?": ["1983", "1985", "1987", "1990"],
            "Which video game has a battle royale mode called 'Warzone'?": ["Call of Duty", "Battlefield", "Halo", "Fortnite"],
            "What is the highest-selling video game of all time?": ["GTA 5", "Minecraft", "Tetris", "Fortnite"],
            "In the game 'Minecraft', what material must players mine to obtain diamonds?": ["Dirt", "Stone", "Iron", "Coal"],
            "What is the most popular console in the world?": ["PS2", "PS4", "XBox 360", "PS5"],
            "What is the name of the city in the game 'Grand Theft Auto V'?": ["Liberty City", "Los Santos", "Vice City", "San Andreas"],
            "What is the primary objective in the game 'Fortnite'?": ["Build structures", "Collect coins", "Solve puzzles", "Survive"],
            "Which Professor provides players with their first Pokémon?": ["Professor Oak", "Professor Birch", "Professor Elm", "Professor Curry"],
            "Which game is played by people that don't take showers?": ["Valorant", "Fortnite", "Minecraft", "Tetris"],
            "Which game was responsible for about 145,000 car accidents?": ["GTA 5", "Genshin Impact", "Pokémon GO", "Tetris"],
        }

        self.correct_answers = {
            "In which year was the iconic game, 'Super Mario Bros', first released?": "1985",
            "Which video game has a battle royale mode called 'Warzone'?": "Call of Duty",
            "What is the highest-selling video game of all time?": "Minecraft",
            "In the game 'Minecraft', what material must players mine to obtain diamonds?": "Iron",
            "What is the most popular console in the world?": "PS2",
            "What is the name of the city in the game 'Grand Theft Auto V'?": "Los Santos",
            "What is the primary objective in the game 'Fortnite'?": "Survive",
            "Which Professor provides players with their first Pokémon?": "Professor Oak",
            "Which game is played by people that don't take showers?": "Valorant",
            "Which game was responsible for about 145,000 car accidents?": "Pokémon GO",
        }

        self.questions = list(self.quiz_data.keys())
        self.current_question_index = 0
        self.score = 0

        # Create widgets
        self.create_main_page_widgets(self.main_canvas)
        self.create_quiz_page_widgets(self.quiz_canvas)
        self.create_result_page_widgets(self.result_canvas)

        # Pack canvases
        self.main_canvas.pack(fill="both", expand=True)
        self.quiz_canvas.pack(fill="both", expand=True)
        self.result_canvas.pack(fill="both", expand=True)

        # Show main page by default
        self.show_main_page()

    def show_main_page(self):
        self.main_page_frame.pack(side="left", fill="both", expand=True)
        self.quiz_page_frame.pack_forget()
        self.result_frame.pack_forget()

    def show_quiz_page(self):
        self.main_page_frame.pack_forget()
        self.quiz_page_frame.pack(side="left", fill="both", expand=True)
        self.result_frame.pack_forget()
        self.load_question()

    def end_quiz(self):
        self.quiz_page_frame.pack_forget()
        self.result_frame.pack(side="left", fill="both", expand=True)
        self.result_canvas.create_text(960, 540, text=f"Your final score is: {self.score}", font=('Cascadia Code', 80), fill='white')

    def load_question(self):
        question = self.questions[self.current_question_index]
        answers = self.quiz_data[question]

        # Update the question text
        if len(question) <= 40:
            self.quiz_canvas.itemconfig(self.question_text_item, text=question)
        else:
            first_line = question[:question.find(' ', len(question) // 2)]
            second_line = question[question.find(' ', len(question) // 2):]
            self.quiz_canvas.itemconfig(self.question_text_item, text=first_line + '\n' + second_line)

        # Update buttons with answers and bind them to check_answer
        self.option1.config(text=answers[0], command=lambda: self.check_answer(answers[0]))
        self.option2.config(text=answers[1], command=lambda: self.check_answer(answers[1]))
        self.option3.config(text=answers[2], command=lambda: self.check_answer(answers[2]))
        self.option4.config(text=answers[3], command=lambda: self.check_answer(answers[3]))

    def check_answer(self, selected_answer):
        question = self.questions[self.current_question_index]
        if selected_answer == self.correct_answers[question]:
            self.score += 1
        self.score_label.config(text=f"Score: {self.score}")
        self.next_question()

    def next_question(self):
        self.current_question_index += 1
        if self.current_question_index < len(self.questions):
            self.load_question()
        else:
            self.end_quiz()

    def create_main_page_widgets(self, canvas):
        canvas.create_image(0, 0, image=self.bg, anchor="nw")
        canvas.create_text(400, 650, text="Enter Your Name:", font=('Cascadia Code', 50), fill='white')
        canvas.create_text(640, 250, text="Video Game", font=('Cascadia Code', 120, 'bold'), fill='white')
        canvas.create_text(300, 400, text="Quiz", font=('Cascadia Code', 120, 'bold'), fill='white')

        self.start_button = Button(canvas, text="Start", font=('Cascadia Code', 45), fg='white', bg='black', command=self.show_quiz_page)
        self.start_button.config(state='disabled') #Initially disabled
        canvas.create_window(1650, 900, window=self.start_button)

        #Variable for entry
        self.name_var = StringVar()
        self.name_var.trace_add("write", self.validate_name) # Attach Validation

        self.input_widget = Entry(self.root, font=('Cascadia Code', 50), bg='white', fg='black', textvariable=self.name_var)
        canvas.create_window(90, 700, window=self.input_widget, anchor="nw")

    def create_quiz_page_widgets(self, canvas):
        canvas.create_image(0, 0, image=self.bg1, anchor="nw")
        back_button = Button(canvas, text="Back", font=('Cascadia Code', 45), fg='white', bg='black', command=self.show_main_page)
        canvas.create_window(100, 900, anchor="nw", window=back_button)

        self.option1 = Button(canvas, font=('Cascadia Code', 60), fg='black', bg='light gray', width=12)
        self.option1.place(x=375, y=600)
        self.option2 = Button(canvas, font=('Cascadia Code', 60), fg='black', bg='light gray', width=12)
        self.option2.place(x=1025, y=600)
        self.option3 = Button(canvas, font=('Cascadia Code', 60), fg='black', bg='light gray', width=12)
        self.option3.place(x=375, y=750)
        self.option4 = Button(canvas, font=('Cascadia Code', 60), fg='black', bg='light gray', width=12)
        self.option4.place(x=1025, y=750)

        self.question_text_item = canvas.create_text(1000, 350, text="", font=('Cascadia Code', 60), fill='white')

        self.score_label = Label(canvas, text=f"Score: {self.score}", font=('Cascadia Code', 45), fg='white', bg='black')
        self.score_label.place(x=1650, y=50)

    def create_result_page_widgets(self, canvas):
        canvas.create_image(0, 0, image=self.bg1, anchor="nw")
        canvas.create_text(960, 250, text="Result Page", font=('Cascadia Code', 80, 'bold'), fill='white')
        back_button = Button(canvas, text="Back", font=('Cascadia Code', 45), fg='white', bg='black', command=self.show_main_page)
        canvas.create_window(100, 900, anchor="nw", window=back_button)

    def validate_name(self, *args):
        name = self.name_var.get()
        if name.isalnum() and name !="":
            self.start_button.config(state='normal')
        else:
            self.start_button.config(state='disabled')

# Initialize the main Tkinter window and run the application
if __name__ == "__main__":
    root = Tk()
    app = QuizApplication(root)
    root.mainloop()

