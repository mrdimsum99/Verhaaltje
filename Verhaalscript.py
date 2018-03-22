# Import and read textfiles
file1 = open("text1.txt", "r")
file2 = open("text2.txt", "r")
file3 = open("text3.txt", "r")
file4 = open("text4.txt", "r")

txt1 = file1.read()+"\n"
txt2 = file2.read()+"\n"
txt3 = file3.read()+"\n"
txt4 = file4.read()+"\n"

verhaal = txt1+txt2+txt3+txt4

# Simple GUI
from tkinter import *

root = Tk()

root.title("Verhaaltje")
root.geometry("400x200")

app = Frame(root)
app.grid()
label = Label(app, text = verhaal)

label.grid()

# Kick off
root.mainloop()
