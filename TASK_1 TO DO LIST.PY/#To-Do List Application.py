# To-Do List Application
TASK_LIST= []


def enqueue():
    element = input("Enter elements to insert:")
    TASK_LIST.append(element)
    print(f"{element} is inserted into the task list.")
    
def dequeue():
    if not TASK_LIST:
        print("TASK LIST is empty! cannot remove elements.")
    else:
        display()

        try:
            index = int(input("Enter the index of the task to remove: "))
            if 1 <= index <= len(TASK_LIST):
                removed = TASK_LIST.pop(index - 1)
                print(f"{removed} has been removed from the task list.")
            else:
                print("Invalid index! Please enter a number between 1 and", len(TASK_LIST))
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def display():
    if not TASK_LIST:
        print("TASK LIST is empty.")
    else:
        print("current TASKLIST:", TASK_LIST)
        for i, task in enumerate(TASK_LIST, start=1):
            print(f"{i}. {task}")
        
while True:
    print("\n--- TO DO APPLICATION ---")
    print("1. INSERT TASK")
    print("2. Remove Task")
    print("3. Display Tasks")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4):")
    
    if choice =='1':
        enqueue()
    elif choice == '2':
        dequeue()
    elif choice == '3':
        display()
    elif choice == '4':
        print("Exiting.... Thank you!")
        break 
    else:
        print("Invalid choice! please enter between 1-4.")