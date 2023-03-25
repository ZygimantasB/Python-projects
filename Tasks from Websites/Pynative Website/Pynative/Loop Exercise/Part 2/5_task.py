numbers = [12, 75, 150, 180, 145, 525, 50]

for value in numbers:
    if value > 500:
        break # no more what 525
    if value > 150:
        continue # Skip everything who is more when 150
    if value % 5 == 0:
        print(value)
