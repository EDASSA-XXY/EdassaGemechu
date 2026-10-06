#1
Name = input("What is your name\n >")
Color = input("What is your favorite color\n >")
Game = input("What is your favorite game\n >")
print("Hi my is " + Name + "my favorite color is " + Color + "and my favorite game is" + Game + ".")
print("---------------------------------------------------------------------------------------------")
#2
value_x = input("What # is x")
value_y = input("What # is y")
value_z = input("What # is z")

def add_three(x,y,z):
    print(x + y + z)

add_three(value_x,value_y,value_z)
print("---------------------------------------------------------------------------------------------")
#3
def data_three():
    Word = input("word choice")
    First_Number = int(input("# choice"))
    Second_Number = float(input("# choice"))
    First_Number + Second_Number 
    print(str(First_Number) + str(Second_Number) + Word) 

