#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().set_next_input('1.What are the two values of the Boolean data type? How do you write them');get_ipython().run_line_magic('pinfo', 'them')

The two boolean values are True and False.
we can assign the boolean value to a variable like s=True 

get_ipython().set_next_input('2. What are the three different types of Boolean operators');get_ipython().run_line_magic('pinfo', 'operators')
 
    Three different boolean operators are and, or and not.
    
3. Make a list of each Boolean operator's truth tables 
(i.e. every possible combination of Boolean values for the operator and what it evaluate ).
    value1  value2  Operator Result
      True   True    and   True
      True  False  and     False
      False  True   and    False
      False  False  and    False
      True   True   or   True
      True  False  or     True
      False  True   or    True
      False  False  or   False
      True         not   False
      False        not    True
      
get_ipython().set_next_input('4. What are the values of the following expressions');get_ipython().run_line_magic('pinfo', 'expressions')
(5 > 4) and (3 == 5)   --- False

not (5 > 4)            --- False
(5 > 4) or (3 == 5)    --- True
not ((5 > 4) or (3 == 5)) ---False
(True and True) and (True == False) --False
(not False) or (not True)  --True

get_ipython().set_next_input('5. What are the six comparison operators');get_ipython().run_line_magic('pinfo', 'operators')
  The six comparison operators in Python are less than ( < ), less than or equal to ( <= ), greater than ( > ),
    greater than or equal to ( >= ), equal to ( == ), and not equal to ( != ).

get_ipython().set_next_input('6. How do you tell the difference between the equal to and assignment operators');get_ipython().run_line_magic('pinfo', 'operators')
   Describe a condition and when you would use one.
The '=' is an assignment operator is used to assign the value on the right to the variable on the left.
The '==' operator checks whether the two given operands are equal or not. If so, it returns true. Otherwise it returns false

a=10  
b=6
if(a==b):
    print("The given values a and b are queal")
else:
    print("The values are not equal") 
    
    
7. Identify the three blocks in this code:
spam = 0
if spam == 10:
print('eggs')
if spam > 5:
print('bacon')
else:
print('ham')
print('spam')
print('spam')


Ans:
    
    spam = 0
if spam == 10:
    print('eggs')  ##Corrected indentation
if spam > 5:
    print('bacon')  ##Corrected indentation
else:
    print('ham')    ##Corrected indentation
print('spam')
print('spam')
8. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! 
   if anything else is stored in spam.
   
spam=int(input("Enter Any Number"))
if spam==1:
    print("Hello")
elif spam==2:
    print("Howdy")
else:    
    print("Greetings!")

get_ipython().set_next_input('9.If your programme is stuck in an endless loop, what keys you’ll press');get_ipython().run_line_magic('pinfo', 'press')
  You can stop an infinite loop with CTRL + C

get_ipython().set_next_input('10. How can you tell the difference between break and continue');get_ipython().run_line_magic('pinfo', 'continue')
   The break is used to terminate the execution of the statements and iteration of the loop. 
    It will move to the next statement after the loop and continue for different purposes. 
    The break statement will allow control to move out of loop skipping the execution of the remaining statements of loop     
    and continue will allow the control to remain inside the loop by moving 1 iteration ahead. The important things that need
    to keep regarding use of continue and break used with the loops. The break statement will cause the jump statements 
    and break statement to cause the termination or exit the loop for early of the loop.
    The break statement is nested loop and allows the innermost loop and the control will remain inside outermost loop 
    inside the nested loop will allow skip of current location and execution of next iteration of innermost loop.
11. In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?
    The output is same for all the three cases ie it will print the numbers from 0 to 9.
    
12. Write a short program that prints the numbers 1 to 10 using a for loop. 
    Then write an equivalent program that prints the numbers 1 to 10 using a while loop.
    #print 1 to 10 using For Loop
    for i in range(1,11,1):
    print(i)
    #print 1 to 10 using for loop
    i=1
while i <=10:
    print(i)
    i=i+1
get_ipython().set_next_input('13. If you had a function named bacon() inside a module named spam, how would you call it after importing spam');get_ipython().run_line_magic('pinfo', 'spam')
     import sparm as s
      s.bacon()

