#while loop
# x=15
# while x >  10:
#     print (x)
#     x = x - 1
# print('test finish')    

#break and continue statement

# for i in range(1,10):
#     if i ==6:
#         break
#     print(i)
        
# for i in range(1,10):
#     if i ==6:
#         continue
#     print(i)
        
#exercise 1
# import random
# option = 'yes'
# while option == 'yes':
#     computer_no = random.randint (1,20)
#     #print(computer_no)
#     user_no = int(input('Enter a guess no:'))
#     if user_no > computer_no:
#        print (' Your guess number is too high')
#     elif user_no < computer_no:
#        print ( 'Your guess number is too low')
#     else:
#        print(' correct the answer')
#     option = input ('Enter your option yes or no:')

#Exercise 2 h.w

#Exercise 3 
# username = 'steph'
# password = '132'
# input_username = input ('Enter a username')
# input_passport = input('Enter a password:')
# while input_username != username and input_passport != password:
#     input_username = input ('Enter a username')
#     input_passport = input('Enter a password:')
# if input_username == username and input_passport == password:
#     print('Welcome')
# else:
#     print('Error Message')

#Exercise 4 

#programming construct in python(string and list). pdf
#exercise h.w

# str = 'WisdomC'
# print(str[0])
# print(str[-1])

# def calculator():
#     while True:
#         print("Select an operation:")
#         print("1. Addition (+)")
#         print("2. Subtraction (-)")
#         print("3. Multiplication (*)")
#         print("4. Division (/)")
        
#         choice = input("Enter choice (1/2/3/4): ")
        
#         if choice in ['1', '2', '3', '4']:
#             try:
#                 num1 = float(input("Enter first number: "))
#                 num2 = float(input("Enter second number: "))
#             except ValueError:
#                 print("Invalid input. Please enter numbers.")
#                 continue

#             if choice == '1':
#                 result = num1 + num2
#                 print(f"The result is: {result}")
#             elif choice == '2':
#                 result = num1 - num2
#                 print(f"The result is: {result}")
#             elif choice == '3':
#                 result = num1 * num2
#                 print(f"The result is: {result}")
#             elif choice == '4':
#                 if num2 != 0:
#                     result = num1 / num2
#                     print(f"The result is: {result}")
#                 else:
#                     print("Cannot divide by zero.")
#         else:
#             print("Invalid choice. Please select from 1 to 4.")

#         again = input("Do you want to perform another calculation? (yes/no): ").lower()
#         if again != 'yes':
#             print("Thank you for using the calculator.")
#             break

# calculator()

#slicing **

# str= 'wisdomc collage'
# print(str[1:6])
# print(str[:10])
# print(str[0:14:2])
# print(str[-1:-15:-2])
# print(str[::-1])

#Multiline string
# message="""
# Never gonna give you up
# Never gonna let you down """
# print(message)

#String operations
# str1 = 'Hello'
# str2 = 'WisdonC'
# str3 = 'Hello'
# print(str1 == str2)
# print(str1 == str3)
# print(str1 + str2)

# school_name = 'WisdonC Collage'
# new_school_name = school_name.replace('Collage','university') 
# print(new_school_name)
# print(school_name.replace('Collage','university'))
# print (school_name)
# for index in school_name:
#      print(index)
# print(len(school_name))
#String Membership test
# print ('C' in school_name)

#Exercise 1
# word = input('Enter a word')
# if len(word) == 2:
#     wholenumber = int(input('Enter the whole number:'))
#     decimalnumber = float(input('Enter the decimal number')) 
#     code= str(wholenumber)+ word[::-1] + str(int(decimalnumber))
#     print('Product code:', code)
# else:
#     print('Enter, please enter two words')

#Exercise 2
# str = input('Enter a string')
# if ('a' in str) or ('e'in str) or ('i'in str) or ('o'in str) or ('u'in str):
#      print('string has vowel character')
# else:
#     print('String has not vowel character')

#Exercise 3
# str = input('Enter a string : ')
# result = str[0]+str[len(str)//2] = str[-1]
# print(result)

#Exercise 4 h.w
#Exercose 5 h.w [:3]

#length of a list
# color = ['green','yellow','red','pink']
# print(color)
# print(color[0])
# print(color[-1])
# color[0]='purple'
# print(color)

# color = ['green','yellow','red','pink']
# list =[2,'syw',34.2,True,[1,2,3,4]]
# for index in range (len(list)):
#     print(list[index])
# print(list)
# print(color[1:])
# print(len(color))

# a = 6
# arr = [0]*a
# print(arr)

# list = list([5,7,'syw,',7.50])
# list.append ('software engr')
# print(list)

# list = list ([5,7,'syw,',7.50])
# list.insert (3,56)
# print(list)

