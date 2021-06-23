# import os
#
#
# # import selenium
# # a =200
# # b =30
# # c=500
# # if a > b: print("a is greater than b")
# # print("A")if a > b else print("=") if a==b else print("B")
# # if a>b and c>a:
# #  # print("Both conditions are true")
# #  pass
# #
# # x =41
# # if x > 10:
# #     print("Above ten,")
# #     if x > 20:
# #      print("and also above 20!")
# #     else:
# #      print(
# #         "but not above 20.")
#
# # i =0
# # while i <6:
# #     i +=1
# #     if i ==3:
# #      continue
# #     print(i)
# #
# # fruits = ["apple","banana","cherry"]
# # for x in fruits:
# #     if x == 'banana':
# #         continue
# #     print(x)
# #
# # count=0
# # for x in "banana":
# #     if 'a' in x:
# #         count+=1
# # print(count)
# #
# # for x in range(6):
# #     if x==3:break
# #     print(x)
# # else:
# #     print("Finally finished")
#
# # adj = ["red","big","tasty"]
# # fruits = ["apple","banana","cherry"]
# # for x in adj:
# #     for y in fruits:
# #         print(x, y)
#
# # def my_function(fname, lname):
# #     print(fname+" "+lname)
# # my_function("Emil")
# #
# # def my_function(child3, child2, child1):
# #     print("The youngest child is "+ child3)
# # my_function(child1 ="Emil", child2 ="Tobias", child3 ="Linus")
# #
# # def my_function(**kid):
# #   print("His last name is " + kid["lname"])
# # my_function(fname = "Tobias", lname = "Refsnes")
#
# # def my_function(country ="Norway"):
# #     print("I am from "+country)
# # my_function()
# # my_function("India")
# # my_function()
# # my_function("Brazil")
#
# # def my_function(food):
# #     for x in food:
# #         print(x)
# # fruits = ["apple","banana","cherry"]
# # my_function(fruits)
#
# # def my_function(x=3):
# #     return 5 * x
# # print(my_function())
# # print(my_function(5))
# # print(my_function(9))
#
# # def factorial(x):
# #     """This is a recursive function
# #     to find the factorial of an integer"""
# #     if x ==1:
# #         return 1
# #     else :
# #         return (x * factorial(x-1))
# # num = 10
# # print("The factorial of", num, "is", factorial(num))
#
# # def recursor():
# #     recursor()
# # recursor()
#
#
# # def my_function():
# # 	"""Demonstrates triple double quotes
# # 	docstrings and does nothing really."""
# # 	return None
# # print("Using __doc__:")
# # print(my_function.__doc__)
# # print("Using help:")
# # help(my_function)
#
# # def my_function(arg1):
# #    """
# #   Summary line.
# #   Extended description of function.
# #   Parameters:
# #     arg1 (int): Description of arg1
# #     Returns:
# #     int: Description of return value
# #     """
# #    return arg1
# # print(my_function.__doc__)
#
#
# # class ComplexNumber:
# #     """
# #     This is a class for mathematical operations on complex numbers.
# #
# #     Attributes:
# #         real (int): The real part of complex number.
# #         imag (int): The imaginary part of complex number.
# #     """
# #
# #
# # def __init__(self, real, imag):
# #     """
# #     The constructor for ComplexNumber class.
# #
# #     Parameters:
# #        real (int): The real part of complex number.
# #        imag (int): The imaginary part of complex number.
# #     """
# #
# # def add(self, num):
# #     """
# #     The function to add two Complex Numbers.
# #
# #     Parameters:
# #         num (ComplexNumber): The complex number to be added.
# #
# #     Returns:
# #         ComplexNumber: A complex number which contains the sum.
# #     """
# #
# #     re = self.real + num.real
# #     im = self.imag + num.imag
# #
# #     return ComplexNumber(re, im)
# #
# #
# # help(ComplexNumber)  # to access Class docstring
# # help(ComplexNumber.add)  # to access method's docstring
#
# # f =open("demofile.txt","rt")
# # # print(f.read(5))
# # print(f.readline())
# # f.close()
#
# # f.write("Woops! I have deleted the content!")
# # f.close()
# #
# # f =open("myfile.txt","x")
#
# #
# # os.remove("demofile.txt")
#
#
# # f =open("demofile.txt","x")
# # if os.path.exists("demofile.txt"):
# #  os.remove("demofile.txt")
# # else:
# #  print("The file does not exist")
# #
# # os.rmdir("Folder")
#
# # f =open("demofile.txt","r")
# # # print(f.tell())
# # # f.write("Woops! I have deleted the content!")
# # print(f.readline())
# # print(f.tell())
# #
# # f =open("demofile.txt","r")
# # f.seek(4)
# # print(f.readline())
#
# # file = open('demofile.txt', 'w')
# # file.write('hello world !')
# # file.close()
#
# # file = open('demofile.txt', 'w')
# # try:
# #     file.write('hello world')
# # finally:
# #     print("Finally")
# #     file.close()
#
# # with open('demofile.txt', 'w') as file:
# #     file.write('hello world !')
#
# # class MessageWriter(object):
# #     def __init__(self, file_name):
# #         self.file_name = file_name
# #     def __enter__(self):
# #         self.file = open(self.file_name, 'w')
# #         return self.file
# #     def __exit__(self):
# #         self.file.close()
# #   # using with statement with MessageWriter
# # with MessageWriter('demofile2.txt') as xfile:
# #     xfile.write('hello world')
#
# # x = lambda a : a + 10
# # print(x(5))
# #
# # def myfunc(n):
# #     return lambda a : a * n
#
#
# # mydoubler = myfunc(2)
# # print(mydoubler(11))
#
# # val = 'BusyQA'
# # print(f"{val}for{val} is a portal for {val}.")
# #
# # name = 'Tushar'
# # age = 23
# # print(f"Hello, My name is {name} and I'm {age} years old.")
#
#
#
# # today = datetime.datetime.today()
# # print(f"{today:%B %d, %Y}")
#
# # answer = 456
# # print(f"Your answer is "{answer}"")
#
# # f"newline: {ord('\n')}”
# #
# # newline = ord('\n')
# # f"newline: {newline}"
#
# # txt ="For only {price:.2f} dollars!"
# # print(txt.format(price =49))
#
# # txt = "We have {:<8} chickens."
# # print(txt.format(49))
#
# # def myFun(*argv):
# #     for arg in argv:
# #         print (arg)
# # myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')
#
#
# # def myFun(arg1, *argv):
# # 	print ("First argument :", arg1)
# # 	for arg in argv:
# # 		print("Next argument through *argv :", arg)
# #
# # myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')
#
# #
# # def myFun(**kwargs):
# #     for key, value in kwargs.items():
# #         print("%s == %s" % (key, value)+ 23)
# #
# #
# # # Driver code
# # myFun(first='Geeks', mid='for', last='Geeks')
#
# # print("The values of variable is" + '23')
#
#
# # def myFun(*args,**kwargs):
# #     print("args: ", args)
# #     print("kwargs: ", kwargs)
# #  # Now we can use both *args ,**kwargs
# # # to pass arguments to this function :
# # myFun('geeks','for','geeks',first="Geeks",mid="for",last="Geeks")
#
#
# # l1 = ["eat","sleep","repeat"]
# # s1 = "geek"
# #
# # # creating enumerate objects
# # obj1 = enumerate(l1)
# # obj2 = enumerate(s1)
# #
# # print ("Return type:",type(obj1))
# # print (list(enumerate(l1)))
# #
# # # changing start index to 2 from 0
# # print (list(enumerate(s1,2)))
# #
# # l1 = ["eat","sleep","repeat"]
# #
# # # printing the tuples in object directly
# # for x in enumerate(l1):
# #  print (x)
#
#
# # print ("Always executed")
#
# # if __name__ == "__main__":
# #  print ("Executed when invoked directly")
# # else:
# #  print ("Executed when imported")
#
#
# # def my_function():
# #   print("I am inside function")
# # # We can test function by calling it.
# # # my_function()
# #
# # if __name__ == "__main__":
# #     my_function()
# # import datetime
# # print(datetime.datetime.today())
#
#
# # myTuple = ("John","Peter","Vicky")
# # x ="#".join(myTuple)
# # print(x)
#
# # myDict = {"name":"John","country":"Norway"}
# # mySeparator ="TEST"
# # x= mySeparator.join(myDict)
# # print(x)
#
# # circle_areas = [3.56773, 5.57668, 4.00914, 56.24241, 9.41344, 32.00013]
# # result = list(map(round, circle_areas,range(1,7)))
# # print(result)
#
# # circle_areas = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.00013]
# # result = list(map(round, circle_areas, range(1,5)))
# # print(result)
#
# # my_strings = ["a", "b", 'c', 'd', 'e’]
# # my_numbers = ['1',2,3,4,5]
# # results = list(zip(my_strings, my_numbers))
# # print(results)
#
# # my_strings = ["a","b","c","d","e"]
# # my_numbers = [1,2,3,4,5]
# # my_arrays=["abc",1,7,9.4,"apple"]
# # results = list(zip(my_strings, my_numbers,my_arrays))
# # print(results)
#
#
# #
# # scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
# # def is_A_student(score):    return score < 75
# # over_75 = list(filter(is_A_student, scores))
# # print(over_75)
#
# # dromes = ("demigod", "rewire", "madam", "freer", "anutforajaroftuna", "kiosk")
# #
# # palindromes = list(filter(lambda word: word == word[::-1], dromes))
# #
# # print(palindromes)
#
# #
# # def shout(text):
# #  return text.upper()
# # print(shout('Hello'))
# # yell = shout
# # print(yell('Hello'))
# #
# #
# # def shout(text):
# #   return text.upper()
# #
# #
# # def whisper(text):
# #   return text.lower()
# #
# #
# #
# # def greet(func):
# #   print(func)
# #   # storing the function in a variable
# #   greeting = func("""Hi, I am created by a function passed as an argument.""")
# #   print(greeting)
# #
# # greet(shout)
# # greet(whisper)
#
#
# # def create_adder(x):
# #   def adder(y):
# #     return x + y
# #
# #   return adder
# #   return x
# # add_15 = create_adder(15)
# # print(add_15)
#
#
# @gfg_decorator
# def hello():
#   print("Hello")
# hello()
#
#
# def hello_decorator(func):
#   # inner1 is a Wrapper function in
#   # which the argument is called
#   # inner function can access the outer local
#   # functions like in this case "func"
#   def inner1():
#     print("Hello, this is before function execution")
#     # calling the actual function now
#     # inside the wrapper function.
#     func()
#
#   print("This is after function execution")
#
#
#   return inner1
#
#
# def function_to_be_used():
#
#   print("This is inside the function !!")
#
# # passing 'function_to_be_used' inside the
# # decorator to control its behavior
# function_to_be_used = hello_decorator(function_to_be_used)
#
# # calling the function
# function_to_be_used()
#
#
#
#
#
#
#
#
#
# def f1():
#   print("Calledf1")
# print(f1)


# def f1():
#   print("Called f1")
#
# def f2(f):
#   f()
#
# f2(f1)

#
def f1(func):
  def wrapper(*args,**kwargs):
    print("Started")
    val=func(*args,**kwargs)
    print("Ended")
    return val
  return wrapper

@f1
def f(a,b=9):
  print(a,b)
# f1(f)()
# f = f1(f)
# f("Hi!")

@f1
def add(x,y):
  return x+y
print(add(4,5))


# def works_for_all(func):
#   def inner(*args, **kwargs):
#     print("I can decorate any function")
#     return func(*args, **kwargs)
#
#   return inner
#
# @works_for_all
# def f():
#  print(9,10)
# f()

# try:
#   print(x)
# except NameError:
#   print("Variable x is not defined")
# except:
#   print("Something else went wrong")


# try:
#   print("Hello")
# except:
#   print("Something went wrong")
# finally:
#   print("Nothing went wrong")

# try:
#   f = open("demofile.txt",'w')
#   f.write("Lorum Ipsum")
# except:
#   print("Something went wrong when writing to the file")
# finally:
#   f.close()

# x = -1
# if x < 0:
#   raise TypeError("Sorry, no numbers below zero")







