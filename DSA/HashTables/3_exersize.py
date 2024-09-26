file = r'C:\mine\python_django\DSA\csv_files\nyc_weather.csv'  # Using raw string
weather = {}

with open(file, mode='r') as f:
    # Skip the header line
    next(f)
    
    for line in f:
        tokens = line.split(',')
        date = tokens[0].strip()  # Remove any leading/trailing whitespace or newlines
        temp = tokens[1].strip()  # Remove any leading/trailing whitespace or newlines
        weather[date] = temp

print(weather)


"""
nyc_weather.csv contains new york city weather for first few days in the month of January. Write a program that can answer following,
    1. What was the average temperature in first week of Jan
    2.What was the maximum temperature in first 10 days of Jan
Figure out data structure that is best for this problem

What was the temperature on Jan 9?
What was the temperature on Jan 4?
"""
sum =0
count = 0
for val in weather.values():
    if count >7:
        break
    sum+=int(val)
    count+=1
print(f'{sum=},{count=}')
print(max(weather.values()))
print(weather['Jan 9'])
print(weather['Jan 4'])
print(sum/7)
