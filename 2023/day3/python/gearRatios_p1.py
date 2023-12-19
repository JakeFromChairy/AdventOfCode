import re

input = open("../resources/input.txt","r")
lines = input.read().splitlines()

sum = 0
reg = r"\d+"


for i, line in enumerate(lines):
    # Get indicies of each number in the line
    numbers = re.finditer(reg, line)
    
    for match in numbers:
        # 1 - Check the char before the number
        j = match.start() - 1
        if (j > -1):
            if (lines[i][j] != '.' and not lines[i][j].isdigit()):
                sum += int(match.group())
                continue
        # 2 - Check the char after the number
        k = match.end()
        if (k < len(line)):
            if (lines[i][k] != '.' and not lines[i][k].isdigit()):
                sum += int(match.group())
                continue
        # 3 - Check chars above the number (including diagonal corners)
        if (j < 0):
            j += 1
        k += 1
        if (k > len(line)):
            k -= 1
        lineNum = i - 1
        if (lineNum > -1):
            chars = lines[lineNum][j:k]
            for char in chars:
                if (char != '.' and not char.isdigit()):
                    sum += int(match.group())
                    break
        # 4 - Check chars below the number (including diagonal corners)
        lineNum = i + 1
        if (lineNum < len(lines)):
            chars = lines[lineNum][j:k]
            for char in chars:
                if (char != '.' and not char.isdigit()):
                    sum += int(match.group())
                    break
        
        
        
print(sum)
