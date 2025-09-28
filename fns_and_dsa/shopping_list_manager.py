
def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            value = input("Enter the item: ")
            shopping_list.append(value)
            print(f"'{value}' has been added to the shopping list.\n")

        elif choice == '2':
            value = input("Enter the item you want to remove: ")
            if value in shopping_list:
                shopping_list.remove(value)
                print(f"'{value}' has been removed from the shopping list.\n")
            else:
                print(f"'{value}' is not in the shopping list.\n")

        elif choice == '3':
            if shopping_list:
                print("\nYour Shopping List:")
                for i, item in enumerate(shopping_list, start=1):
                    print(f"{i}. {item}")
                print()
            else:
                print("Your shopping list is empty.\n")

        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()

