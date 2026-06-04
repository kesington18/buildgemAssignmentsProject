# import another_variable

# print(another_variable.another_variable)

# from turtle import Turtle, Screen
#
# timi = Turtle()
# print(timi)
# timi.shape("turtle")
# timi.color("red")
# timi.forward(100)
#
# myScreen = Screen()
# print(myScreen.canvheight)
# myScreen.exitonclick()

# i had to install prettytables in my interpreter
from prettytable import PrettyTable as pt

table = pt()
table.add_column("Pokemon name", [
    "Pikachu",
    "Squirtle",
    "Charmander",
])
table.add_column("Type", [
    "Electric",
    "Water",
    "Fire",
])

table.align = "l"

print(table)