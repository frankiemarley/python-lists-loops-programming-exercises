def lyrics_generator(listx):
    count = 0
    my_list = []
    for i in listx:
        if i == 0:
            my_list.append('Boom ')
            count = 0
        if i == 1:
            my_list.append('Drop the bass ')
            count += 1
            if count == 3:
                my_list.append('!!!Break the bass!!! ')
                count = 0
    return "".join(my_list)

        

# Your code above, nothing to change after this line
print(lyrics_generator([0,0,1,1,0,0,0]))
print(lyrics_generator([0,0,1,1,1,0,0,0]))
print(lyrics_generator([0,0,0]))
print(lyrics_generator([1,0,1]))
print(lyrics_generator([1,1,1]))
