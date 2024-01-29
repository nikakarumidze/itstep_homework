# Task 1
def looper(num):
    # Base case
    if num == 0:
        return
    print("hello world")
    # Recursion
    return looper(num - 1)


looper(3)

# Task 2


def order_food(food, quantity=1):
    return f"{food}, {quantity}"


print(order_food('Shawarma'))

# Task 3


def multiply(*args):
    if len(args) < 2:
        return 'not enough numbers'
    multiply = 1
    for num in args:
        multiply *= num
    return multiply


print(multiply(1))
