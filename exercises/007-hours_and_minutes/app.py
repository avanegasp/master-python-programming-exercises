def hours_minutes(seconds):
  # Your code here
  seconds_time = round(seconds / 3600)
  hour_time = (seconds_time - 1) * 60

  if hour_time > 60:
    hour_time -= 60
  return hour_time, seconds_time

# Invoke the function and pass any integer as its argument
print(hours_minutes(3900))
