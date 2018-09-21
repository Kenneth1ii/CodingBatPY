
# Some Problems done on CodingBat Python
#Credits to diezguerra for some of solutions

"""
1.
Given a number n, return True if n is in the range 1..10, inclusive. Unless outside_mode is True, in which case
return True if the number is less or equal to 1, or greater or equal to 10.

"""

# solution
def in1to10(n, outside_mode):
  return n in range(1,11) if not outside_mode else outside_mode and n not in range(2,10)


# found new Solution using Bitwise Operator

 def in1to10(n, outside_mode):
  if n == 1 or n == 10:
    return True
  return (n in range(1,11)) ^ outside_mode


"""
2.
The squirrels in Palo Alto spend most of the day playing. In particular, 
they play if the temperature is between 60 and 90 (inclusive). Unless it is summer, then the upper limit is 100 instead of 90. 
Given an int temperature and a boolean is_summer, return True if the squirrels play and False otherwise.

"""
# my 1st solution

def squirrel_play(temp, is_summer):
    return True if (is_summer and 60 <= temp <= 100) or 60 <= temp <= 90 else False

# Found better solution
def squirrel_play(temp, is_summer):
    return temp in range(60, 101 if is_summer else 91)



"""
3.
You are driving a little too fast, and a police officer stops you. 
Write code to compute the result, encoded as an int value: 0=no ticket, 1=small ticket, 2=big ticket. 
If speed is 60 or less, the result is 0. If speed is between 61 and 80 inclusive, the result is 1. If speed is 81 or more, 
the result is 2. Unless it is your birthday -- on that day, your speed can be 5 higher in all cases.

"""

def caught_speeding(speed, is_birthday):
  if is_birthday:
    if speed <= 65:
      return 0
    if 66 <= speed <= 85:
      return 1
    if speed >= 85:
      return 2
  elif speed <= 60:
    return 0
  elif 61 <= speed <= 80:
    return 1
  else:
    return 2

# Solution 2
  speeding = speed - (65 if is_birthday else 60)
  if speeding > 20:
    return 2
  elif speeding > 0:
    return 1
  else:
    return 0

"""
  Given an array of ints length 3, figure out which is larger, the first or last element in the array, 
and set all the other elements to be that value. Return the changed array.
"""

def max_end3(nums):
  a = max(nums[0],nums[2])
  return [a,a,a]

"""
Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. 
So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.
"""

def string_match(a, b):
  count = 0
  for i in range(len(a)-1):
    if a[i:i+2] == b[i:i+2]:
      count += 1
  return count

"""
Given an int n, return True if it is within 10 of 100 or 200. 
Note: abs(num) computes the absolute value of a number.
"""


#My solution
def near_hundred(n):
  return (n >= 90 and n <= 110 ) or (n >= 190 and n <= 210)

#Solution 2:
def near_hundred(n):
  return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))


"""
  Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat, and a 
  boolean indicating if we are on vacation, return a string of the form "7:00" 
  indicating when the alarm clock should ring. Weekdays, the alarm should be 
  "7:00" and on the weekend it should be "10:00". Unless we are on vacation --
  then on 
"""

def alarm_clock(day, vacation):
  if vacation:
    return '10:00' if day in range(1,6) else 'off'
  if day in range(1,6):
    return '7:00'
  else:
    return '10:00'

def alarm_clock(day, vacation):
    week_preset = "7:00" if not vacation else "10:00"
    weekend_preset = "10:00" if not vacation else "off"
    return week_preset if day not in [6, 0] else weekend_preset
