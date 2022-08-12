# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 17:14:05 2022

@author: Dell
"""



from tkinter import*
import random
root = Tk()
root.title("Password Generator")
root.geometry("500x500")
root.configure(background = "lightpink")

input_password = Entry(root , bg = "yellow" , fg = "purple" , font = 25)
input_password.place(relx = 0.5 , rely = 0.3 , anchor = CENTER)
label_guessed = Label(root , bg = "lightpink" , fg = "purple" , font = 25)
label_guessed.place(relx = 0.5 , rely = 0.4 , anchor = CENTER)

label = Label(root,bg = "lightpink" , fg = "purple" , font = 25)

array_3d = [
    [["%" , "$" , "*" , "&"],
     ["king" , "queen" , "jack" , "ace"],
     ["1" , "7" , "6" , "0"]]
    
    ]

print(array_3d[0]) #whole array
print(array_3d[0][0]) #number list
print(array_3d[0][1]) #word list
print(array_3d[0][2]) #alphabet list

def password():
    label_guessed["text"] =str("Guessed Password") + input_password.get()
    random_no_1 = random.randint(0,3)
    random_no_2 = random.randint(0,3)
    random_no_3 = random.randint(0,3)
    
    letter_1 = str(array_3d[0][0][random_no_1])
    letter_2 = str(array_3d[0][1][random_no_2])
    letter_3 = str(array_3d[0][2][random_no_3])
    
    label["text"] = letter_1 + letter_2 + letter_3
    
btn = Button(root, text = "Generate Password" , command = password , bg = "purple" , fg = "lightpink" , font = 25)    
btn.place(relx = 0.5 , rely = 0.5 , anchor = CENTER)
label.place(relx = 0.5 , rely = 0.6 , anchor = CENTER)

root.mainloop()