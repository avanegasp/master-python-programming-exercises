# Complete the function to return the number of day of the week for k'th day of year
def day_of_week(k):

  any_day = int(k)
  day_of_year = (any_day + 3) %7

  return day_of_year


# Invoke function day_of_week with an integer between 1 and 365
print(day_of_week(1))
