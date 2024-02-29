from tkinter import *
import random
def get_computer_choice():
    a= random.choice(['rock', 'paper', 'scissors'])
    e2.insert(0,a)
    return a
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or (user_choice == 'paper' and computer_choice == 'rock') or  (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"
def play_game():
    user_choice = e1.get().lower()
    computer_choice = get_computer_choice()
    result=determine_winner(user_choice, computer_choice)
    return e3.insert(0,result)
def clear():
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
top=Tk()
top.title("game")
top.configure(background="powder blue") 
user_choice=Label(top,text="enter your choice  (rock,paper,sessior):")
user_choice.grid(row=0,column=0)
e1=Entry(top)
e1.grid(row=0,column=1)

play_button=Button(top,text="play",command=play_game)
play_button.grid(row=1,column=1)

computer_choice=Label(top,text="compter choice")
computer_choice.grid(row=2,column=0)
e2=Entry(top)
e2.grid(row=2,column=1)

result_label=Label(top,text="result")
result_label.grid(row=3,column=0)
e3=Entry(top)
e3.grid(row=3,column=1)

clear=Button(top,text="clear ",command=clear)
clear.grid(row=4,column=1)
top.mainloop()