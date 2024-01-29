import os

#Task 1
def capture_customer_input():
    # Enter your file name
    file_name = "customer_data.txt"
    
    with open(file_name, 'a') as file:
        print("Enter customer information. Type 'enough' to stop.")
        
        while True:
            customer_input = input("Enter data: ")
            
            if customer_input.lower() == 'enough':
                print("Customer input completed. Data saved to", file_name)
                break
            
            file.write(customer_input + '\n')

capture_customer_input()

#Task 2
def create_file_info():
    location = input("Enter folder location: ")
    file_name = input("Enter the file name: ")
    pathname = location + file_name
    
    with open(pathname, 'x') as file:
            print(f"File '{pathname}' created successfully at location: {location}")

            file_names = os.listdir(location)

            print("File names in the folder: ")
            for name in file_names:
                print(name)

create_file_info()
