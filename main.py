from tkinter import *

class QuizStarter:
  def __init__(self, parent):
    background_color="OldLace"
    #frame set up
    self.quiz_frame=Frame(parent, bg=background_color, padx=100, pady=100)
    self.quiz_frame.grid()

    #Label widget for our heading
    self.heading_label=Label(self.quiz_frame, text="Quiz", font=("Tw Cen MT", "18", "bold"), bg=background_color)
    self.heading_label.grid(row=0)

    #Label widget for our user name prompt
    self.user_label = Label (self.quiz_frame, text="Please enter your name below", font=("Tw Cen MT", "16"), bg=background_color)
    self.user_label.grid(row=1, pady=20)

    #user input
    self.entry_box=Entry(self.quiz_frame)
    self.entry_box.grid(row=2, pady=20)

    #continue button
    self.continue_button = Button(self.quiz_frame, text="Continue", font=("Helvetica", "13", "bold"), bg="pink", command=self.name_collection)
    self.continue_button.grid(row=3, pady=20)

  def name_collection(self)



#******************Starting Point Of Program******************#
if __name__ == "__main__":
  root=Tk()
  root.title("Quiz")
  QuizStarter_object = QuizStarter(root)
  root.mainloop()