# list = list([5, 8, 'Tom', 7.50])
# list.extend([25, 75, 100])
# print(list) 

# my_list = [2, 4, 6, 8]
# for i in range(len(my_list)):
#      square = my_list[i] * my_list[i]
#      my_list[i] = square
# print(my_list)
# newlist = []
# for i in my_list:
#     square_value = i*i
#     newlist.append (square_value)
# print (newlist)

# list = [2,3,4,5,6,8,9,]
# list.remove(6)
# list.remove(8)
# print(list)

# list = [2,3,4,5,6,8,9,]
# list.pop(2)
# print(list)

# list = [2,4,3,5,7,6,8,9,6,4,2,5,6,8,9,]
# list.sort()
# print(list)
# list.sort(reverse='True')
# print(list)

# list = [3, 4, 5, 6, 1]
# print(max(list))
# print(min(list))
# print(sum(list))


#exercise 1 h.w

#exercise 2
# list1 = [5, 20, 15, 20, 25, 50, 20]
# for index in list1:
#     if index == 20:
#         list1.remove(index)
# print(list1)

#exeercise 3 h.w
# dec_no = int(input('Enter a deximal number(0-255): '))
# while dec_no <0 or dec_no>255:
#     dec_no= int(input('Enter a deximal number(0-255): '))
# blist = []
# value=128
# while value > 0:
#     if dec_no >=value:
#         blist.append(1)
#         dec_no= dec_no- value
#     else:
#         blist.append(0)
#     value = value //2
# bstring = ''
# for bit in blist:
#     # print(bit,end='')
#     bstring = bstring + str(bit)
# print('Binary representation is : ', bstring)

#a = [[1, 2, 3], [4, 5, 6], [34,55,12]]
#     for i in index:
#         print(i)
# print(a[0])
# print(a[0][0])
# a.append()
# print(a)
# print(len(a))
# print(a[2][1])

# a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
# for i in range(len(a)):
#    for j in range(len(a[i])):
#     print(a[i][j], end=' ')
# print()

#exercise 5 h.w
#exercise 1and2 2d list


#Tuple, Set and dictionary pdf.file

#Tuple 
# num_tuple=(10,11,20,25.45)
# print(num_tuple)

# tuple1 = 1,2,"Hello"
# print(tuple1)

# i,j,k=tuple1
# print(i,j,k)

# tuple1 = (10,20,30,40,50)
# position = tuple1.index(30)
# print(position)
# tuple2 = (10, 20, 30, 40, 50, 60, 70, 80)
# position = tuple2.index(60,4,6)
# print(position)
# position = tuple1.index(100)
# print(position)

# tuple1 = (10, 20, 30, 50, 40, 50, 60, 70, 80)
# # count=0
# value = int (input('Enter a value: '))
# # for i in tuple1:
# if(value in tuple1):
#     #  count = count + value 
#     value+= 1
#     print(value)
# else:
#     print('value not found')
# # print(50 in tuple1)
# # print(500 in tuple1)

# tuple1 = (0,1,2,3,4,5)
# sample_list=list(tuple1)
# sample_list.append(6)
# tuple1 = tuple(sample_list)
# print(tuple1)
# for i in tuple1:
#     print(i, end=' ')

# tu1 = (10,20,60,60,30,60,40)
# count = tu1.count(60)
# print(count)

# count= tu1.count(600)
# print(count)

# tuple1 = (0,1,2,3,4,5,)
# tuple2 = tuple1
# print(tuple2)

# tuple1 = (1,2,3,4,5)
# tuple2 = (3,4,5,6,7)
# # tuple3 = tuple1 + tuple2
# # print (tuple3)

# tuple3 = sum((tuple1,tuple2),())
# print(tuple3)

# nested_tuple = ((20,40,60,), (10,30,50),'python')
# print(nested_tuple[2][0])
# for i in nested_tuple:
#     print('tuple', i, 'elements')
#     for j in i:
#         print(j,end=',')
#         print('\n')

# tuple1 = ('wyeu','yoeu','abc')
# print(max(tuple1))
# print(min(tuple1))

# tuple2 = ('11','22','33','yellow')
# print(max(tuple2))
# print(min(tuple2))

# tuple1 = (10, 20, 30, 40, 50)
# rev_tuple = tuple1[::-1]
# print(rev_tuple)

# tuple1 = ('Orange',[10,20,30],(5,15,25))
# print(tuple1[1][1])

# tuple1 = (50,10,60,70,50)
# count=tuple1.count(50)
# print(count)



#Week5
# sample_set = [ 'Mark','jessa',25,278.4]
# print(sample_set)

# num_list= [20,30,40,50,30,20,40,60]
# sample_set= set(num_list)
# print (sample_set)

# new_set = set()
# print(type(new_set))
# print()

