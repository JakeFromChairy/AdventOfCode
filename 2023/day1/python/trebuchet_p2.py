'''
The newly-improved calibration document consists of lines of text; each line
originally contained a specific calibration value that the Elves now need to
recover. On each line, the calibration value can be found by combining the
first digit and the last digit (in that order) to form a single two-digit
number.

For example:

1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet

In this example, the calibration values of these four lines are 12, 38, 15, and
77. Adding these together produces 142.

Consider your entire calibration document. What is the sum of all of the calibration values?
'''

import re

input = open("../resources/input.txt","r")
lines = input.readlines()

targets = [
    '0','1','2','3','4','5','6','7','8','9',
    'zero','one','two','three','four','five','six','seven','eight','nine'
]
values = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

sum = 0

for line in lines:
    numbers = re.findall(r"(?=("+'|'.join(targets)+r"))", line)
        
    firstDigitValue = values[numbers[0]] * 10
    lastDigitValue = values[numbers[-1]]
    
    sum += (firstDigitValue+lastDigitValue)

print(sum)


'''
Correct Answer: 54203
'''
