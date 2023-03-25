from distutils import command
from tkinter import *

window = Tk()
window.title('My GUI first program') # I will see my title
window.minsize(width=500, height=300) # My Window becomes bigger
window.config(padx=40, pady=40) # Give me more space around edges

# Label

my_label = Label(text='I Am a Label', font=('Ariel', 24, 'bold'))
my_label.pack()

my_label['text'] = 'New Text'
my_label.config(text='New Text') # Change text I Am a Label', to 'New
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50) #
# Text'

# Button

def button_clicked():
    print('I got clicked')
    new_text = input.get()
    my_label.config(text=new_text) # Show a text inside in label, when I clicked the bgutton
    # my_label.config(text='Button Got Clicked') # Then i click change my label

button = Button(text='Click Me', command=button_clicked)
button.grid(column=1, row=1)

# New Button

new_button = Button(text='New Button')
new_button.grid(column=2, row=0)


# Entry

input = Entry(width=20) # I wll get input, there I can write text
input.grid(column=3, row=2)

window.mainloop() # Infinity Loop for GUI not to close