# book_set = {'Harry Potter','slkdj','saung'}
# for book in book_set:
#     print(book)

# book_set = {"Angels and Demons", "Atlas Shrugged"}
# if 'Harry Potter' not in book_set:
#  print("Book does not exists in the book set")
# else:
#  print('book exists in the book set')

# bk_set = {' Harry Potter', 'Angels and demons'}
# bk_set.add ('the god of small things')
# print(bk_set)

# bk_set.update(['stlas shrugged', 'high'])
# print(bk_set)

# color_set= {'red', 'orange', 'yellow', 'white', 'black'}
# color_set.remove('yellow')
# print(color_set)
# color_set.discard('white')
# print(color_set)

# color_set = {'violet', 'indigo', 'blue', 'green', 'yellow'}
# remaining_colors = {'indigo', 'orange', 'red'}
# vibgyor_colors = color_set | remaining_colors
# print(vibgyor_colors)
# vibgyor_colors = color_set.union(remaining_colors)
# print(vibgyor_colors)

# color_set= {'violet', 'indigo','blue'}
# remaining_color= {'indigo','orange','red'}
# new_set= color_set & remaining_color
# print(new_set)
# new_set = color_set.intersection(remaining_color)
# print(new_set)

# color_set = {'violet', 'indigo', 'blue', 'green', 'yellow'}
# remaining_colors = {'indigo', 'orange', 'red'}
# common_colors = color_set.intersection(remaining_colors)
# print(common_colors)
# print(color_set)
# color_set.intersection_update(remaining_colors)
# print(color_set)

# color_set = {'violet', 'indigo', 'blue', 'green', 'yellow'}
# remaining_colors = {'indigo', 'orange', 'red'}
# print(color_set- remaining_colors)
# print(color_set.difference(remaining_colors))

# A = {2,3,4}
# B = {1,2,6}
# print('using^:',A^B)
# print('using symmetric_difference():',A.symmetric_difference(B))

# A = {1, 3, 5}
# B = {3, 5, 1}
# if A == B:
#  print('Set A and Set B are equal')
# else:
#  print('Set A and Set B are not equal')

# set1 = {10, 20, 30, 40, 50}
# set2 = {60, 70, 80, 90, 10}

# common_element = set1 & set2
# print(common_element)
 
# sample_set = {"Yellow", "Orange", "Black"}
#sample_list = ["Blue", "Green", "Red"]
# if 'Yellow' in sample_set:
#     sample_set.remove('Yellow')
#     print('already removed',sample_set)
# sample_set.update(sample_list)
# print (sample_set)

#Dictionaries
# person = {"name":"jessa","country":"USA","telephone":"1178"}
# print(person.get('telephone'))
# print(person.keys())
# print(person.values())
# print(person.items())
# print(person.get('name'))
#for key in person:
#     print(key,":",person.get(key))
#     print(key,":",person[key])
# for key_value in person.items():
#     print(key_value[0],key_value[1])
# print(len(person))
# person["weight"]=50
# person.update({"Height":6,"age":30})
# print(person)
# person.setdefault('state','Texas')
# person.setdefault('zip')
# person.setdefault('country','Canada')
# for key,value in person.items():
#     print(key,':',value)
# deleted_item=person.popitem()
# print(deleted_item)
# print(person)
# del person['weight']
# print(person)
# person.clear()
# print(person)
# key_name='country'
# if key_name in person.keys():
#     print('country name is',person[key_name])
# else:
#     print('key not found')
# person1 = {'Jessa': 70, 'Arul': 80, 'Emma': 55}
# perosn2 = {'Kelly': 68, 'Harry': 50, 'Olivia': 66}
# person1.update(person2)
# print(person1)
# student_dict1 = {'Aadya': 1, 'Arul': 2, }
# student_dict2 = {'Harry': 5, 'Olivia': 6}
# student_dict3 = {'Nancy': 7, 'Perry': 9}
# student_dict = {**student_dict1, **student_dict2, **student_dict3}
# print(student_dict)
# dict1={'jessa':70,'Emma':55}
#dict2=dict1
# dict2=dict1.copy()
# dict2.update({'jessa':90})
# print(dict2)
# print(dict1)
# address = {"state": "Texas", 'city': 'Houston'}
# person = {'name': 'Jessa', 'company': 'Google', 'address': address}
# print("person:", person)
# print("City:", person['address']['city'])
# print("Person details")
# for key, value in person.items():
#  if key == 'address':
#   print("Person Address")
# for key, value in person.items():
#     if key =='adress':
#         print('person adress')
#         for nested_key, nested_value in value.items():
#             print(nested_key, ':',nested_value)
# else:
#     print(key,':',value)
# jessa = {'name': 'Jessa', 'state': 'Texas', 'city': 'Houston', 'marks': 75}
# emma = {'name': 'Emma', 'state': 'Texas', 'city': 'Dallas', 'marks': 60}
# kelly = {'name': 'Kelly', 'state': 'Texas', 'city': 'Austin', 'marks': 85}
# class_six = {'student1': jessa, 'student2': emma, 'student3': kelly}
# print("Student 3 name:", class_six['student3']['name'])
# print('Student 3 marks:',class_six['student3']['name'])
# print("Student 3 marks:", class_six['student3']['marks'])
# print("\nClass details\n")
# for key, value in class_six.items():
#    print(key)
# for nested_key, nested_value in value.items():
#  print(nested_key, ':', nested_value)
#  print('\n') 
# dict1 = {'c': 45, 'b': 95, 'a': 35}
# print(sorted(dict1.items()))
# print(sorted(dict1))
# print(sorted(dict1.values()))
# dict = {1:'aaa',2:'bbb',3:'AAA'}
# print('Maximum :',max(dict)) 
# print('Minimum :',min(dict))

