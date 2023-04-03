from linked_list import LinkedList
import time

print("***** welcome to linked list data structure!!! *****")
print("Please select one of the below operation")
print("1. To print the existing linked list.")
print("2. To add to the end of the linked list.")
print("3. To add to the beginning of the linked list.")
print("4. To insert a node at a specified position. Head being at 1st position")
print("5. Reverse a linked list")
print("6. Insert at specified index using recursion.")
print("   press '*' to exit the console.")
l1 = LinkedList()
is_true = True
while is_true:
    user_choice = input("Enter your choice of operation: ").lower()
    if user_choice == "1":
        print("Your current linked list: ", end="")
        l1.print_linked_list()
        print("")
    elif user_choice == "2":
        print("Entering to the end of the linked list..")
        new_value = input("Enter value of node you want to add: ").lower()
        l1.add_node(new_value)
    elif user_choice == "3":
        print("Entering to the beginning of the linked list..")
        new_value = input("Enter value of node you want to add: ").lower()
        l1.add_node_at_start(new_value)
    elif user_choice == "4":
        new_value = input("Enter value of node you want to add: ").lower()
        position = int(input("Enter position where you want to add node: "))
        l1.insert(position, new_value)
    elif user_choice == "5":
        l1.reverse_linked_list()
        l1.print_linked_list()
    elif user_choice =="6":
        new_value = input("Enter value of node you want to add: ").lower()
        position = int(input("Enter position where you want to add node: "))
        l1.insertRec(position, new_value)
    elif user_choice == "*":
        t = 3
        while t > 0:
            print(f"Exiting the console window in ({t}) seconds")
            time.sleep(1)
            t -= 1
        is_true = False
    else:
        print("You have selected a wrong option, please select again.")


