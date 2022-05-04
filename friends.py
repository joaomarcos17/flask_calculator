# Problem: Check how old you are on 5 May 2022
import datetime
# start the variables
day = 2

month = 3

year = 1998

current_year = 2022


# Input: day of birthday as an integer from 1 to 31
day = int(input("day of birthday as an integer from 1 to 31:\n"))

# Input: month of birthday as an integer from 1 to 12
month = int(input("month of birthday as an integer from 1 to 12:\n"))

# Input: year of birthday as an integer from 1922 to 2010
year = int(input("year of birthday as an integer from 1922 to 2010:\n"))


# Calculate age based only on year

age = current_year - year

# Adjust for month

if month > 5 :
  
  age = age  # changed sign to positive
 



if month == 5 and day <= 5:
 
  age = age - 1


print('On 5 May 2022 I am ' , age , 'years old')

# print the data types of the variables 
# print(type(year))
# print(type(month))
# print(type(day))