#all any read kah homework slide (87)

#Function in phython
# def add():
#     a = 10 
#     b = 2
#     c = a + b
#     return(c)

# sum=add()
# print(add())

# def add (num1, num2):
#     print('Number 1:',num1)
#     print('Number 2:',num1)
#     addition = num1 + num2
#     return addition
# res = add(2,4)
# res1 = add(7,8)
# print(res)
# print(res1)
# def greet():
#     print('Hello World!')
# greet()
# print('Outside function')

# def course_func(name,course_name):
#     print(' Hello',name,'Welcome to WosdomC')
#     print('Your course name is',course_name)
# course_func('John','python')

# def is_even(list1):
#     even_num = []
#     for n in list1:
#         if n %2 == 0:
#             even_num.append(n)
#     return even_num
# even_num=is_even([2,3,42,51,62,70,5,9])
# print('Even number are:',even_num)

# def arithmetic (num1,num2):
#     add = num1 +num2
#     sub = num1 - num2
#     multiply = num1 * num2
#     division = num1 / num2
#     return add, sub,multiply, division
# a,b,c,d = arithmetic (10,2)
# print('addition:',a)
# print('subtraction:',b)
# print('multiplication:',c)
# print('division:',d)

# def sum(a,b):
#     add= a+b
#     print('Addition of two number:', add)

# def sub(a,b):
#     if a < b :
#         print('This number cant be Subtract')
#     else:
#         add = a - b
#         print('Subtraction of two numbers:', add)

# def mult(a,b):
#     add = a*b
#     print('multply of two numbers:' ,add)


# num1 = int(input('Enter number 1: '))
# num2 = int(input('Enter number 2'))
# sum(num1,num2)
# sub(num1,num2)
# mult(num1,num2)

# def login(users):
#     'Username and pin'
#     username= input('Enter you username:')
#     pin= input('Enter your 4-digit PIN:')

#     for user in users:
#         if user[0]== username and user[1]==pin:
#             return user
#     print ('Invalid username or pin. please try again.')
#     return None

# def show_menu():
#     'display the ATM menu option'
#     print('ATM menu:')
#     print('1. Check Balance')
#     print('2. deposit Money')
#     print('3. Withdraw Money')
#     print('4. Exit')

#     while True:
#         try:
#             choice = int(input('Enter your choice (1-4):'))
#             if 1 <= choice <= 4:
#                 return choice
#             else:
#                 print('Please enter a number between 1 and 4.')
#         except ValueError:
#             print('invalid input. Please enter a number.')

# def check_balance(user):
#     "deposit money into the user's account"
#     print(f' your current balance is : $ {user[2]:.2f}')

# def deposit (user):
#     "Deposit money into the user's account"
#     while True:
#         try:
#             amount = float (input('Enter amount to deposit: $'))
#             if amount > 0:
#                 user[2]+= amount
#                 print(f"${amount:.2f} has been deposited successfully.")
#                 print(f"New balance: $ (user[2]:.2f)")
#                 break
#             else:
#                 print('Please enter a positive amount.')
#         except ValueError:
#             print('Invalid amount. please enter a number.')
# def withdraw (user):
#     "ithdraw monet from the user's account if sufficient balance exists"
#     while True:
#         try:
#             amount = float (input('Enter amount to withdraw:$'))
#             if amount <= 0:
#                 print("Please enter a positive amount.")
#             elif amount > user[2]:
#                 print("Insufficient funds. Please enter a smaller amount.")
#             else:
#                 user[2] -= amount
#                 print(f"${amount:.2f} has been withdrawn successfully.")
#                 print(f"New balance: ${user[2]:.2f}")
#                 break
#         except ValueError:
#             print("Invalid amount. Please enter a number.")

