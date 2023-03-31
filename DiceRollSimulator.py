# importing random module
import random 
# importing tkinter library
# we are importing everything from tkinter library
from tkinter import *
#defining a tkinter window
root=Tk()
#defining dimensions for tkinter window
#Here 600 represents length of tkinter window
#Here 300 represents width of tkinter window
#Here alphabet "x" is present between dimension of tkinter window
root.geometry("800x500")
#creating label  
#label is used is to specify container box where one can put image or text
#root is a tkinter window of dimension 600x300 
#text is a text which is to be written on label
#font(arial(font-style)) is the font for text written in label
#300 is the font-size of the text.
text_1=Label(root,text='',font=("arial",300))
def roll_the_dice():
    num_code=['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    # By using config() we can access the object's attributes after its initialisation.
    text_1.config(text=f'{random.choice(num_code)} {random.choice(num_code)}')
    #The Pack geometry manager packs widgets relative to the earlier widget
    text_1.pack()
#defining a button
#text is a text which is to be written on button
#roll_the_dice is a function
button_1=Button(root,text="Roll the dice",command=roll_the_dice)
#Defining where to place button 
button_1.place(x=350,y=0)
# mainloop() is used when our application is ready to run. mainloop() is an infinite loop used to run the application, wait for an event to occur and process the event as long as the window is not closed.
root.mainloop()
