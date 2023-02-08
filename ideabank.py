from os import system, name
from io import open

def clear():
 
    if name=='nt':
        _ = system('cls')
    else:
        _ = system('clear')

clear()

new_idea = ""
idea_file_name = "ideas.txt"

idea_file = open(idea_file_name, mode="r", encoding="utf-8")
idea_list = idea_file.read().splitlines()
idea_file.close()

while new_idea.lower() != 'quit':
    clear()
    print("Welcom to Idea Bank!\n")

    for i, idea in enumerate(idea_list):
        print(f"{i+1}. {idea}")

    idea_file = open(idea_file_name, mode="w", encoding="utf-8")
    idea_file.write('\n'.join(idea_list))
    idea_file.close()

    print("\nType 'Quit' to finish")
    new_idea = input("\nWhat is your new idea? ")
    idea_list.append(new_idea)