# Python offers several ways to reverse a String. This is a classic thing
# that lots of people want to do. It's probably easy to look up this
# answer on Stack Overflow.
#
# This website of 30 Python Tips and Tricks also happens to point out
# several ways to reverse a string, and it's a good read!
#
# http://www.techbeamers.com/essential-python-tips-tricks-programmers/?utm_source=mybridge&utm_medium=blog&utm_campaign=read_more#tip1

"""### Challenge 2 - Reverse a string
Reverse a string manually. Don't use s[::-1] (even though that's awesome).
Create a new variable storing an empty string and add the letters from
the first string one by one. The for loop should iterate over the length
of the string and you should access letters individually.

Below is some sample output.

```
Enter a string:
reverse_me
em_esrever
```"""

string_empty = []
string_forward = "This_is_a_string"
string_forward.split(" ")
string_empty[:] = string_forward
rev_string = " "
for i in range(len(string_empty)):
    rev_string += string_empty[len(string_empty) - 1 - i]
 
    
print(rev_string)    

    
