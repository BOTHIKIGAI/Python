"""
String Assignment we will do together:

Ask the user how many days until their birthday
and print an approx number of weeks until their birthday

Weeks is = 7 days

Decimal within the return is allowed...
"""

days = input("Cuantos dias faltan para tu cumpleaños: ")
weeks = round(int(days) / 7)
print(weeks)