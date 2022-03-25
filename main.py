todos = []
print("Enter \"a\" to add a todo, enter \"d\" to delete a todo, and enter \"quit\" to quit.")

while(True):
    print("Here are your todos: " + str(todos))
    action = input("Add or delete? ")
    if (action == 'a'):
        new_todo = input("What should your new todo be named? ")
        todos.append(new_todo)
    elif (action == 'd'):
        del_todo = input("What todo should I delete? ")
        try:
            if (type(del_todo) == str):
                todos.remove(del_todo)
        except:
            print("That todo could not be found.")
    elif (action == 'quit'):
        print('Ok, quitting!')
        break;
    else:
        print("Please enter a for add or d for delete. If you would like to leave enter quit")