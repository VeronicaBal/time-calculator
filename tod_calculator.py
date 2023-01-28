def tod_calculator(res_hour, start_hour, morning, extra_days):
  if res_hour == 12 and start_hour != 12:
    #If the starting hour was in the evening, now it's the next day
    if not morning:
      extra_days = extra_days + 1
    #Change AM/PM
    morning = not morning
  else:
    #Convert to twelve-hour-format if necessary
    while res_hour > 12 :
      res_hour = res_hour - 12
      #If it was the evening, now it's the next day
      if morning == False:
        extra_days = extra_days + 1
      #Every time 12 hours pass, we change the time of the day (AM/PM)
      morning = not morning
  return res_hour, morning, extra_days
  