my_list = [43,23,6,87,43,1,4,6,3,67,8,3445,3,7,5435,63,346,3,456,734,6,34]

# Your code here
def max_integer(a_list):

    max_num=0
    for i in a_list:
        if (max_num < i):     
            max_num= i     
    return max_num
print(max_integer(my_list))