#Computes the day of the week based on the original day of the week and the amount of days elapsed since that day
def compute_dow(day, extra_days):
  if extra_days == 0 or extra_days % 7 == 0:
      return day.capitalize()
  else: 
    days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    new_day_index = extra_days + days.index(day.lower())
    #If it's more than a week, remove 7 until it's less than a week
    while new_day_index >= 7:
      new_day_index = new_day_index - 7
    new_day = days[new_day_index]
    return new_day.capitalize()