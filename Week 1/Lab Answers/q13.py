num_list = [5, 10, 15, 20, 25, 5, 10, 25]

def unduplicate(num_list):
    new_list = []
    for i in num_list:
        if i not in new_list:
            new_list.append(i)
    return new_list

print(unduplicate(num_list))