# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

### Challenge 1 - Calculator

"""Create a simple calculator that first asks the user what method they would like
to use (addition, subtraction, multiplication, division) and then asks the user
for two numbers, returning the result of the method with the two numbers. Here
is a sample prompt:

```
What calculation would you like to do? (add, sub, mult, div)
add
What is number 1?
3
What is number 2?
6
Your result is 9
```"""

operation = input("What calculation woud you like to do? (add, sub, mult, div)?  ")
num1 = input("What's the first number? ")
num2 = input("What's the second number?" )

def calc(num1, num2, operation):
    if operation == "add":
        return num1 + num2
    elif operation == "sub":
        return num1 - num2
    elif operation == "mult":
        return num1 * num2
    else:
        return num1 / num2

print(calc(int(num1), int(num2), operation))