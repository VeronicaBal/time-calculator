def add_minutes(start_min, dur_min, dur_hour):
  res_min = int(start_min) + int(dur_min);

  #Edge case: it's the next hour
  if res_min >= 60:
    res_min = res_min-60
    dur_hour = int(dur_hour)+1

  #Edge case: we need a zero to have 2 digits
  if res_min < 10:
    res_min = "0" + str(res_min)

  return res_min, dur_hour