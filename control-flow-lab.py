 # python3 control-flow-lab.py

# exercise-01 Vowel or Consonant

# Write the code that:
# 1. Prompts the user to enter a letter in the alphabet:
#      Please enter a letter from the alphabet (a-z or A-Z): 
# 2. Write the code that determines whether the letter entered is a vowel
# 3. Print one of following messages (substituting the letter for x):
#      - The letter x is a vowel
#      - The letter x is a consonant

# Hints:  Use the in operator to check if a character is in another string
#         For example, if some_char in 'abc':


consonants=['b','c','d','f','g','h',
'j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']

vowel =['a','e', 'i', 'o','u']
#print(dir(consonant))


char_input= input("Enter a letter: ").lower()

if char_input in consonants:
    print(f"The letter {char_input} is a consonant")
elif char_input in vowel:
    print(f"The letter {char_input} is a vowel")




# exercise-02 Length of Phrase

# Write the code that:
# 1. Prompts the user to enter a phrase:
#      Please enter a word or phrase: 
# 2. Print the following message:
#      - What you entered is xx characters long
# 3. Return to step 1, unless the word 'quit' was entered.

phrase=""
while phrase !="quit":
    phrase= input("Please enter a phrase: ")
    print(f"What you entered is {len(phrase)} characters long ")





# exercise-03 Calculate Dog Years

# Write the code that:
# 1. Prompts the user to enter a dog's age like this:
#      Input a dog's age: 
# 2. Calculates the equivalent dog years, where:
#      - The first two years count as 10 years each
#      - Any remaining years count as 7 years each
# 3. Prints the answer in the following format:
#      The dog's age in dog years is xx

# Hints:
# Use the int() function to convert the string returned from input() into an integer
# Start with an if that checks if the age is less than 3

print('  Enter the age of dog')
a=input("age: ")
dogage=int(a)
age=0 #output

if dogage <= 2:
    age=10*dogage
elif dogage>2:
    age=10*2
    dogage=dogage-2
    print(f'dogage after sub 2 = {dogage}')
    age+=7*dogage


print( f" The dog's age in dog years is {age}")





# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a: 
#      b:
#      c:
# 2. Write the code that determines if the triangle is:
#      equilateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - exactly two sides are the same length
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle


print('  Enter the lengths of three side of a triangle:')
a=input("a: ")
b=input("b: ")
c=input("c: ")

if a==b and b==c:
    print(f" A triangle with sides of a:{a}, b:{b} & c:{c} is a equilateral triangle")
elif a!=b and b!=c and c!=a:
      print(f" A triangle with sides of a:{a}, b:{b} & c:{c} is a scalene triangle")
elif a==b or b==c or c==a:
      print(f" A triangle with sides of a:{a}, b:{b} & c:{c} is a isosceles triangle")






# exercise-05 Fibonacci sequence for first 50 terms

# Write the code that:
# 1. Calculates and prints the first 50 terms of the fibonacci sequence.
# 2. Print each term and number as follows:
#      term: 0 / number: 0
#      term: 1 / number: 1
#      term: 2 / number: 1
#      term: 3 / number: 2
#      term: 4 / number: 3
#      term: 5 / number: 5
#      etc.

# Hints:
# The next number is found by adding the two numbers before it
# Use a while loop with a looping variable, or look into Python ranges, e.g.:
#   for n in range(50):

first_num = 0 
sec_num =1
count = 0

while count < 50:
    print(f"{count}:  {first_num}")
    next_in_sequence = first_num + sec_num
  
    first_num = sec_num
    sec_num = next_in_sequence
    count += 1


# exercise-06 What's the Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the year (Jan - Dec):
# 2. Then prompts the user to enter the day of the month: 
#      Enter the day of the month:
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season> 

# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
#   if input_month in ('Jan', 'Feb', 'Mar'):
#
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.

winter=['Dec', 'Jan', 'Feb', 'Mar']
spring=['Mar','Apr','May', 'Jun']
summer=['Jun','Jul','Aug','Sep']
fall=['Sep','Oct','Nov','Dec']

Season=''

input_month=input(' Enter the month of the year (Jan - Dec): ')
input_day=int(input('Enter the day: '))

if input_month in winter:
    if input_day >=21 and input_month =='Dec':
        Season='Winter'
    elif input_day <=19 and input_month =='Mar':
        Season='Winter'
    else:
        Season='Winter'

elif input_month in spring:
    if input_day >=20 and input_month =='Mar':
        Season='Spring'
    elif input_day <=20 and input_month =='Jun':
        Season='Spring'
    else:
        Season='Spring'

elif input_month in summer:
    if input_day >=21 and input_month =='Jun':
        Season='Summer'
    elif input_day <=21 and input_month =='Sep':
        Season='Summer'
    else:
        Season='Summer'

elif input_month in fall:
    if input_day >=22 and input_month =='Sep':
        Season='Fall'
    elif input_day <=20 and input_month =='Dec':
        Season='Fall'
    else:
        Season='Fall'



print(f" {input_month} {input_day} is in  {Season}")