# def main():
#     # Initialize user data (username, PIN, balance)
#     users = [
#         ["john_doe", "1234", 1000.00],
#         ["jane_smith", "5678", 2500.50],
#         ["alex_wong", "4321", 500.75]
#     ]
    
#     print("Welcome to the ATM System")
    
#     # Login
#     current_user = None
#     while current_user is None:
#         current_user = login(users)
    
#     # ATM operations
#     while True:
#         choice = show_menu()
        
#         if choice == 1:
#             check_balance(current_user)
#         elif choice == 2:
#             deposit(current_user)
#         elif choice == 3:
#             withdraw(current_user)
#         elif choice == 4:
#             print("\nThank you for using the ATM. Goodbye!")
#             break

# if __name__ == "__main__":
#     main()

#global_var = 5
# def function1():
#     global global_var
#     global_var = 555
#     print('Value in 1st function:',global_var)
# def function2():
#     print('Value in 2nd function:', global_var)
# def function3():
#     print('Value in 3rd function:', global_var)
# function1()
# function2()
# function3()

# def outer_func():
#     x = 777
#     def inner_func():
#         nonlocal x
#         x=700
#         print('Value of x inside inner function is:',x)
#     inner_func
#     print('Value of x inside outer function is:',x)
# outer_func

# def factorial(no):
#     if no == 0:
#         return 1
#     else:
#         return no * factorial(no - 1)
# print("factorial of a number is:", factorial(8))

# def even_numbers(nums):
#     even_list = []
#     for n in nums:
#         if n % 2 == 0:
#             even_list.append(n)
#     return even_list

# num_list = [10, 5, 12, 78, 6, 1, 7, 9]
# ans = even_numbers(num_list)
# print("Even numbers are:", ans)

# l = [10, 5, 12, 78, 6, 1, 7, 9]
# even_nos = list(filter(lambda x: x % 2 == 0, l))
# print("Even numbers are: ", even_nos)

# numbers = [1, 2, 3, 4]
# squares = map(lambda x: x ** 2, numbers)
# print(list(squares))

# from functools import reduce
# numbers = [1, 2, 3, 4]
# product = reduce(lambda x, y: x * y, numbers)
# print(product)

# myfile = open('testfile.txt','w')
# myfile.write('Hello')
# myfile.close()

# file = open('testfile.txt','r')
# print(file.read())
# file.close

# import os
# print(os.getcwd()) 

# import os
# os.mkdir('test')
# print(os.listdir())

# import csv
# with open('data.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(["SN", "Movie", "Protagonist"])
#     writer.writerow([1, "Lord of the Rings", "Frodo Baggins"])
#     writer.writerow([2, "Harry Potter", "Harry Potter"]) 


# import csv
# with open ('data.csv','r') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)

#Exception

# try:
#     numerator = 10
#     denominator = 0
#     result = numerator/denominator
#     print(result)
# except:
#     print('Error:Denominator cannot be 0.')

# try:
#     even_numbers = [2,4,6,8]
#     print(even_numbers[5])
# except ZeroDivisionError:
#     print('Denominator cannot be 0 .')
# except IndexError:
#     print('Index Out of Bound.')

# try:
#     num = int(input('Enter a number:'))
#     assert num % 2 == 0
# except:
#     print('Not an even number!')
# else:
#     reciprocal =1/num
#     print(reciprocal)              

# try:
#     numerator=10
#     denoiminator=0
#     result=numerator/denoiminator
#     print(result)
# except:
#     print('Error:Denominator cannot be 0.')
# finally:
#     print('This is finally block.')

# class InvalidAgeException(Exception):
#     'Raised when the inpur calue is less than 18'
#     pass
# number = 18
# try:
#     input_num = int(input('Enter a number:'))
#     if input_num < number :
#         raise InvalidAgeException
#     else:
#         print('Eligible to Vote')
# except InvalidAgeException:
#     print('Exception occurred: invalid Age')
    
# class Student:
#     def show (self):
#         print('My name is syw')
# syw = Student ()
# syw.show()

# class A:
#     def display (self):
#         print('syw')
# obj = A()
# obj.display()

# class B:
#     def __init__(self):
#         self.name='SYW'
#     def display(self):
#         print(self.name)
# obj=B()
# obj.display()

# class C:
#     def __init__(self,name,age):
#         self.name= name
#         self.age = age
#     def display(self):
#         print(self.name,self.age)
# obj = C('SYW','17')
# obj.display()

#instance methods
# class student:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def show(self):
#         print('Name:', self.name, 'Age:',self.age)
# obj = student('SYW',17)
# obj.show()

# class student:
#     school_name = 'WisdomC' 

#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     @classmethod
#     def change_school (cls, name):
#         print( student.school_name)
#         student.school_name = name
# obj = student ('SYW',17)
# student.change_school('WisdomC')

