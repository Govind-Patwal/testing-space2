'''
Course 3 - Week 3
Functions
'''

# # a very simple function w/o parameters and w/o return value
# def hello():
#     '''
#     This funtion has no paramaters and no return value. 
#     Upon invocation, it prints 'Hello World'
#     >>> hello()
#     Hello World
#     '''
#     print('Hello World')
# hello()         # invoking the function  
# help(hello)     # displaying the docstring of a function



# # funtion to draw a sqare using turtle
# def draw_square(turtle_name, side1):
#     '''
#     This function draws a sqaure, it takes 2 arguments - name of turtle and 
#     length of a side of a square, and gets the turtle to draw it
#     >>> draw_square(50)
#     '''
#     for i in range(4):
#         turtle_name.forward(side1)
#         turtle_name.left(90)
# import turtle
# window = turtle.Screen()
# window.bgcolor('green')
# alex = turtle.Turtle()
# draw_square(alex, 50)
# window.exitonclick()

# # name of the parameters at the time of naming the functions are called the 
# # formal parameters or param names
# # name of the parameters at the time of invoking the funcion are called 
# # Actual parameters or arguments or param values
# # formal paramaters are not available outside of the function

# # the default return of a function is None, always a good idea to use 
# # return rather than print, return assigns the output of the function to a 
# # variable, but does NOT print it.

# # a return statement terminates the execution of a function, and goes outside the current function


# list1 = ['alex', 'marin', 'jess', 'simon', 'josph', 'modi', 'jutin', 'seven']
# list2 = ['alexendar', 'martin', 'jessica', 'simon', 'joseph', 'modi', 'justin', 'steven']

# def name_longer_than_5_chars_in_a_list (name_list):
#     for name in name_list:
#         if len(name) > 5:
#             return 'This list has a name that is longer than 5 chars'
#     return 'This list does not have a name longer than 5 chars'        

# i = name_longer_than_5_chars_in_a_list(list1)
# j = name_longer_than_5_chars_in_a_list(list2     )

# print(i)
# print(j)


# # while loop - 4 important parts (1) initiator (2) condition (3) code (4) incrementer

# # initiator
# num = 0
# even_nums = []

# # condiiton
# while num <= 15:
#     if num%2 ==0:
#         even_nums.append(num)
#     num += 1

# print(even_nums)

# even_nums = []
# for i in range(15):
#         if i%2 ==0:
#             even_nums.append(i)
# print(even_nums)

print('dummy_value' != 0)



    


