#This is a python script for a shopping store manager that helps in arranging 
# addind, removing and viewing the current items in the store 
# This script helps in managing your store


# This Code Display the front page and promt user to about what action to take
def display_menu():
    print("Shopping List Manager") 
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

#This is the main function that perform the operations 
# To add items
# To delete items 

def main():
    shopping_list = []
    while True: #This loop throuch the shopping list items to check if its true ofr false
        display_menu() # To display the menu function above
        choice = input("Enter your choice: ") 

        if choice == '1':
            item_name = input("Enter the item to add`: ")
            shopping_list.append(item_name)
            pass
        elif choice == '2':
            item_name == input("Which item do you want to remove: ")
            shopping_list.remove(item_name)
            pass
        elif choice == '3':
            print(*shopping_list, sep=", ")
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. please try again.")

if __name__ == "__main__":
    main()


