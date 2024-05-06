my_list = [4,5,734,43,45,100,4,56,23,67,23,58,45]

# Your code here
def sum_odds(my_list):
    sum = 0
    for i in my_list:
        if (i%2 == 0):
            continue
        else:
            sum = sum + i
    return sum

print(sum_odds(my_list))