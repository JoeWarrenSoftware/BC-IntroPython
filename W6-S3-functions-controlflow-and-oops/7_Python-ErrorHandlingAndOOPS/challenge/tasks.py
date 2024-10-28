# Load Modules
import json
import traceback

# Default states
version = 1.0
exit = False
Tasks = {}
print(f"Welcome to the Tasks Program v{version}")


# Load up tasks if found:
try:
    with open('tasks.json', 'r') as file:
        Tasks = json.load(file)
        print(f"Loaded Tasks from File: {len(Tasks)} tasks found")
except FileNotFoundError:
    print("No File Found")
except Exception as e:
    print(f"ERROR - Loading File: {e}\n{traceback.format_exc()}") 

def WriteTasksToFile():
    with open('tasks.json', 'w') as file:
            json.dump(Tasks, file, indent=4)
            print("Task saved to tasks.json")

# Option 1 - Add a Task
def AddTask():
    try:
        # Read Input from User 
        desc = input("Add Task - Please provide a description for the task: ")       
        
        id = 1
        keys = Tasks.keys()
        print(f"Tasks found: {len(keys)} Keys found: {sorted(keys)}")
        # Loop through existing Tasks until an unused ID can be found
        while str(id) in keys:
            id += 1
        
        print(f"Using new key = {id}")

        # Create new Task object
        newTask = {
            "status" : "Not Started",
            "description" : desc
        }

        # Add Task to larger collection
        Tasks[str(id)] = newTask
        # Write the task to the JSON file
        WriteTasksToFile()

    except Exception as e:
        print(f"ERROR - Add Task: {e}\n{traceback.format_exc()}") # Print the Exception message followed by the Traceback to find where the throwing happened

# Option 2 - View a Task
def ViewTask():
    try:
        # Read Input from User 
        keys = Tasks.keys()
        print (f"View Task - IDs Found: {sorted(keys)}")
        userInput = input("View Task - Enter an ID: ")
        
        # print task data if found, otherwise report missing key
        if userInput in keys:
            task = Tasks[userInput]
            print(f"View Task - Task Found: {task}")
        else:
            print(f"View Task - Task '{userInput}' Not Found in Keys: {keys}")
    except Exception as e:
        print(f"ERROR - View Task: {e}\n{traceback.format_exc()}") # Print the Exception message followed by the Traceback to find where the throwing happened

# Option 3 - Modify a Task
def ModifyTask():
    try:
        # Read Input from User 
        keys = Tasks.keys()
        print (f"View Task - IDs Found: {sorted(keys)}")
        userInput = input("Modify Task - Enter an ID: ")
        
        # print task data if found, otherwise report missing key
        if userInput in keys:
            task = Tasks[userInput]
            print(f"Modify Task - Task Found: {task}")
            status = input("Modify Task - Enter new status (leave blank to keep to keep unchanged): ")
            desc = input("Modify Task - Enter description (leave blank to keep to keep unchanged): ")
            if (status != "" or desc != ""):
                if status != "":
                    task["status"] = status # Update status if not empty
                if desc != "":
                    task["description"] = desc # Update description if not empty
                Tasks[userInput] = task # Update Tasks collection with modified task
                WriteTasksToFile() # Write to the JSON file
                print(f"Task updated: {task}")
            print(f"No updates to change: {task}")
        else:
            print(f"Modify Task - Task '{userInput}' Not Found in Keys: {keys}")
    except Exception as e:
        print(f"ERROR - Modify Task: {e}\n{traceback.format_exc()}") # Print the Exception message followed by the Traceback to find where the throwing happened

# Option 4 - Delete a Task
def DeleteTask():
    try:
        # Read Input from User 
        keys = Tasks.keys()
        print (f"Delete Task - IDs Found: {sorted(keys)}")
        userInput = input("Delete Task - Enter an ID: ")
        # print task data if found, otherwise report missing key
        if userInput in keys:
            task = Tasks[userInput]
            print(f"Delete Task - Task Found: {task}")
            del Tasks[str(userInput)]
            WriteTasksToFile()
            print("Delete Task - Task Deleted")
        else:
            print(f"Delete Task - Task '{userInput}' Not Found in Keys: {keys}")
    except Exception as e:
        print(f"ERROR - Delete Task: {e}\n{traceback.format_exc()}") # Print the Exception message followed by the Traceback to find where the throwing happened

try:
    while exit==False:
        print("\nMain Menu - Please select an option (1-5):") # Show Main Menu
        print("Option 1 : Add Task")
        print("Option 2 : View Task")
        print("Option 3 : Modify Task")
        print("Option 4 : Delete Task")
        print("Option 5 : Exit")
        inputS = input("Enter Option: ") # Store user input (string)
        option = int(inputS) if inputS.isnumeric() else None # Try-Parse the input to an interger
        match option:
            case 1:
                AddTask()
            case 2:
                ViewTask()
            case 3:
                ModifyTask()
            case 4:
                DeleteTask()
            case 5:
                print("Exiting Program...")
                exit = True
            case _:
                print("Input not recogised as an input. Please try again")
except Exception as e:
    print(f"ERROR - Main Menu: {e}\n{traceback.format_exc()}") # Print the Exception message followed by the Traceback to find where the throwing happened