# 1
first_input = input('Let me count symbols: ')
letters = 0
digits = 0
symbols = 0

for letter in first_input:
    if letter.isalpha():
        letters += 1
    elif letter.isdigit():
        digits += 1
    else:
        symbols += 1
print(f"letters: {letters}, digits: {digits}, symbols: {symbols}")

# 2
first_sentence = input('First sentence: ')
second_sentence = input('Second sentence: ')

first_sentence_length = len(first_sentence)
second_sentence_length = len(second_sentence)

longest_sentence = max(first_sentence_length, second_sentence_length)

output_sentence = ''
index = 0

while index < longest_sentence:
    if first_sentence_length > index:
        output_sentence += first_sentence[index]
    if second_sentence_length - index > 0:
        output_sentence += second_sentence[-index - 1]
    index += 1

print(output_sentence)

# 3
first_sent = input('first sent: ')
second_sent = input('second sent: ')

unique_chars_first = set(first_sent)
unique_chars_second = set(second_sent)

if unique_chars_first == unique_chars_second:
    print('Strings are balanced!')
else:
    print('Strings are not balanced!')
