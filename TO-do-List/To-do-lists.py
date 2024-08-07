def display_menu():
    print("\nTo-Do List Application")
    print("1. View To-Do List")
    print("2. Add To-Do Item")
    print("3. Update To-Do Item")
    print("4. Delete To-Do Item")
    print("5. Exit")

def view_todo_list(todo_list):
    if not todo_list:
        print("\nYour to-do list is empty.")
    else:
        print("\nYour To-Do List:")
        for index, item in enumerate(todo_list, start=1):
            print(f"{index}. {item}")

def add_todo_item(todo_list):
    item = input("\nEnter the to-do item: ")
    todo_list.append(item)
    print(f"'{item}' has been added to your to-do list.")

def update_todo_item(todo_list):
    view_todo_list(todo_list)
    index = int(input("\nEnter the number of the item you want to update: ")) - 1
    if 0 <= index < len(todo_list):
        new_item = input("Enter the new to-do item: ")
        todo_list[index] = new_item
        print(f"Item {index + 1} has been updated to '{new_item}'.")
    else:
        print("Invalid item number.")

def delete_todo_item(todo_list):
    view_todo_list(todo_list)
    index = int(input("\nEnter the number of the item you want to delete: ")) - 1
    if 0 <= index < len(todo_list):
        removed_item = todo_list.pop(index)
        print(f"'{removed_item}' has been removed from your to-do list.")
    else:
        print("Invalid item number.")

def main():
    todo_list = []
    while True:
        display_menu()
        choice = input("\nEnter your choice: ")
        
        if choice == '1':
            view_todo_list(todo_list)
        elif choice == '2':
            add_todo_item(todo_list)
        elif choice == '3':
            update_todo_item(todo_list)
        elif choice == '4':
            delete_todo_item(todo_list)
        elif choice == '5':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
