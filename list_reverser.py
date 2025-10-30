# ------------------------------------------------------------
# List Reverser (Without Built-in reverse)
# Description:
#   Reverses a list manually without using built-in methods.
# Author: Abhishek Rana
# ------------------------------------------------------------

def reverse_list(lst):
    reversed_list = []
    for i in range(len(lst) - 1, -1, -1):
        reversed_list.append(lst[i])
    return reversed_list

if __name__ == "__main__":
    user_input = input("Enter numbers separated by spaces: ")
    numbers = [int(x) for x in user_input.split()]
    print("Reversed list:", reverse_list(numbers))
