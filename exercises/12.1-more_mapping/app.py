my_numbers = [23,234,345,4356234,243,43,56,2]

def multiply_by_three(number):
    return number * 3


result = map(multiply_by_three, my_numbers)  
new_list= list(result)
print(new_list)
