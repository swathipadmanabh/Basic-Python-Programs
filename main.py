import re

print("Our Magical calculator")
print("Type 'Quit' to exit")

previous = 0
run = True

def perform_math():
    global run
    global previous
    equation = ""
    if previous == 0:
        equation = input("Enter the operation:")
    else:
        equation = input(str(previous))
    if equation == 'quit':
        run = False
    else:
        equation = re.sub('[a-zA-Z,:." "]', '', equation)
        if previous ==0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation )
        print(equation)

while run:
    perform_math()