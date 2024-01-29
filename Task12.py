def remove_duplicates(input_dict):
    unique_dict = {}
    for key, value in input_dict.items():
        if value not in unique_dict.values():
            unique_dict[key] = value
    return unique_dict

# Example usage:
sample_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 2, 'e': 3, 'f': 1}
result_dict = remove_duplicates(sample_dict)
print(result_dict)

def is_dict_empty(input_dict):
    return not bool(input_dict)

# Example usage:
empty_dict = {}
non_empty_dict = {'a': 1, 'b': 2}

print(is_dict_empty(empty_dict))  # Output: True
print(is_dict_empty(non_empty_dict))  # Output: False

def create_dict_from_string(input_string):
    char_count_dict = {}
    for char in input_string:
        char_count_dict[char] = char_count_dict.get(char, 0) + 1
    return char_count_dict

# Example usage:
sample_string = 'w3schools'
result_dict = create_dict_from_string(sample_string)
print(result_dict)
