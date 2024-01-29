# Task 2

input_number = int(input('გამრავლების ტაბულა მოცემულ რიცხვზე'))

for i in range(1, input_number+1):
    for j in range(1, 11):
        print(f"{i}*{j}={i*j}")

# Task 3
print("type your expenses")
total_budget = 3000

while True:
    bank_input = int(input('expense'))
    if (not bank_input):
        print(total_budget)
        break
    if (bank_input > total_budget):
        print("Not enough money on account")
        continue
    total_budget -= bank_input

# Task 3
print("parrot")

while True:
    parrot_input = input('Type anything')
    if (parrot_input == "quit"):
        break
    print("User Said Whaaat!?")
    print(f"User Said {parrot_input}")
