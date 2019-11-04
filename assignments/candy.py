candy1 = "Snickers"
candy2 = "Heath"
candy3 = "Twix"

timeofday = input("Enter the time of day (M,A,E): ")

if timeofday == "M":
  print("Because it's morning, you eat "+candy1)
elif timeofday == "A":
  print("Because it's afternoon, you eat "+candy2)
else:
  print("Because it's evening, you eat "+candy3)
