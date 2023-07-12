
#from turtle import Turtle, Screen
#timmy = Turtle()
#timmy.shape("turtle")
#timmy.color("red")
#def move():
#    timmy.forward(100)
#my_screen = Screen()
#my_screen.onkey(move, "g")
#my_screen.listen()
#my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
#table2 = PrettyTable()
table.add_column("pokemon", ["pikachu", "charmander", "squirtle", "bulbasaur"])
table.add_column("type", ["electric", "fire", "water", "grass"])
#table.border = False
table.align = "r"

#table2.add_row(["person", "james", 122])
#print(table2)
print(table)