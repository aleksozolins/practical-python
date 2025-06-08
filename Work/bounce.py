# bounce.py
#
# Exercise 1.5

height = 100 # Meters
drop = 1 # Which time it is dropped

while drop <= 10:
    height = height * .6
    print(drop, round(height, 4))
    drop += 1
