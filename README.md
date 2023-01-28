# Time Calculator
Program to add a duration of time to the start time and return the result, including the amount of days elapsed.
<br> 
<br>

The function takes two required and one optional parameter:
- a start time in the 12-hour clock format (ending in AM or PM)

- a duration time that indicates the number of hours and minutes

- (optional) a starting day of the week, case insensitive
<br> 
<br>

Examples: 
````
add_time("11:43 AM", "00:20")
# Returns: 12:03 PM

add_time("10:10 PM", "3:30")
# Returns: 1:40 AM (next day)

add_time("11:43 PM", "24:20", "tueSday")
# Returns: 12:03 AM, Thursday (2 days later)

````

This project is part of the freeCodeCamp's "Scientific Computing with Python" projects.
Instructions for building this project can be found [here](https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/time-calculator).
