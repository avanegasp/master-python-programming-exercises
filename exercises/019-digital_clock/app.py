# Complete the function to return how many hours and minutes are displayed on the 24h digital clock
def digital_clock(n):

  mid_hour = n // 60
  mid_sec = n % 60

  return mid_hour, mid_sec

# Invoke the function with any integer (minutes after midnight)
print(digital_clock(250))
