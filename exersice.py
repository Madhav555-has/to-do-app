# name = input("Enter the name of the new member")
# file = open("members.txt",'r')
# text = file.read()
# file.close()
# file = open("members.txt", 'w')
# print(f"{text}" + f"\n" + f"{name}")
#


# file.close()
# filenames = ["file1.txt", "file2.txt", "file3.txt"]
# for filename in filenames:
#     file = open(f'{filename}','w')
#     file.write("Hello")
#     file.close()


# filenames = ['a.txt', 'b.txt', 'c.txt']
# # for filename in filenames:
# #     file = open(f'{filename}', 'r')
# #     text = file.read()
# #     print(text)
# #     file.close()

# filenames = ["1.doc", "1.report", "1.presentation"]
# for filename in filenames:
#     filename = filename.replace('.', '-')
#     filenames.append(filename)
# print(filenames)

# names = ["john smith", "jay santi", "eva kuki"]
# new_names = [name.title() for name in names]
# print(new_names)

# usernames = ["john 1990", "alberta1970", "magnola2000"]
# new_usernames = [len(username) for username in usernames]
# print(new_usernames)

# user_entries = ['10', '19.1', '20']
# new_user_entries = [float(user_entry) for user_entry in user_entries]
# print(new_user_entries)

# user_entries = ['10', '19.1', '20']
# new_user_entries = [float(user_entry) for user_entry in user_entries];
# print(sum(new_user_entries))

# i=0
# while True:
#     inp = input("Throw the coin and enter heads or tail here?")
#     match inp:
#         case 'head':
#             i=i+100
#             print("Head%",i)
#         case 'tails':
#             i=i-100
#             print("Head",i)
#         case 'exit':
#             break

# try:
#     width = float(input("Enter the width of rectangle:"))
#     length = float(input("Enter the length of rectangle:"))
#     if width != length:
#         area = width*length
#     print("The area of the rectangle is:", area)
# except:
#     print("Enter a valid input")

# try:
#     total_value = float(input("Enter the total value:"))
#     try:
#         if total_value != 0:
#             value = float(input("Enter the value:"))
#             percentage = (100*value)/total_value
#             print("Percentage is :", percentage, "%")
#     except:
#         print("Your total value can not be zero")
# except:
#     print("You need to enter a number, run program again.")

# try:
#     waiting_list = ["john", "marry"]
#     name = input("Enter name: ")
#     number = waiting_list.index(name)
# except:
#     print("The given name is not in the list")
#     print(f"{name}'s turn is {number}")

# def calculate_time(h, g=9.80665):
#     t = (2 * h / g) ** 0.5
#     return t
#
#
# time = calculate_time(100)
# print(time)

# def age(date_of_birth, current_year=2023):
#     agge = current_year-date_of_birth
#     return agge
# birth_date = int(input("Enter your birthdate:"))
# your_age = age(birth_date)
# if your_age<=120:
#     print("Your age is less than 120")
# else:
#     print("Your age is more than 120")

# names = []
# while True:
#     name = input("Enter name")
#     if name != 'exit':
#         names.append(name)
#     elif name == 'exit':
#         break
# print(len(names))

x = float(input("Enter the temperature:"))
def status(temperature):
    if temperature<0:
        print("Solid")
    elif 0<temperature<100:
        print("Liquid")
    else:
        print("Gas")

form = status(x)


