"""Exercise
A leap year is a year that consists of 366, and not 365, days. It roughly occurs every four years. More specifically, 
a year is considered leap if it is either divisible by 4 but not by 100 or divisible by 400.

Write a program that asks the user for a year and replies with either: leap year or not a leap year."""

year = int(input('Provide a year: '))

if (year % 4 == 0 and year % 100 != 0):
  print("leap year")
elif (year % 4 == 0 and year % 400 == 0):
  print("leap year")
else:
  print("not a leap year")
