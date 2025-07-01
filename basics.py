print("Mohit is very good boy") #to print any msg in python we use this

if 5<8:
    print("5 is greater than 8") #if condition is true then this will be printed

number_1=23,number_2=45 #we can assign multiple values to multiple variables in one line
print(number_1) #to print the value of variable we use print function
print(number_2) #to print the value of variable we use print function
# we can also assign multiple values to multiple variables in one line
number_1, number_2 = 23, 45
print(number_1) #to print the value of variable we use print function
print(number_2) #to print the value of variable we use print function
# we can also assign multiple values to multiple variables in one line
number_1 = 23
number_2 = 45
print(number_1) #to print the value of variable we use print function
print(number_2) #to print the value of variable we use print function
print(number_1+number_2) #to print the sum of two variables we use print function

x = 5
y = "John"
print(type(x))
print(type(y))

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

myVariableName = "John" # Camel case variable name
my_variable_name = "John" # Snake case variable name
MyVariableName2 = "John" # Pascal case variable name

# Unpacking a collection into variables
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z) 

# Concatenating strings
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

x = 5
y = "John"
print(x + y) # This will raise an error because you cannot concatenate a string and an integer

# Using a global variable in a function
x = "awesome"
def myfunc():
  print("Python is " + x)
myfunc()

# Using a global variable in a function with local variable
x = "awesome"
def myfunc():
  x = "fantastic"
  print("Python is " + x)
myfunc()
print("Python is " + x)

# Using a global variable in a function with global declaration
def myfunc():
  global x # This will allow us to modify the global variable x
  x = "fantastic"
myfunc()
print("Python is " + x)

# Using a global variable in a function with global declaration and modifying it
x = "awesome"
def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)

x = 5
print(type(x))

# Assigning different data types to a variable
x = "Hello World"		# String
x = 20		# Integer
x = 20.5		# Float
x = 1j		# Complex number
x = ["apple", "banana", "cherry"]	# List	
x = ("apple", "banana", "cherry")		# Tuple
x = range(6)		# Range object
x = {"name" : "John", "age" : 36}	# Dictionary	
x = {"apple", "banana", "cherry"}		# Set
x = frozenset({"apple", "banana", "cherry"})	# Frozenset	
x = True		# Boolean
x = b"Hello"	# Bytes
x = bytearray(5)		# Bytearray
x = memoryview(bytes(5))		# Memoryview
x = None#        # NoneType

# Assigning different data types to a variable with type casting
x = str("Hello World")	
x = int(20)		
x = float(20.5)		
x = complex(1j)		
x = list(("apple", "banana", "cherry"))		
x = tuple(("apple", "banana", "cherry"))		
x = range(6)	
x = dict(name="John", age=36)		
x = set(("apple", "banana", "cherry"))		
x = frozenset(("apple", "banana", "cherry"))		
x = bool(5)		
x = bytes(5)		
x = bytearray(5)		
x = memoryview(bytes(5))
#Setting the Specific Data Type

x = 1    # int
y = 2.8  # float
z = 1j   # complex
# Printing the types of variables
print(type(x))
print(type(y))
print(type(z))

x = 1
y = 35656222554887711
z = -3255522
print(type(x))
print(type(y))
print(type(z))

x = 1.10
y = 1.0
z = -35.59
print(type(x))
print(type(y))
print(type(z))

x = 3+5j
y = 5j
z = -5j
print(type(x))
print(type(y))
print(type(z))

x = 1    # int
y = 2.8  # float
z = 1j   # complex
#convert from int to float:
a = float(x)
#convert from float to int:
b = int(y)
#convert from int to complex:
c = complex(x)
print(a)
print(b)
print(c)
print(type(a))
print(type(b))
print(type(c))

# Importing the random module to generate random numbers
import random
print(random.randrange(1, 10))

print("Hello") 
print('Hello') 

print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

a = "Hello"
print(a)

# Using triple quotes for multi-line strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# Using triple single quotes for multi-line strings
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

# Accessing characters in a string using indexing
a = "Hello, World!"
print(a[1])

