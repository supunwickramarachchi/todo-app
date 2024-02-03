# from functions import get_todos, write_todos
import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print(f"It's {now}")
while True:
    # Get user input and strip , space char from it
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo.title() + '\n')

        functions.write_todos(todos)

    elif user_action.startswith("show"):
        todos = functions.get_todos()

        # use list comprehension to strip "\n" from items
        new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(new_todos, 1):
            print(f"{index}: {item}")

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number -= 1

            todos = functions.get_todos()

            new_todo = input("Enter new todo: ").title()
            todos[number] = new_todo + '\n'

            functions.write_todos(todos)
        except ValueError:
            print("Your command is not valid!")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')

            todos.pop(index)

            functions.write_todos(todos)

            message = f"Todo {todo_to_remove} was removed from the list!"
            print(message)
        except IndexError:
            print("There is no items with that number")
            continue
        except ValueError:
            print("Your command is not valid!")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("Command is not valid!")

print("Bye!")
