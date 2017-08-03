name = 'Ali'
last_name = "Coder"
#--------------------------------
print "My name is {} {}".format(name, last_name)
hw = "hello %s" % 'world'
print hw
# the output would be:
# hello world
#------------------------------------
# print "my name is",5
# print "my name is"+5
# --------------------------
x = "Hello World"
print x.upper()
# output:
"HELLO WORLD"
#returns number of occurrences of substring in string.
print x.count('o')
# returns a boolean based upon whether the last characters of string match substring. not case sensitive
print x.endswith('d')
#: returns the index of the start of the first occurrence of substring within string. case sensitive
print x.find('H')
#(is alphanumeric) returns boolean depending on whether the string's length is > 0 and all characters are alphanumeric (letters and numbers only). 
# Strings that include spaces and punctuation will return False for this method. Similar methods include 
# .isalpha(), .isdigit(), .islower(), .isupper(), and so on. All return booleans. 
print x.isalnum()
#returns a list of values where string is split at the given character. Without a parameter the default split is at every space.
arr = x.split() 
# : returns a string that is all strings within our set (in this case a list) concatenated.
print arr
print x.join(" ")
#-------------------------------------------------------------------------------------------------
fruits = ['apples', 'bananas', 'oranges','peaches']
veg = ['cucumber', 'tomato', 'lettuce', 'carrots']
frt_veg = fruits + veg
print frt_veg   #['apples', 'bananas', 'oranges', 'peaches', 'cucumber', 'tomato', 'lettuce', 'carrots']
salad = 3* veg
print salad  # ['cucumber', 'tomato', 'lettuce', 'carrots', 'cucumber', 'tomato', 'lettuce', 'carrots', 'cucumber', 'tomato', 'lettuce', 'carrots']
# ------------------------------------------------------------------------------------
drawer = ['documents', 'envelopes', 'pens']
#access the drawer with index of 0 and print value
print drawer[0]  #prints documents
#access the drawer with index of 1 and print value
print drawer[1] #prints envelopes
#access the drawer with index of 2 and print value
print drawer[2] #prints pens

# ------------------------------------------------------------------------------------
x = [1,2,3,4,5]
x.append(99)
print x
#the output would be [1,2,3,4,5,99]
# ===============================================================================
x = [99,4,2,5,-3];
print x[:]
#the output would be [99,4,2,5,-3]
print x[1:]
#the output would be [4,2,5,-3];
print x[:4]
#the output would be [99,4,2,5]
print x[2:4]
#the output would be [2,5];
# ===============================================================================
# len(sequence) returns number of items in a sequence , Think of a sequence as anything over which we can iterate. 
my_list = [1, 'Zen', 'hi']
print len(my_list)
# output : 3
# ============================
my_list = ['apple', 'banana', 'grapes', 'pear']
for c, value in enumerate(my_list, 1):
    print(c, value)
#  ===============================

# list.extend(list2) #adds all values from a second sequence to the end of the original sequence.
# list.pop(index) #remove a value at given position. if no parameter is passed, defaults to final value in the list.
# list.index(value) #returns the index position in a list for the given parameter.

# ===================================================
# if statement:
# if <condition>:
  # do something
# if-else statement:
# elif <condition>:
  # do something
# else:
  # do this instead
# +++++++++===================================
# <>	Checks if the value of two operands are equal or not, 
# if values are not equal then condition becomes true.	(1 <> 2) is true. This is similar to != operator.*
# not 
# Reverses the true-false value of the operand	not(true) is false. 
# not(false) is true. 
# not(1 >= 2) is true. 
# not(1 =< 2) is false. 
# not(1 <= 2 and 2 =< 3) is false. 
# not(1 >= 2 or 2 >= 3) is true. 

# =======================================================================
for count in range (0,5):
    print "looping -", count

my_list = [4, 'dog', 99, ['list', 'inside', 55]]
for alir in my_list:
    print alir
    # =================================

# break statement
# Terminates the loop statement and transfers execution to the statement immediately following the loop.

# continue statement
# Causes the loop to skip the remainder of its body and immediately retest its condition prior to reiterating.

# pass statement (does nothin = null = )
# The pass statement in Python is used when a statement is required syntactically but you do not want any command or code to execute.

for letter in 'Python': 
   if letter == 'h':
      pass
   print 'Current Letter :', letter
print "Good bye!"
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++
x ='1'
y=2
print x+str(y)





