import re
from add_minutes import add_minutes
from compute_days import compute_days
from tod_calculator import tod_calculator
from dow_calculator import compute_dow


def add_time(start, duration, day=None):
  
  #Initial parsing
  [start_hour, start_min, start_time] = re.search("(\d+):(\d+)\s(\w+)", start).groups();
  morning = (True if start_time == "AM" else False)
  [dur_hour, dur_min] = re.search("(\d+):(\d+)", duration).groups();
  
  #Add minutes
  res_min, dur_hour = add_minutes(start_min, dur_min, dur_hour)

  #Add hours
  res_hour = int(start_hour) + int(dur_hour);
  
  #Compute extra days
  res_hour, extra_days = compute_days(res_hour)

  #Change time of the day (AM/PM)
  if res_hour > 12 or (res_hour == 12 and start_hour != 12):
    res_hour, morning, extra_days = tod_calculator(res_hour, start_hour, morning, extra_days)
  
  result = f'{res_hour}:{res_min} {"AM" if morning else "PM"}'
  
  #Day of the week (optional arg)
  if day != None:
    week_day = compute_dow(day, extra_days)
    result = f'{result}, {week_day}'
    
  #Add extra days to result
  if extra_days > 1:
    result = f'{result} ({extra_days} days later)'
  elif extra_days > 0:
    result = f'{result} (next day)'

  return result
  
  
