from os import system, name

def clear():
 
    if name=='nt':
        _ = system('cls')
    else:
        _ = system('clear')

clear()

new_idea = ""
idea_list = []

while new_idea.lower() != 'quit':
    clear()
    print("Welcom to Idea Bank!\n")

    for i, idea in enumerate(idea_list):
        print(f"{i+1}. {idea}")
    
    print("\nType 'Quit' to finish")
    new_idea = input("\nWhat is your new idea? ")
    idea_list.append(new_idea)