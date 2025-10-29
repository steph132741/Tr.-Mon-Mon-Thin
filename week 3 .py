# x=-22
# y=-22
# print(id(x))
# print(id(y))
# print(x is y)

# print(1*2+3*5%4)
# print(1+8%3*2-9)
# print(7+6*5)

# exercise 2
# ping_value = int(input('enter a ping value:'))
# if ping_value >= 150:
#     print('too high')
# else:
#     print('low to everage')

#exercise 3
# age = int(input('Learner age:'))
# if age ==18:
#     lesson=20
#     print('Number of lesson:',lesson)
# else:
#     lesson = 20+(age - 18)*2
#     print('number of lesson:',lesson)

#Exercise 4 h.w
# book_sold = int(input('enter number of book sold:'))
# profit = int(input('Enter amount of profit made:'))
# if book_sold >= 5 and profit >= 10:
#     print('Sales and profit are good this week')
# elif book_sold > 20 and profit >=20: 
#     print('Sales and profit are excellent this week')
# elif book_sold <5 or profit < 5:
#     print('poor performance this week')
# else:
#     print('Alert manager')


#exercise 5 
# year = int(input('enter a year:'))
# if year % 400== 0:
#     print('Leap Year')
# elif year % 4 == 0 and year % 100 !=0:
#     print('Leap Year')
# else:
#     print('not leap year')

#exercise 6 h.w
# stored_letter = 'S'
# user_letter = input('Enter a letter:')
# if user_letter < stored_letter:
#     print('Your letter comes before the stored letter.')
# elif user_letter > stored_letter:
#     print('Your letter comes after the stored letter.')
# else:
#     print('Your letter is the same as the stored letter.')

#exercise 7 h.w
# quantity = int(input('Enter number of textbooks:'))
# if quantity >= 1 and quantity<= 5:
#     price=20
# elif quantity >= 6 and quantity <= 9:
#     price=15
# elif quantity >= 10:
#     price= 12
# else:
#     price = 0

# total = price*quantity
# print('price per textbook: ', price)
# print('Total cost: ', total)

#exercise 8 h.w
# import math
# side = float(input('Enter square side length: '))
# radius = float(input('Enter circle radius: '))
# square_area = side*side
# circle_area = math.pi * radius * radius
# excess_area = square_area - circle_area
# print('Excess area:', excess_area)

#exercise 9
# option = input('Enter a menu option lunch or dinner')
# if option == 'lunch':
#     choice = int(input('Enter a menu choices 1,2,3'))
#     if choice == 1:
#         print('Your order is caesar salad')
#     elif choice == 2:
#         print(' Your order is spicy chicken wrap')
#     elif choice == 3:
#         print('Your order is Butternut squash soup')
#     else:
#         print('wrong order')

# elif option == 'dinner':
#     choice = int(input('enter a menu choices 1,2,3'))
#     if choice ==1:
#         print('Baked salmon')
#     elif choice ==2:
#         print('Turkey burger')
#     elif choice ==3:
#         print('Mushroom risotto')
#     else:
#         priint('Wrong dinner')
# else:
#     print('your input error')

#loop
# total = 0
# for index in range (1,10):
#     total = total + index
# print( total )

# exercise 1
# start_no = int(input('Enter the start number:'))
# end_no = int(input('Enter the end number: '))
# total=0
# for number in range(start_no,end_no +1):
#    total= total + number
#    if number < end_no:
#       print(number,end='+')
#    else:
#       print(number,end= '=')
# print(total)

#nested loop structure
# for i in range(1,6):
#     for j in range (1,4):
#         print ('@', end='')
#     print('$')
# print ('all finished')

# #exercise 1

for i in range (1,13):
    for j in range(2,13):
        print(f'{i}x {j}= {i*j}')
    print()

#exercise 2
Pattern (a)
for i in range(1,11):
    for j in range (i):
        print('*',end='')
    print()

Pattern (b)
num_rows_b = 10
for i in range(num_rows_b, 0, -1):
    for j in range(i):
        print("*", end="")
    print() 

Pattern (c)
num_rows_c = 10
for i in range(num_rows_c, 0, -1):
    for j in range(num_rows_c - i):
        print(" ", end="")
    for k in range(i):
        print("*", end="")
    print()

Pattern (d)
num_rows_d = 10
for i in range(1, num_rows_d + 1):
    for j in range(num_rows_d - i):
        print(" ", end="")
    for k in range(i):
        print("*", end="")
    print()



