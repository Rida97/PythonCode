""""
Street Fighter: Ryu punches Ken.
By David, 2017
Rafeh Qazi made it work ;)
"""

import tkinter as tk


class Fighter:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.damage = 10

    # function for one fighter to attack another
    def attack(self, other_guy):
        # print(dir(event))
        other_guy.health -= self.damage
        print("{} attacks {} for {} damage, ouch that's gotta hurt!".format(self.name, other_guy.name, self.damage))


ryu = Fighter('Ryu')
ken = Fighter('Ken')

window = tk.Tk()
window.geometry("500x500")
window.bind("<Button-1>", )

ryu_label = tk.Label(text="Ryu")
ryu_label.grid(column=0, row=0)


def button1_callback(event=None):
    ryu.attack(ken)


ryu_attack_button = tk.Button(text="Attack", command=button1_callback)
ryu_attack_button.grid(column=0, row=1)

# *** shortkeyys are binded to FRAMES and NOT buttons. ***
window.bind("<Return>", button1_callback)

ken_label = tk.Label(text="Ken")
ken_label.grid(column=2, row=0)

import tkinter as tk
import webbrowser

URL = 'https://cleverprogrammer.com'


# Event handler function
def doorbell(event):
    print("You rang the doorbell!!")


def open_cp(event):
    webbrowser.open_new_tab(URL)


def cp_blog(event):
    webbrowser.open_new_tab(URL + "/blog")


window = tk.Tk()
window.geometry("300x200")

alabel = tk.Label(text="Banana")
alabel.grid(column=0, row=0)

blabel = tk.Label(text="Home")
blabel.grid(column=1, row=0)

clabel = tk.Label(text="Blog")
clabel.grid(column=2, row=0)

button = tk.Button(window, text="Doorbell")
button.grid(column=0)

button2 = tk.Button(window, text="Clever Programmer")
button2.grid(column=1, row=1)

button3 = tk.Button(window, text="CP Blog")
button3.grid(column=2, row=1)

button.bind("<Button-1>", doorbell)
button2.bind("<Button-1>", open_cp)
button3.bind("<Button-1>", cp_blog)

window.mainloop()
class Animal:
    def __init__(self, name):
        self.name = name

    def talk(self):
        pass

class Dog(Animal):
    def talk(self):
        return "WOOF"

class Cat(Animal):
    def talk(self):
        return "Meow"

pet_qazi = Animal("Qazoo")
print(pet_qazi.name)
print(pet_qazi.talk())

pet = Dog("Dot")
print(pet.name)
print(pet.talk())

kitten = Cat("Brian")
print(kitten.name)
print(kitten.talk())