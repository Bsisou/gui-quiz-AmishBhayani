from tkinter import *
import random

names_list = []
global questions_answers
asked = []

questions_answers = {
1: ["What must you do when you see blue and red flashing lights behind you?", 'Speed up to get out of the way', 'Slow down and drive carefully',
'Slow down and stop', 'Drive on as usual', 'Slow down and stop', 3],
2: ["You may stop on a motorway only:", 'if there is an emergency', 'To let down or pick up passengers', 'to make a U-turn',
'to stop and take a photo', 'if there is an emergency',1],
3: ["When coming up to a pedestrian crossing without a raised traffic island, what must you do?", "Speed up before the pedestrians cross",
'Stop and give way to pedestrians on any part of the crossing', "Sound the horn on your vehicle to warn the perestrians",
"slow down to 30kmh", 'Stop and give way to pedestrians on any part of the crossing',2],
4: ["Can you stop on a bus stop in a private motor vehicle?", 'Only between midnight and 6am', "Under no circumstances",
"When dropping off passengers", 'Only if it is less than 5 minutes',"Under no circumstances", 2],
5: ["What is the maximum speed you may drive if you have a 'space saver wheel' fitted? (km/h)", '70 km/h',
"100 km/h so you do not hold up traffic", "80 km/h and if the wheel spacer displays a lower limit that applies",
"90 km/h", "80 km/h and if the wheel spacer displays a lower limit that applies",3],
6: ["When following another vehicle on a dusty road, you should:", 'Speed up to get passed', "Turn your vehicle's windscreen wipers on",
"Stay back from the dust cloud", 'Turn your vehicles headlights on', "Stay back from the dust cloud", 3],
7: ["What does the sign containing the letters 'LSZ' mean", 'Low safety zone', "Low stability zone", "Lone star zone", 'Limited speed zone',
'Limited speed zone',4],
8: ["What speed are you allowed to pass a school bus that has stopped to let students get on or off?", '20 km/h', "30 km/h", "70 km/h",
'10 km/h', '20 km/h',1],
9: ["What is the maximum distance a load may extend in front of a car?", '2 meters forward of the front edge of the front seat',
"4 meters forward of the front edge of the front seat", "3 meters forward of the front edge of the front seat", '2.5 meters forward of the front edge of the back seat','3 meters forward of the front edge of the front seat',3],
10: ["To avoid being blinded by the headlights of another vehicle coming towards you what should you do?", 'Look to the left of the road', "Look to the centre of the road",'Wear sunglasses that have sufficient strength', 'Look to the right side of the road', 'Look to the left of the road',1],

}

def randomiser():
  global qnum 
  qnum = random.randint(1,10)
  if qnum not in asked: 
    asked.append(qnum)
  elif qnum in asked:
    randomiser()

randomiser()

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
    self.continue_button = Button(self.quiz_frame, text="Continue", font=("Helvetica", "13", "bold"), bg="grey", command=self.name_collection)
    self.continue_button.grid(row=3, pady=20)

  def name_collection(self):
    name=self.entry_box.get()
    names_list.append(name)
    self.quiz_frame.destroy()

#******************Starting Point Of Program******************#
randomiser()
if __name__ == "__main__":
  root=Tk()
  root.title("Quiz")
  QuizStarter_object = QuizStarter(root)
  root.mainloop()