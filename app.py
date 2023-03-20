# Exercise 1: Vowel or Consonant
# ------------------------------------------------------------------ #
# Write the code that:
# 1. Prompts the user to enter a letter in the alphabet:
#      Please enter a letter from the alphabet (a-z or A-Z):
# 2. Write the code that determines whether the letter entered is a vowel
# 3. Print one of following messages (substituting the letter for x):
#      - The letter x is a vowel
#      - The letter x is a consonant

# Hints:  Use the in operator to check if a character is in another string
#         For example, if some_char in 'abc':
# ------------------------------------------------------------------ #
letter = input(
    'Please enter a letter from the alphabet (a-z or A-Z): ').lower()
if letter in 'a e i o u y':
    print(f'The letter {letter} is a vowel')
else:
    print(f'The letter {letter} is a consonant')


# Exercise 2: Length of Phrase
# ------------------------------------------------------------------ #
# Write the code that:
# 1. Prompts the user to enter a phrase:
#      Please enter a word or phrase:
# 2. Print the following message:
#      - What you entered is xx characters long
# 3. Return to step 1, unless the word 'quit' was entered.
# ------------------------------------------------------------------ #
phrase = ''
while phrase != 'quit':
    phrase = input('Please enter a word or phrase: ')
    print(f'What you entered is {len(phrase)} characters long')


# Exercise 3: Calculate Dog Years
# ------------------------------------------------------------------ #
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
# ------------------------------------------------------------------ #
human_years = int(input("Input a dog's age in human years: "))
if human_years < 3:
    dog_years = human_years * 10
else:
    dog_years = 20 + (human_years - 2) * 7
print(f"The dog's age in dog years is {dog_years}")


# Exercise 4: What kind of Triangle?
# ------------------------------------------------------------------ #
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
# ------------------------------------------------------------------ #
print('Enter the lengths of three side of a triangle:')
a = input('a: ')
b = input('b: ')
c = input('c: ')

if a == b and b == c:
    print(
        f'A triangle with sides of {a}, {b} & {c} is an equalateral triangle')
elif a != b and a != c and b != c:
    print(f'A triangle with sides of {a}, {b} & {c} is a scalene triangle')
else:
    print(f'A triangle with sides of {a}, {b} & {c} is an isosceles triangle')


# Exercise 5: Fibonacci sequence for first 50 terms
# ------------------------------------------------------------------ #
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
# ------------------------------------------------------------------ #
# Using a range with a for loop
a = 1
b = 1
for term in range(50):
    if term < 2:
        print('term: {term} / number: {term}')
    else:
        c = a + b
        print(f'term: {term} / number: {c}')
        a = b
        b = c

# Using a while loop
term = 0
a = 0
b = 1
while term < 50:
    if term < 2:
        print(f'term: {term} / number: {term}')
    else:
        num = a + b
        print(f'term: {term} / number: {num}')
        a = b
        b = num
    term += 1


# Exericse 6: What's the Season?
# ------------------------------------------------------------------ #
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
# ------------------------------------------------------------------ #
mo = input('Enter the month of the season (Jan - Dec): ')
day = int(input('Enter the day of the month: '))
if mo in ('Jan', 'Feb', 'Mar'):
    season = 'Winter'
elif mo in ('Apr', 'May', 'Jun'):
    season = 'Spring'
elif mo in ('Jul', 'Aug', 'Sep'):
    season = 'Summer'
else:
    season = 'Fall'
if mo == 'Mar' and day > 19:
    season = 'Spring'
elif mo == 'Jun' and day > 20:
    season = 'Summer'
elif mo == 'Sep' and day > 21:
    season = 'Fall'
elif mo == 'Dec' and day > 20:
    season = 'Winter'
print(f'{mo} {day} is in {season}')

# More concise using the Python version of a ternary expression...
mo = input('Enter the month of the year (Jan - Dec): ')
day = int(input('Enter the day of the month: '))
if mo in ('Dec', 'Jan', 'Feb'):
    season = 'Fall' if mo == 'Dec' and day < 21 else 'Winter'
elif mo in ('Mar', 'Apr', 'May'):
    season = 'Winter' if mo == 'Mar' and day < 20 else 'Spring'
elif mo in ('Jun', 'Jul', 'Aug'):
    season = 'Spring' if mo == 'Jun' and day < 21 else 'Summer'
else:
    season = 'Summer' if mo == 'Sep' and day < 22 else 'Fall'
print(f'{mo} {day} is in {season}')
