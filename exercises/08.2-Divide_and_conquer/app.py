list_of_numbers = [4, 80, 85, 59, 37, 25, 5, 64, 66, 81, 20, 64, 41, 22, 76, 76, 55, 96, 2, 68]

# Your code here
def sort_odd_even(list_of_numbers):
    sorted_list = []
    for i in list_of_numbers:
        if (i % 2 != 0):
            sorted_list.append(i)
    for i in list_of_numbers:
        if (i % 2 == 0):
            sorted_list.append(i)
    
    return sorted_list



print(sort_odd_even(list_of_numbers))
