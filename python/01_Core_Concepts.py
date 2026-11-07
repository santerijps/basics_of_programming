# Core concepts
# This is a comment
# Comments do not get executed as code
# print("Hello")

# Values and Data types

# Numbers
31 # integer (kokonaisluku)
3.14 # float (desimaaliluku)

# String (text)
'31'
"31"
"Santeri"

# Boolean
# Used in comparisons
# Truth values, is something X?
True # Always with an uppercase T
False # Always with an uppercase F

# List
[] # brackets
list() # built-in function
[1, 2, 3, "Santeri", True]

[   # name      age
    ["Santeri", 31],
    ["Alice",   50]
]

# Dictionary (key-value pairs)
{} # braces
# key    value
{"dog": "dogs are canines..."}
dict()

# Tuple (immutable list)
# Immutable = cannot be "mutated" (changed)
(1, 2) # parentheses
tuple()

# How to use the above values?
# We can create variables!
# In euros €
water_price = 1.5
spaghetti_price = 18
ice_cream_price = 4

total_bill = water_price + spaghetti_price + ice_cream_price
print(total_bill)

# Count the total weight of apples picked
apple_weights = [1, 0.5, 2]
apple_total = 0

for weight in apple_weights: # for-loop
    apple_total = apple_total + weight
    # apple_total += weight # same as above

print(apple_total)

# Example: is Alice an adult?
alice_age = 16
is_alice_adult = alice_age >= 18

if is_alice_adult:
    print("Alice is an adult!")
# elif (else if)
else:
    print("Alice is a child!")

# Loops
# Coding structure where some code is repeated X times

# While loop
print("Count from 1 to 10 with a while-loop")
count = 0
while count < 10: # while CONDITION:
    count += 1 # count = count + 1
    print(count)

print("Done!")

# For loop
print("Count from 1 to 10 with a for-loop")
for count in range(1, 11): # range is a function (more on that later)
    # 1 is inclusive
    # 11 is exclusive
    print(count)

print("Done!")

# Functions
# If we want to run the same code in many different places

def is_adult(name, age):
    # is_adult -> function name
    # name -> first parameter (variable in the function) (argument)
    # age -> second parameter (variable in the function) (argument)

    if age >= 18:
        print(f"{name} is an adult!")
    else:
        print(f"{name} is not an adult...")

is_adult("Seppo", 6)
is_adult("Matti", 80)
