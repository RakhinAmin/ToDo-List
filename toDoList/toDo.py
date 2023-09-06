# Function to read and return the content of the tasks file
def display_tasks(__file__):
    # Open the tasks file in read mode
    with open(__file__, 'r') as t:
        # Read all lines from the file and store them as a list of strings
        lines = t.readlines()
    # Return the content of the file as a single string
    return ''.join(lines)

# Function to add a new task to the tasks file


def add_tasks(__file__):
    # Ask the user to input a new task
    userTask = input("Please enter a task: ")
    # Open the tasks file in append mode and write the new task followed by a newline character (to separate the tasks)
    with open(__file__, 'a') as addTask:
        addTask.write(userTask + '\n')
    # Print a success message (did not manage to implement a print statement that shows the new task)
    print("Your task has been added")

# Function to update an existing task in the tasks file


def update_task(__file__):
    # Open the tasks file in read mode
    with open(__file__, 'r') as tasks_file:
        # Read all lines from the file and store them as a list of strings
        lines = tasks_file.readlines()

    # Display the current tasks along with their index number
    print("Current tasks:")
    for i, task in enumerate(lines, start=1):
        # Strips each task to have only the index remaining
        print(f"{i}. {task.strip()}")

    try:
        # Ask the user for the index of the task they want to update
        task_index = int(
            input("Enter the index of the task you want to update: ")) - 1
        # Check if the provided index is within the range of index's
        if 0 <= task_index < len(lines):
            # Ask the user for the updated task description
            updated_task = input("Enter the updated task description: ")
            # Update the task in the list with the new description
            lines[task_index] = updated_task + '\n'

            # Open the tasks file in write mode
            with open(__file__, 'w') as tasks_file:
                # Write the updated lines back to the file
                tasks_file.writelines(lines)
            # Print a success message
            print("Task updated successfully!")
        else:
            # Print an error message for invalid index
            print("Invalid task index.")
    except ValueError:
        # Print an error message for invalid input
        print("Invalid input. Please enter a valid task index.")

# Function to delete a task from the tasks file


def delete_task(__file__):
    # Open the tasks file in read mode
    with open(__file__, 'r') as tasks_file:
        # Read all lines from the file and store them as a list of strings
        lines = tasks_file.readlines()

    # Display the current tasks along with their indices
    print("Current tasks:")
    for i, task in enumerate(lines, start=1):
        print(f"{i}. {task.strip()}")

    try:
        # Ask the user for the index of the task they want to delete
        task_index = int(
            input("Enter the index of the task you want to delete: ")) - 1
        # Check if the provided index is within valid range
        if 0 <= task_index < len(lines):
            # Delete the selected task from the list
            del lines[task_index]

            # Open the tasks file in write mode
            with open(__file__, 'w') as tasks_file:
                # Write the updated lines back to the file
                tasks_file.writelines(lines)
            # Print a success message
            print("Task deleted successfully!")
        else:
            # Print an error message for invalid index
            print("Invalid task index.")
    except ValueError:
        # Print an error message for invalid input
        print("Invalid input. Please enter a valid task index.")


# Main loop for the to-do list application
while True:
    # Ask the user for their choice
    userChoice = input(
        "Please enter one of the following choices for the task list: view, add, update, delete, or exit the program")
    print(userChoice)

    # User choices handling
    if userChoice == "view":
        # Display the current tasks by calling the display_tasks function
        print(display_tasks('tasks.txt'))
    elif userChoice == "add":
        # Add a new task by calling the add_tasks function
        add_tasks('tasks.txt')
    elif userChoice == "update":
        # Update a task by calling the update_task function
        update_task('tasks.txt')
    elif userChoice == "delete":
        # Delete a task by calling the delete_task function
        delete_task('tasks.txt')
    elif userChoice == "exit":
        # Exit the loop to end the program
        break
    else:
        # Display an error message for invalid input
        print("Invalid input, please try again")

# Display a thank you message when the program ends
print("Thank you for using the to-do list application")
