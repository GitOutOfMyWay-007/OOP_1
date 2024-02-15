from turtle import Turtle, Screen

timmy = Turtle()  # Timmy object declared from Turtle class
print(timmy)
timmy.shape("turtle")  # object method / function
timmy.color("coral")   # object method / function
timmy.forward(100)     # object method / function


my_screen = Screen()  # my_screen object declared from Screen class
print(my_screen.canvheight)  # attribute declared from the object
my_screen.exitonclick()


from prettytable import PrettyTable

table = PrettyTable()  # Object table declared from Class PrettyTable
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])  # Object Method / function
table.add_column("type", ["Electric", "Water", "Fire"])  # Object Method / function
print(table)
print(table.align)

table.align = 'l'  # changing the value of object attribute / variable
print(table)
print(table.align)
print("This file is uploaded to git and this is test print to update files.")