# class student:
#     @staticmethod
#     def sample(x):
#         print('Inside static method',x)
# student.sample(5)

# obj = student()
# student.sample(15)

# class student:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def display(self):
#         print('Name:', self.name, 'Age:', self.age)
#     @staticmethod
#     def show ():
#         print('WisdomC')
# # student.show ()
# obj = student('Saung Yu Wady', 17)
# obj.display (), obj.show()
        
# class Vehicle:
#     def Vehicle_info(self):
#         print('Inside Vehicle class')
# class Car (Vehicle):
#     def car_info(self):
#         print('Inside Car class')
# car = Car()
# car.Vehicle_info()
# car.car_info()

# class University:
#     def __init__(self):
#         self.batch='Batch 2'
#     def call_batch(self):
#         print('The batch name is batch 2')

# class Student ( University ):
#     def __init__(self,major):
#         self.major = major
#     def call_major(self):
#         print('My major name is:', self.major)        

# syw = Student('Computer Science')
# syw.call_major()
# # syw.call_batch()
# uni = University()
# uni.call_batch()

# class person:
#     def person_info(self,name,age):
#         print('Inside person class')
#         print('Name:',name,'Age:',age)
# class Company:
#     def company_info(self,company_name,location):
#         print('inside company class')
#         print('Name:',company_name,'location:',location)
# class employee(person,Company):
#     def employee_info (self,salary,skill):
#         print('inside employee class')
#         print('salary:',salary,'skill:',skill)
# emp = employee()
# emp.person_info('syw',25)
# emp.company_info('Google', 'Atlanta')
# emp.employee_info(12000,'Machine Learning')

#slide 31 exercise
# class Vehicle:
#     def Vehicle_info(self):
#         print('Inside Vehicle class

#exercise page 54 and page 75

#Polymorphism

# import tkinter as tk
# root = tk.Tk()
# root.title('Frame')
# frame = tk.Frame(root,width=500, height= 300, bg= 'lightblue')
# frame.grid()
# root.resizable(True,True)

# # root.mainloop()
 
# from tkinter import ttk
# from tkinter import messagebox
# import tkinter as tk
# s = tk.Tk()
# s.title('Login Form')

# login_frame = ttk.Labelframe(s,text='Login From', padding= '10')
# login_frame.grid( row=0,column=0,padx=20,pady=20,sticky='nsew')

# username_lable = ttk.Label(login_frame, text='UserName:')
# username_lable.grid(row=0,column=0,padx=10,pady=10,sticky='w')

# username_lable = ttk.Label(login_frame, text='Password:')
# username_lable.grid(row=1,column=0,padx=10,pady=10,sticky='w')

# username_entry= ttk.Entry(login_frame)
# username_entry.grid(row=0,column=1,padx=10,pady=10,sticky='w')

# password_lable = ttk.Label(login_frame,text='password:')
# password_lable.grid(row=1, column=0, padx=10, pady=10, sticky="w")

# password_Entry= ttk.Entry(login_frame,show='*')
# password_Entry.grid(row=1, column=1, padx=10, pady=10)

# def action_login():
#     username = username_entry.get()
#     password = password_Entry.get()
#     if  username == ''or password == '':
#                 messagebox.showerror("Error", "Please enter both username and password.")
#         # result_label.config(text= 'Please enter both user name and password', foreground= 'red')
#     else:
#         # result_label.config(text=f'Welcome, {username}!', foreground= 'green')
#         messagebox.showinfo('Welcome',f"Welcome,{username}!")
# login_button = ttk.Button(s, text="Login", command= action_login)
# login_button.grid(row=2, column=0, pady=10)

# def cancle_action():
#     username_entry.delete(0,tk.END) #clear username entry
#     password_Entry.delete(0,tk.END)
#     result_label.config(text='', foreground='black')

# cancle_botton = ttk.Button(s, text='Cancle', command=cancle_action )
# cancle_botton.grid(row=2, column=1, pady=10, padx=10) 

# result_label = ttk.Label(s, text="", foreground="black")
# result_label.grid(row=3, columnspan=2, pady=10)

# s.mainloop()

# import tkinter as tk
# from tkinter import ttk, messagebox

# s = tk.Tk()
# s.title('TreeView')
# s.geometry('450x300')

# #creating a treeview widget
# tree = ttk.Treeview(s, columns= ('Destination','Date', 'Price'), show='headings')
# tree.heading('Destination',text='Destination')
# tree.heading('Date', text='Date')
# tree.heading('Price',text='Price')

# #add sample data
# tree.insert('','end',values=('paris','2024-10-10','$5000'))
# tree.insert('','end',values=('New York','2024-12-20','$800') )
# tree.pack(pady=20)

#function totopen a new orm for adding an item
# def open_add_form():

