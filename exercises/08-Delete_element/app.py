people = ['juan','ana','michelle','daniella','stefany','lucy','barak']

def delete_person(person_name):
    new_list= []
    for i in people:
        if (i == person_name):
            continue
        else:
            new_list.append(i)
    return new_list
    
    

    
# Don't delete anything below
print(delete_person("daniella"))
print(delete_person("juan"))
print(delete_person("emilio"))
