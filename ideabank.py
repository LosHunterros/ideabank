from os import system, name

def clear():
 
    if name=='nt':
        _ = system('cls')
    else:
        _ = system('clear')

clear()

ideas_list = []

while True:
    clear()
    print("Welcom to Idea Bank!\n")
    ideas_list.append(input("What is your new idea? "))