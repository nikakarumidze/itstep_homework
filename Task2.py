# Task 1

victorina1 = input("""
                   რომელი იმპერიის მიერ აგებულ იწყალ-მომარაგების სისტემა(აკვედუკი) ფუნქციონირებს დღესაც?
                   1.შუმერთა
                   2.სელჩუკთა
                   3.რომის
                   4.მონღოლთა
                   """)

if victorina1 == 'რომის' or victorina1 == str(3):
    print('სწორია!')
else:
    print('არა! სწორი პასუხია რომის!')

# Task 2

victorina2 = input("""
                   ამოირჩიე:
                  1.ლეპტოპები
                  2.პერსონალური კომპიუტერები
                  3.მობილურები
                   """)

victorina2_budget = int(input('Budget'))

if victorina2 == str(1) or 'ლეპტოპები':
    if (victorina2_budget > 1000):
        print('Dell XPS')
    if (victorina2_budget > 500):
        print('პენტიუმ 4 5ის ნაწილებით')
    else:
        print('არაფერი მოგივა')


elif victorina2 == str(2) or 'პერსონალური კომპიუტერები':
    if (victorina2_budget > 1000):
        print('Dell XPS')
    if (victorina2_budget > 500):
        print('intel i3 6000U')
    else:
        print('არაფერი მოგივა')

elif victorina2 == str(3) or 'მობილურები':
    if (victorina2_budget > 1000):
        print('iPhone 20')
    if (victorina2_budget > 500):
        print('iPhone X')
    else:
        print('არაფერი მოგივა')

# Task 3

quest_rules = input('If you lose, you pay me 5000$ usd, proceed? y/n')

if quest_rules == 'y':
    choice = input("""
                     Choose Door:
                     1
                     2
                     3
                     """)
    if choice == "1":
        print("\nYou open the door on the left and find a treasure chest!")
        print("Congratulations! You win!")
    elif choice == "2":
        print("\nYou open the door in the middle and encounter a fierce dragon.")
        print("The dragon breathes fire, and you are burned to ashes. Game over!")
    elif choice == "3":
        print("\nYou open the door on the right and fall into a deep pit.")
        print("Unfortunately, you couldn't survive the fall. Game over!")
elif quest_rules == 'n':
    print('bye :(')

print("Welcome to the Career Questionnaire!")
name = input("What is your name? ")
print(f"\nHello, {name}! Let's get started.")

answer1 = input("\nWhat subjects do you enjoy the most?\n"
                "a. Science and Math\n"
                "b. Arts and Humanities\n"
                "c. Both\n")


answer2 = input("\nWhat type of activities do you find most interesting?\n"
                "a. Problem-solving and analyzing data\n"
                "b. Creativity and artistic expression\n"
                "c. Both\n")
answer3 = input("\nWhat work environment do you prefer?\n"
                "a. Lab or office setting\n"
                "b. Art studio or creative space\n"
                "c. Both\n")

if answer1 == 'a' and answer2 == 'a' and answer3 == 'a':
    print("You might enjoy a career in Science or Technology.")
elif answer1 == 'b' and answer2 == 'b' and answer3 == 'b':
    print("You might enjoy a career in the Arts or Humanities.")
elif (answer1 == 'c' and answer2 == 'c') or (answer1 == 'c' and answer3 == 'c') or (answer2 == 'c' and answer3 == 'c'):
    print("You have diverse interests! Consider a career that combines both Science/Technology and Arts/Humanities.")
else:
    print("Your preferences are unique! Explore different career options based on your interests.")
