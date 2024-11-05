from msilib.schema import File
import turtle
import tkinter as tk
from tkinter.scrolledtext import ScrolledText

# d - distance a - angle F - forward (+) - right (-) - left 
# X - penup forward c - pencolor s - pensize c - color
# C - clear x - setx y - sety
def draw(t, instruction):
    distance = 50
    angle = 90
    
    commands = {
        'd': lambda: set_distance(),
        'a': lambda: set_angle(),
        'F': lambda: t.forward(distance),
        '+': lambda: t.right(angle),
        '-': lambda: t.left(angle),
        'X': lambda: (t.penup(), t.forward(distance), t.pendown()),
        'c': lambda: set_color(),
        's': lambda: set_size(),
        'C': lambda: t.clear(),
        'x': lambda: set_x(),
        'y': lambda: set_y(),
    }

    def set_distance():
        nonlocal instruction, distance
        distance_str = instruction[instruction.index('d') + 1:instruction.index('/', instruction.index('d') + 1)]
        distance = int(distance_str)
        instruction = instruction[instruction.index('d') + len(distance_str) + 1:]
        

    def set_angle():
        nonlocal instruction, angle
        angle_str = instruction[instruction.index('a') + 1:instruction.index('/', instruction.index('a') + 1)]
        angle = int(angle_str)
        instruction = instruction[instruction.index('a') + len(angle_str) + 1:]

    def set_color():
        nonlocal instruction
        color = instruction[instruction.index('c') + 1:instruction.index('/', instruction.index('c') + 1)]
        t.pencolor(color)
        instruction = instruction[instruction.index('c') + len(color) + 1:]

    def set_size():
        nonlocal instruction
        size = instruction[instruction.index('s') + 1:instruction.index('/', instruction.index('s') + 1)]
        t.pensize(int(size))
        instruction = instruction[instruction.index('s') + len(size) + 1:]

    def set_x():
        nonlocal instruction
        Setx = instruction[instruction.index('x') + 1:instruction.index('/', instruction.index('x') + 1)]
        t.setx(int(Setx))
        instruction = instruction[instruction.index('x') + len(Setx) + 1:]

    def set_y():
        nonlocal instruction
        Sety = instruction[instruction.index('y') + 1:instruction.index('/', instruction.index('y') + 1)]
        t.sety(int(Sety))
        instruction = instruction[instruction.index('y') + len(Sety) + 1:]

    while instruction:
        if instruction[0] in commands:
            commands[instruction[0]]()
            instruction = instruction[1:]
        else:
            print("Error")

def create_l_system(iters, axiom, rules):
    start_string = axiom
    if iters == 0:
        return axiom
    end_string = ""
    for _ in range(iters):
        end_string = "".join(rules[i] if i in rules else i for i in start_string)
        start_string = end_string

    return end_string

def run_code():
    # Get the code from the text editor
    code = text_editor.get("1.0", tk.END)

    exec(code)
    with open("D:\Repos\Python\Fractal turtle\script.py", "w") as f:
        f.write(code)
    
wn = turtle.Screen()
width, height = 450, 450
wn.setup(width, height)

# Create the main window
window = tk.Tk()

# Create the text editor
text_editor = ScrolledText(window, height=20, width=50)
text_editor.pack()
with open("D:\Repos\Python\Fractal turtle\script.py", "r") as f:
    text_editor.insert(tk.END, f.read())

stop = True
# Create the run button
run_button = tk.Button(window, text="Run", command=run_code)
run_button.pack()
clear_button = tk.Button(window, text="Clear", command=wn.clear)
clear_button.pack()
# Run the main loop
window.mainloop()