import random
import timeit

#Task 1 and 2
def generate_elements(n):
    return [random.randint(1, 100) for i in range(n)]

def sort_elements(elements,reverse=False):
    #if reverse=True, its descending
    return sorted(elements, reverse=reverse)

random_elements = generate_elements(10)

sorted_ascending = sort_elements(random_elements)
sorted_descending = sort_elements(random_elements,True)

print("Ascending", sorted_ascending)
print("Descending", sorted_descending)

#Task 3
random_array_1000 = generate_elements(1000)
random_array_2000 = generate_elements(2000)
random_array_3000 = generate_elements(3000)

def bubble_sort(arr):
    index = 0
    while index < len(arr):
        for j in range(0, len(arr)-index-1):
            if arr[j] > arr[j+1]:
                # Swap places
                arr[j], arr[j+1] = arr[j+1], arr[j]
        index += 1
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        # Select left member of array
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

bubble_sort_time_1000 = timeit.timeit(lambda: bubble_sort(random_array_1000.copy()))
insertion_sort_time_1000 = timeit.timeit(lambda: insertion_sort(random_array_1000.copy()))

bubble_sort_time_2000 = timeit.timeit(lambda: bubble_sort(random_array_2000.copy()))
insertion_sort_time_2000 = timeit.timeit(lambda: insertion_sort(random_array_2000.copy()))

bubble_sort_time_3000 = timeit.timeit(lambda: bubble_sort(random_array_3000.copy()))
insertion_sort_time_3000 = timeit.timeit(lambda: insertion_sort(random_array_3000.copy()))

print(f"""
      Bubble Sort Time: {bubble_sort_time_1000},{bubble_sort_time_2000},{bubble_sort_time_3000} seconds
      Insertion Sort Time: {insertion_sort_time_1000},{insertion_sort_time_2000},{insertion_sort_time_3000} seconds
      """)

