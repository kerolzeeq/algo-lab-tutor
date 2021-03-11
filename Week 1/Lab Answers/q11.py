num_list = [5, 10, 15, 20, 25]

def first_last(num_list):
    new_list = [num_list[0], num_list[len(num_list)-1]]
    return new_list

print(first_last(num_list))