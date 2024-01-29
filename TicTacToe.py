import re

# Length is 3, fill with None/null
subArr = [None] * 3
matrix = [[None] * 3, [None] * 3, subArr]

# If user_turn is odd, it's first user's turn, otherwise second's
user_turn = 1


def user_indicator(num):
    if num % 2:
        return 'first user wins'
    return 'second user wins'


while True:
    print(matrix)
    if user_turn % 2:
        input_string = input('First user input location: ')
        numbers = re.findall(r'\d+', input_string)

        if matrix[int(numbers[0])][int(numbers[1])] == None:
            matrix[int(numbers[0])][int(numbers[1])] = 0
        else:
            print('The area is not empty')
            continue
    else:
        input_string = input('Second user input location: ')
        numbers = re.findall(r'\d+', input_string)

        if matrix[int(numbers[0])][int(numbers[1])] == None:
            matrix[int(numbers[0])][int(numbers[1])] = 1
        else:
            print('The area is not empty')
            continue

    for i in range(3):
        if matrix[i][0] == matrix[i][1] == matrix[i][2] is not None:
            print(user_indicator(user_turn))
            break
        if matrix[0][i] == matrix[1][i] == matrix[2][i] is not None:
            print(user_indicator(user_turn))
            break

    # Check diagonals
    if matrix[0][0] == matrix[1][1] == matrix[2][2] is not None:
        print(user_indicator(user_turn))
        break
    if matrix[0][2] == matrix[1][1] == matrix[2][0] is not None:
        print(user_indicator(user_turn))
        break

    user_turn += 1
