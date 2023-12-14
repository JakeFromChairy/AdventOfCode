import re

input = open("../resources/input.txt","r")
lines = input.readlines()

sum = 0

for line in lines:
    numbers = re.findall(r"\d", line)
    sum += int(numbers[0]+numbers[-1])

print(sum)
