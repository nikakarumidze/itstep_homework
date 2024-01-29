def triple(input):
    return 3 * input


print(triple('digger'))


def moon_weight(weight):
    return weight / 6


print(moon_weight(72))

# eval ფუნქციით უფრო მარტივად კეთდება


def calculator(action):
    arr = action.split(' ')
    operand1 = int(arr[0])
    operand2 = int(arr[2])
    operator = arr[1]
    if operator == '+':
        return operand1 + operand2
    elif operator == '-':
        return operand1 - operand2
    elif operator == '*':
        return operand1 * operand2
    elif operator == '/':
        if int(arr[2]) == 0:
            return 'can not divide to 0'
        return operand1 / operand2
    elif arr[1] == '^':
        return operand1 ^ operand2
    elif arr[1] == '**':
        return operand1 ** operand2
    else:
        return 'some error occured'


print(calculator('2 ** 4'))