#looping through a string using a for loop
for x in "banana":
  print(x)
  
# Checking the length of a string using the len() function
a = "Hello, World!"
print(len(a))

# Checking if a substring exists in a string using the in keyword
txt = "The best things in life are free!"
print("free" in txt)

# Checking if a substring exists in a string using the in keyword with an if statement
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
  
# Checking if a substring does not exist in a string using the not in keyword
txt = "The best things in life are free!"
print("expensive" not in txt)

# Checking if a substring does not exist in a string using the not in keyword with an if statement
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")
  
# Slicing a string to get a substring
b = "Hello, World!"
print(b[2:5])

# Slicing a string to get a substring with a step
b = "Hello, World!"
print(b[:5])

# Slicing a string to get a substring from a specific index to the end
b = "Hello, World!"
print(b[2:])

# negative slicing to get a substring from the end
b = "Hello, World!"
print(b[-5:-2])

# converting a string to uppercase using the upper() method
a = "Hello, World!"
print(a.upper())

# converting a string to lowercase using the lower() method
a = "Hello, World!"
print(a.lower())

# removing whitespace from the beginning and end of a string using the strip() method
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

# replacing a substring in a string using the replace() method
a = "Hello, World!"
print(a.replace("H", "J"))

# splitting a string into a list using the split() method
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

# concatenating two strings using the + operator
a = "Hello"
b = "World"
c = a + b
print(c)

# concatenating two strings with a space in between
a = "Hello"
b = "World"
c = a + " " + b
print(c)

# concatenating a string with an integer (this will raise an error)
age = 36
txt = "My name is John, I am " + age
print(txt)

# concatenating a string with an integer using f-strings (formatted string literals)
age = 36
txt = f"My name is John, I am {age}"
print(txt)

# concatenating a string with an integer using the format() method
price = 59
txt = f"The price is {price} dollars"
print(txt)

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

txt = f"The price is {20 * 59} dollars"
print(txt)

#You will get an error if you use double quotes inside a string that is surrounded by double quotes:
txt = "We are the so-called "#Vikings" from the north."

txt = "We are the so-called \"Vikings\" from the north."

""" Method	Description
capitalize()	Converts the first character to upper case
casefold()	Converts string into lower case
center()	Returns a centered string
count()	Returns the number of times a specified value occurs in a string
encode()	Returns an encoded version of the string
endswith()	Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	Searches the string for a specified value and returns the position of where it was found
format()	Formats specified values in a string
format_map()	Formats specified values in a string
index()	Searches the string for a specified value and returns the position of where it was found
isalnum()	Returns True if all characters in the string are alphanumeric
isalpha()	Returns True if all characters in the string are in the alphabet
isascii()	Returns True if all characters in the string are ascii characters
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	Returns True if all characters in the string are lower case
isnumeric()	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	Returns True if all characters in the string are whitespaces
istitle()	Returns True if the string follows the rules of a title
isupper()	Returns True if all characters in the string are upper case
join()	Joins the elements of an iterable to the end of the string
ljust()	Returns a left justified version of the string
lower()	Converts a string into lower case
lstrip()	Returns a left trim version of the string
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
replace()	Returns a string where a specified value is replaced with a specified value
rfind()	Searches the string for a specified value and returns the last position of where it was found
rindex()	Searches the string for a specified value and returns the last position of where it was found
rjust()	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	Splits the string at the specified separator, and returns a list
rstrip()	Returns a right trim version of the string
split()	Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	Returns a trimmed version of the string
swapcase()	Swaps cases, lower case becomes upper case and vice versa
title()	Converts the first character of each word to upper case
translate()	Returns a translated string
upper()	Converts a string into upper case
zfill()	Fills the string with a specified number of 0 values at the beginning
    """
    
print(10 > 9)
print(10 == 9)
print(10 < 9)

a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
  
print(bool("Hello"))
print(bool(15))

x = "Hello"
y = 16
print(bool(x))
print(bool(y))

# Check the truth value of different data types
bool("abc")# non-empty string is True
bool(123)# non-zero integer is True
bool(["apple", "cherry", "banana"])# non-empty list is True
bool([])# empty list is False

