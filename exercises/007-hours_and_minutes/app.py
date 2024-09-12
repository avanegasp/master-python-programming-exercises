def hours_minutes(seconds):
  # Your code here
  # minutes = int(seconds / 60)

  # if minutes == 65:
  #   minutes_2 = minutes - 5
  #   minutes_2 = 1

  # minutes_1 = minutes - minutes_2 + 1
  # return minutes_2, minutes_1

  hours = seconds // 3600
  print(hours)
  remaining_seconds = seconds % 3600
  print("****",remaining_seconds)
  minutes = remaining_seconds // 60

  return hours, minutes

# Invoke the function and pass any integer as its argument
print(hours_minutes(3900))
