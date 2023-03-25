from tkinter import*


class TK_extended(Tk):

    def __init__(self, master, title):
        self.master = master
        self.title = title


    def create(self):
        self.master = Tk()
        self.master.title(self.title)


    def resize(self, width , height):
        self.master.geometry("{}x{}".format(width , height))


    def generate(self):
        self.master.mainloop()


root = TK_extended("win", "My Window")
root.create()
root.resize(500, 300)
root.generate()