#     add_window = tk.Toplevel(s) #creating a new popup window
#     add_window.title('Add New Destination')
#     add_window.geometry("300x200")

#     # Labels and Entry Fields
#     tk.Label(add_window, text="Destination:").grid(row=0, column=0, padx=10, pady=5)
#     entry_dest = tk.Entry(add_window, width=20)
#     entry_dest.grid(row=0, column=1, padx=10, pady=5)

#     tk.Label(add_window, text="Date (YYYY-MM-DD):").grid(row=1, column=0, padx=10, pady=5)
#     entry_date = tk.Entry(add_window, width=20)
#     entry_date.grid(row=1, column=1, padx=10, pady=5)

#     tk.Label(add_window, text="Price ($):").grid(row=2, column=0, padx=10, pady=5)
#     entry_price = tk.Entry(add_window, width=20)
#     entry_price.grid(row=2, column=1, padx=10, pady=5)

#     def add_item():
#         destination = entry_dest.get()
#         date = entry_date.get()
#         price = entry_price.get()

#         if destination and date and price:
#             tree.insert('','end',values=(destination,date,price))
#             add_window.destroy()#close the popup window after ading
#         else:
#             messagebox.showerror('Error', 'All fields must be filled!')

    # btn_submit=tk.Button(add_window,text='Add',command=add_item)
    # btn_submit.grid(row=3,columnspan=2,pady=10)

# btn_open_form = tk.Button (s, text='Add Data', command=open_add_form)
# btn_open_form.pack(pady=10)

# # #function to edit an existing item
# def open_edit_form():
#     selected_item=tree.selection()
#     if not selected_item:
#         messagebox.showwarning('Warning','Please select an item to edit!:')

# # #Get sexected item data
#     item=selected_item[0]
#     values=tree.item(item,'values')
#     #create an edit opoup window
#     edit_window=tk.Toplevel (s)
#     edit_window.title("Edit Destination")
#     edit_window.geometry("300x200")
#     tk.Label(edit_window, text="Destination:").grid(row=0, column=0, padx=10, pady=5)
#     entry_dest = tk.Entry(edit_window, width=20)
#     entry_dest.grid(row=0, column=1, padx=10, pady=5)
#     entry_dest.insert(0, values[0])  # Pre-fill with existing data

#     tk.Label(edit_window, text="Date (YYYY-MM-DD):").grid(row=1, column=0, padx=10, pady=5)
#     entry_date = tk.Entry(edit_window, width=20)
#     entry_date.grid(row=1, column=1, padx=10, pady=5)
#     entry_date.insert(0, values[1])
#     tk.Label(edit_window, text="Price ($):").grid(row=2, column=0, padx=10, pady=5)
#     entry_price = tk.Entry(edit_window, width=20)
#     entry_price.grid(row=2, column=1, padx=10, pady=5)
#     entry_price.insert(0, values[2])

#function to update item
#     def update_item():
#         new_dest=entry_dest.get()
#         new_date=entry_date.get()
#         new_price=entry_price.get()
#         if new_dest and new_date and new_price:
#             tree.item(item, values=(new_dest, new_date, new_price))
#             edit_window.destroy()
#         else:
#             messagebox.showerror('Error,All fields must be filled!')

#     btn_edit_form= tk.Button(edit_window, text='Update', command=update_item)
#     btn_edit_form.grid(row=3,column=2)

# btn_open_form = tk.Button (s, text='Edit Data', command=open_edit_form)
# btn_open_form.pack(pady=10)

#Function to delete data
# def delete_item():
#     selected_item=tree.selection()
#     if not selected_item:
#         messagebox.showwarning('Warning','Please select an item to delete')
#         return
    
#     confirm= messagebox.askyesno('Confirm Delete','Are you sure you want to delete this destination?')
#     if confirm:
#         tree.delete(selected_item)
#     #Buttons for Edit and Delete
#     btn_delete=tk.button(s,text='Delete destination', command=delete_item)
#     btn_delete.pack(pady=50)

#Spinbox
# import tkinter as tk
# from tkinter import ttk
# root = tk.Tk()
# root.title('Spinbox example')

# def my_callback():
#     print(f'Spinbox value:{my_int_var.get()}')
# my_int_var= tk.IntVar(value=0)
# myspinbox=ttk.Spinbox (root,from_=0,to=100, increment=10,textvariable=my_int_var, command=my_callback)
# myspinbox.pack(pady=10)
# root.mainloop()

# #Checkbutton
# import tkinter as tk
# from tkinter import ttk

# def display_value():
#     value_label.config(text=f'Checkbutton Value:{my_dbl_var.get()}')

# #create main window
# root=tk.Tk()
# root.title('checkbutton Example')

# #create a variable to stor the checkbutton value
# my_dbl_var=tk.DoubleVar(value=0) #DoubleVar to store float values

