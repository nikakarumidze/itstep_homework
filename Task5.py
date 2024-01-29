# Task 1
consumer_info = []
for i in range(3):
    user_name = input('name: ')
    user_lastname = input('lastname: ')
    user_age = int(input('age: '))
    consumer_info.append([user_name, user_lastname, user_age])

user_index = int(input('which user info do you want? '))

if 0 <= user_index < len(consumer_info):
    user = consumer_info[user_index]
    print(f"""
          Name: {user[0]}
          Lastname: {user[1]}
          Age: {user[2]}
          """)
else:
    print('The User on this index does not exists')

# Task 2
user_database = []

user_input_2 = input('Name: ')
user_password_2 = input('Password: ')

if not len(user_input_2) or len(user_password_2) < 8:
    print('Problem with input')
else:
    user_database.append([user_input_2, user_password_2])
    print('successfuly registered')


user_login_name = input('login name ')
user_login_password = input('login password ')

has_found = False

for user in user_database:
    if user[0] == user_login_name:
        if user[1] == user_login_password:
            has_found = True
            print('successfuly logged in')
            break

if not has_found:
    print('user or password is incorrect')

# Task 3\
actors_info = [
    {"name": "Tom", "surname": "Hanks", "age": 65, "nationality": "American",
        "movies": ["Forrest Gump", "Saving Private Ryan", "Cast Away"]},
    {"name": "Meryl", "surname": "Streep", "age": 72, "nationality": "American",
        "movies": ["The Devil Wears Prada", "Sophie's Choice", "Mamma Mia!"]},
    {"name": "Leonardo", "surname": "DiCaprio", "age": 47,
        "nationality": "American", "movies": ["Titanic", "Inception", "The Revenant"]},
    {"name": "Jennifer", "surname": "Lawrence", "age": 31, "nationality": "American",
        "movies": ["The Hunger Games", "Silver Linings Playbook", "Joy"]},
    {"name": "Will", "surname": "Smith", "age": 53, "nationality": "American",
        "movies": ["Men in Black", "The Pursuit of Happyness", "Independence Day"]}
]


def get_actor_info(name, surname):
    for actor in actors_info:
        if actor["name"].lower() == name.lower() and actor["surname"].lower() == surname.lower():
            return actor
    return None


input_name = input("Enter actor's name: ")
input_surname = input("Enter actor's surname: ")

# display actor information
actor_info = get_actor_info(input_name, input_surname)
if actor_info:
    print("\nActor Information:")
    print(f"Name: {actor_info['name']} {actor_info['surname']}")
    print(f"Age: {actor_info['age']}")
    print(f"Nationality: {actor_info['nationality']}")
    print("Movies:", ", ".join(actor_info['movies']))
else:
    print("Actor not found in the database.")