# false values in Python
# The following values are considered false in Python: 
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

class myclass():
  def __len__(self):
    return 0
myobj = myclass()
print(bool(myobj))

def myFunction() :
  return True
print(myFunction())

def myFunction() :
  return True
if myFunction():
  print("YES!")
else:
  print("NO!")

x = 200
print(isinstance(x, int))

print(10 + 5)
"""
+	Addition	    x + y	
-	Subtraction    	x - y	
*	Multiplication	x * y	
/	Division	    x / y	
%	Modulus	        x % y	
**	Exponentiation	x ** y	
//	Floor division	x // y

=	x = 5	x = 5	
+=	x += 3	x = x + 3	
-=	x -= 3	x = x - 3	
*=	x *= 3	x = x * 3	
/=	x /= 3	x = x / 3	
%=	x %= 3	x = x % 3	
//=	x //= 3	x = x // 3	
**=	x **= 3	x = x ** 3	
&=	x &= 3	x = x & 3	
|=	x |= 3	x = x | 3	
^=	x ^= 3	x = x ^ 3	
>>=	x >>= 3	x = x >> 3	
<<=	x <<= 3	x = x << 3	
:=	print(x := 3)	x = 3,print(x)

Operator	Name	
==	Equal	    x == y	
!=	Not equal	x != y	
>	Greater than	x > y	
<	Less than	    x < y	
>=	Greater than or equal to	x >= y	
<=	Less than or equal to	    x <= y

and 	Returns True if both statements are true	x < 5 and  x < 10	
or	Returns True if one of the statements is true	x < 5 or x < 4	
not	Reverse the result, returns False if the result is true	not(x < 5 and x < 10)

is 	Returns True if both variables are the same object	x is y	
is not	Returns True if both variables are not the same object	x is not y

in 	Returns True if a sequence with the specified value is present in the object	x in y	
not in	Returns True if a sequence with the specified value is not present in the object	x not in y

& 	AND	Sets each bit to 1 if both bits are 1	x & y	
|	OR	Sets each bit to 1 if one of two bits is 1	x | y	
^	XOR	Sets each bit to 1 if only one of two bits is 1	x ^ y	
~	NOT	Inverts all the bits	~x	
<<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off	x << 2	
>>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off	x >> 2

print((6 + 3) - (6 + 3))
print(100 + 5 * 3)

The precedence order is described in the table below, starting with the highest precedence at the top:
Operator	Description	
()	Parentheses	
**	Exponentiation	
+x  -x  ~x	Unary plus, unary minus, and bitwise NOT	
*  /  //  %	Multiplication, division, floor division, and modulus	
+  -	Addition and subtraction	
<<  >>	Bitwise left and right shifts	
&	Bitwise AND	
^	Bitwise XOR	
|	Bitwise OR	
==  !=  >  >=  <  <=  is  is not  in  not in 	Comparisons, identity, and membership operators	
not	Logical NOT	
and	AND	
or	OR
"""
print(5 + 4 - 7 + 3)

#STARTING OF LISTS
thislist = ["apple", "banana", "cherry"]
print(thislist)

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
print(len(thislist))

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

list1 = ["abc", 34, True, 40, "male"]

mylist = ["apple", "banana", "cherry"]
print(type(mylist))

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)
"""
Python Collections (Arrays)
There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members """

thislist = ["apple", "banana", "cherry"]
print(thislist[1])

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

#newlist = [expression for item in iterable if condition == True]
newlist = [x for x in fruits if x != "apple"]
#alternative for the above one
newlist = [x for x in fruits]

newlist = [x for x in range(10)]

newlist = [x for x in range(10) if x < 5]

"""
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits]
print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = ['hello' for x in fruits]
print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)
"""
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

def myfunc(n):
  return abs(n - 50)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)
print(list1)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)

"""
List Methods
Python has a set of built-in methods that you can use on lists.

Method	Description
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list
"""
#ENDING OF THE LSITS
#STARTING OF TUPLES















