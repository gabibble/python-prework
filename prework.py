# Question 1
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below. def hello_name(user_name):

def hello_name(user_name):
    """Greets user"""
    print(f"Hello {user_name}!")

# Question 2
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing def first_odds():


def first_odds():
    """Prints all the odd numbers up to 100"""
    list = []
    x = 0
    while x < 100:
        x += 1
        if x % 2 == 0:
            continue
        else:
            list.append(x)
    for number in list:
        print(number, end=" ")


# Question 3
# Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below. def max_num_in_list(a_list):

def max_num_in_list(a_list):
    """Returns the max number in a list"""
    return max(a_list)


# Question 4
# Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100 unless it is also divisible by 400. The return should be boolean Type (true/false). def is_leap_year(a_year):

def is_leap_year(a_year):
    """Will tell you if a year is a leap year"""
    if a_year % 400 == 0:
        return True
    elif a_year % 100 == 0:
        return False
    elif a_year % 4 == 0:
        return True
    else: 
        return False


# QUESTION 5
# Write a function to check to see if all numbers in the list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type. def is_consecutive(a_list):

def is_consecutive(a_list):
    """checks if numbers in a list are consecutive"""
    while len(a_list[:]) >= 2:
        if a_list.pop() == a_list[-1] + 1:
            continue
        else: 
            return False
    return True


