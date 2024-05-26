hello_1 = "Hello World"
hello_2 = "hello python"

""" Lower and Upper """
# all to lower case
print(hello_1.lower())

# all to upper case
print(hello_1.upper())

# all to capitalize
print(hello_2.capitalize())

# return where start the letter/word in a string and return the index
print(hello_2.index("p"))
print(hello_2.index("python"))

# replace the word
hello_3 = hello_2.replace("hello", "Hi")
print(hello_3)

list_hello_2 = hello_2.split(" ")
print(list_hello_2)

list_hello_2 = hello_2.split("python")
print(list_hello_2)
