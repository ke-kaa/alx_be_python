shopping_list = []


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
            item = input("Item: ")
            shopping_list.append(item)
        elif choice == '2':
            item = input("Item: ")
            shopping_list.remove(item)
        elif choice == '3':
            for items in shopping_list:
                print(items)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
