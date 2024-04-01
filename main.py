from tkinter import *
import tkinter
import webbrowser
import random
from PIL import Image, ImageTk

def rgb_to_hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

def get_text_color(r, g, b):
    luminance = (0.299 * r + 0.587 * g + 0.114 * b) / 255
    return "black" if luminance > 0.5 else "white"

def button1_action():
    webbrowser.open('https://github.com/')
def button2_action():
    webbrowser.open('https://bahcelievleradnanmenderes.meb.k12.tr/')

def button3_action():
    webbrowser.open("https://www.youtube.com/@adnanmenderesand.lisesi2937")

def button4_action():
    webbrowser.open("https://www.instagram.com/adnan_menderes_al1989/")
def button5_action():
    print("Button 5 clicked")

def button6_action():
    print("Button 6 clicked")

texts= ["GitHub", "Site", "Youtube", "Instagram", "Buton 5", "Buton 6"]

window=tkinter.Tk()
window.attributes('-fullscreen', True) # Make the window fullscreen
window.config(background="grey")

buttons = []
button_functions = [button1_action, button2_action, button3_action, button4_action, button5_action, button6_action]
for i in range(1,6+1):
    rand_color = (random.randint(1,255), random.randint(1,255), random.randint(1,255))
    button = Button(window, text=texts[i-1],
                    background=rgb_to_hex(*rand_color),
                    foreground=get_text_color(*rand_color),
                    width=50,
                    height=5,
                    padx=5,
                    pady=5,
                    command=button_functions[i-1],
                    font=("Arial", 10))
    if(i<=3):
        button.place(x=100, y=200*i)
    else:
        button.place(x=1100, y=200*(i-3))
    buttons.append(button)

# Load the image
image = Image.open("foto.png")
# Resize the image
image = image.resize((500, 500))
photo = ImageTk.PhotoImage(image)

# Display the image in the middle
label = Label(window, image=photo)
label.place(relx=0.5, rely=0.5, anchor=CENTER)

window.mainloop()
