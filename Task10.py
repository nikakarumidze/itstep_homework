import time
import random

def tictoc(func):
    def wrapper(arr, target):
        t1 = time.time()
        result = func(arr, target)
        t2 = time.time() - t1
        print(f'Took {t2} seconds')
        return result
    return wrapper

def generate_random_array(size, low=0, high=1000):
    return [random.randint(low, high) for _ in range(size)]

@tictoc
def linear_search(arr, target):
    for i, num in enumerate(arr):
        if num == target:
            return i
    return -1

@tictoc
def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

# Generate array
random_arr = generate_random_array(500)

# Sort array
sorted_arr = sorted(random_arr)

# Choose element to search
target = random.choice(sorted_arr)

# Perform searches
linear_search_result = linear_search(sorted_arr, target)
binary_search_result = binary_search(sorted_arr, target)

print(f"Linear Search Result: {linear_search_result}")
print(f"Binary Search Result: {binary_search_result}")
