# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 13:56:19 2021

@author: hp
"""

from tkinter import*
import random 

root=Tk()

root.title("LUCKY BIAS?")
root.geometry("400x400")

label_element=Label(root)

def random_name():
    alpha_list=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    random_no1=random.randint(1,26)
    random_no2=random.randint(1,26)
    random_no3=random.randint(1,26)
    random_no4=random.randint(1,26)
    random_no5=random.randint(1,26)
    random_alpha1=alpha_list=[random_no1]
    random_alpha2=alpha_list=[random_no2]
    random_alpha3=alpha_list=[random_no3]
    random_alpha4=alpha_list=[random_no4]
    random_alpha5=alpha_list=[random_no5]
    
label_element=Label(" ") + (random_alpha1) + (random_alpha2) + (random_alpha3) + (random_alpha4) + (random_alpha5) + " "
button=Button(root,text="generate a random word !!!",command=random_name)
button.place(relx=0.5,rely=0.4,anchor=CENTER,bg=red,fg=black)
root.mainloop()