from collections import Counter
import re
import csv

#Task 1
def get_second_most_repeated_word(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    words = re.findall(r'\b\w+\b', content.lower())

    word_counts = Counter(words)
    return word_counts.most_common(2)[1][0]

file_path = 'article.txt'
result = get_second_most_repeated_word(file_path)
print(result)

#Task 2
def copy_csv_to_text(csv_file, text_file):
    with open(csv_file, 'r', newline='', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        with open(text_file, 'w', encoding='utf-8') as text_file:
            for row in csv_reader:
                name = row['name']
                text_file.write(name + '\n')

csv_file_path = 'names.csv'
text_file_path = 'names.txt'

copy_csv_to_text(csv_file_path, text_file_path)


