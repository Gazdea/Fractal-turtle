t = turtle.Turtle()
#t.hideturtle()
t.speed(0)
instruction = "d5/a70/"
axiom = "F+X-F+X-F+X+F+X-F+X-F+X-F+X+F+X-F+X-F+X-F+X+F+X"
rules = {"F":"F-F+F","X":"F+F-F"}
iterations = 1
instruction = instruction + create_l_system(iterations, axiom, rules)
draw(t, instruction)