# #creath checkbutton
# mycheckbutton2= ttk.Checkbutton(root,variable=my_dbl_var,text='Would you like Pi?',
# onvalue=3.14159, #value when checked
# offvalue=0, #value when unchecked
# underline=15, #calls function whem clicked
# command=display_value #calls function when clicked
# )

# mycheckbutton2.pack(pady=10)
# #create a lable to display the value
# value_label= ttk.Label(root,text='Checkbutton Value:0')
# value_label.pack(pady=10)
# #run the tkinter event loop
# root.mainloop()

# #Radiobutton
# import tkinter as tk
# from tkinter import ttk

# #function to update th lable with the selected value
# def display_value():
#     Value_label.config(text=f'Selected Value:{my_int_var.get()}')

# #create main window
# root=tk.Tk()
# root.title('Radiobutton example')

# #creawte an IntVar to store the selected radio button value
# my_int_var=tk.IntVar(value=0) #default value

# #create a frame to group the radio buttons
# buttons=tk.Frame(root)
# buttons.pack(pady=10)

# #create radiobuttons
# r1 =ttk.Radiobutton(buttons,variable=my_int_var,value=1,text='One',command=display_value)#update lable when clicked
# r1.pack(anchor='w')
# r2 =ttk.Radiobutton(buttons,variable=my_int_var,value=2,text='Two',command=display_value)#update lable when clicked
# r2.pack(anchor='w')

# #create a label to display the selectedd value
# Value_label = ttk.Label(root,text='Selected Value:0')
# Value_label.pack(pady=10)

# root.mainloop()

# #Combobox
# import tkinter as tk
# from tkinter import ttk
 
# #function to display the selected value
# def display_value(event):
#     value_label.config(text=f'Selected:{my_string_var.get()}')

# #create main window
# root=tk.Tk()
# root.title('Combobox Example')

# #create a StringVar to store the selected value
# my_string_var=tk.StringVar()

# #create the conbobox 
# mycombo = ttk.Combobox(root,textvariable=my_string_var, values=['Apple','Orange','Grape' ])
# mycombo.pack(pady=10)

# #bind the event to update label when selection chages
# mycombo.bind('<<ComboboxSelected>>',display_value)

# #vreate a label to display the selected value
# value_label=ttk.Label(root,text='Selected:None')
# value_label.pack(pady=10)

# root.mainloop()

# #Text
# import tkinter as tk
# from tkinter import ttk

# #function to display text content
# def display_text():
#     text_content=mytext.get('1.0',tk.END).strip() #Get text from the widget
#     value_label.config(text=f'Entered Text:\n{text_content}') #create main window
# root=tk.Tk()
# root.title('Text Widget Example')
# #create the text widget
# mytext= tk.Text(
#     root,
# undo=True, # enable undo functionality
# maxundo = 100, #maximum number of undo action
# spacing1 = 10, #space before a paragraph
# spacing2 = 2, #spacce between lines
# spacing3 = 5, #space after a paragraph
# height = 5, #number of rows
# wrap = 'char' # wrap text at character level
#     )

# mytext.pack(pady=10)
# #create a button to ediaplay text content
# display_button= ttk.Button(root,text='Show Text', command=display_text)
# display_button.pack(pady=5)

#     #create a laabel to display the entered text
# value_label= ttk.Label(root,text='Entered Text:')
# value_label.pack(pady=10)
# root.mainloop()

# #Menu
# import tkinter as tk
# from tkinter import ttk
# #funcion to update teh label text
# def update_text(new_text):
#     main_text.set(new_text)

# #create main window
# root=tk.Tk()
# root.geometry('200x150')
# root.title('Menu example')

# #create a stringVar for the label text
# main_text = tk.StringVar(value='Hi')

# #create the label
# label = tk.Label(root, textvariable=main_text)
# label.pack(side='bottom',pady=10)

# #create the menu bar
# menubar= tk.Menu(root)

# #create a menu 
# file_menu= tk.Menu(menubar,tearoff=0)
# file_menu.add_command(label='Open', command=lambda:update_text('Open File'))
# file_menu.add_command(label='Save',command=lambda:update_text('Save File'))
# file_menu.add_separator()
# file_menu.add_command(label='Exit',command=root.quit)

# #add menu to the menu bar
# menubar.add_cascade(label='File',menu=file_menu)

# #display the menu
# root.config(menu=menubar)
# root.mainloop()

# Procedural approach: step-by-step execution
# def calculate_balance(balance, deposit, withdrawal):
#     balance += deposit
#     balance -= withdrawal
#     return balance
# # Function call
# initial_balance = 1000
# deposit_amount = 500
# withdrawal_amount = 200
# new_balance = calculate_balance(initial_balance, deposit_amount)
# print("Updated Balance:", new_balance)