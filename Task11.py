#Task 1
def unique_list(input_array):
    unique_set = set(input_array)
    return list(unique_set)

input_array = [1, 2, 2, 3, 4, 4, 5]

print(unique_list(input_array))

#Task 2
def immutable_se(input_array):
    unique_set = set(input_array)
    return frozenset(unique_set)

print(immutable_se(input_array))

#Task 3
def set_to_tuple(set1, set2):
    united_set = set1.union(set2)
    return tuple(united_set)

set_a = {1, 2, 3}
set_b = {3, 4, 5}

print(set_to_tuple(set_a,set_b))