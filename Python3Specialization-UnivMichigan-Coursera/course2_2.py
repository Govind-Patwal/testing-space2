'''
https://www.coursera.org/learn/python-functions-files-dictionaries?specialization=python-3-programming
This course introduces the dictionary data structure and user-defined functions. You’ll learn about local and global variables, optional and keyword parameter-passing, named functions and lambda expressions. You’ll also learn about Python’s sorted function and how to control the order in which it sorts by passing in another function as an input. For your final project, you’ll read in simulated social media data from a file, compute sentiment scores, and write out .csv files. It covers chapters 10-16 of the textbook “Fundamentals of Python Programming,” which is the accompanying text (optional and free) for this course.
The course is well-suited for you if you have already taken the "Python Basics" course and want to gain further fundamental knowledge of the Python language. Together, both courses are geared towards newcomers to Python programming, those who need a refresher on Python basics, or those who may have had some exposure to Python programming but want a more in-depth exposition and vocabulary for describing and reasoning about programs.
This is a follow-up to the "Python Basics" course (course 1 of the Python 3 Programming Specialization), and it is the second of five courses in the specialization.
'''
# DICTIONARIES

# eng_to_hindi = {}
# eng_to_hindi[1] = 1
# eng_to_hindi['one'] = 'ek'
# eng_to_hindi[2.2] = 2.2
# eng_to_hindi['two'] = 'do'
# eng_to_hindi[(23,23,34)] = (23,23,34)

# for key in eng_to_hindi:
#     print('The key {} corresponds to the value {}.'.format(key,eng_to_hindi[key]))

# # print(eng_to_hindi['thisis a book'])


# new_dict = eng_to_hindi.copy()
# print(eng_to_hindi)

string1 = 'the quick brown fox jumped over the lazy dog'
print('Original String is: {}'.format(string1))
list1 = string1.split()
print('String convered to list using .split() : {}'.format(list1))
list2=list(string1)
print('String convered to list using list(string) is : {}'.format(list2))
list3=string1.tolist()
print('String convered to list using string.tolist()) is : {}'.format(list3))



