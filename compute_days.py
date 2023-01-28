def compute_days(res_hour):
  extra_days = 0
  while res_hour >=24:
    res_hour = res_hour - 24
    extra_days = extra_days + 1
  return res_hour, extra_days