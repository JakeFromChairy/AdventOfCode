input = open("../resources/input.txt","r")
lines = input.read().splitlines()

sum = 0

for line in lines:
    minNeededRed = 0
    minNeededBlue = 0
    minNeededGreen = 0

    # Split line into title and results
    info = line.split(':')
    results = info[1]

    # Split the results into individual rounds
    rounds = results.split(';')

    for round in rounds:
        # Split the round into counts...
        counts = round.split(',')
                
        for count in counts:
            outcome = count.split(' ')
            # And the count into value and color, ignoring the space,
            # will be: ['', '#', 'color']
            # then check values to determine minimum needed per game
        
            if outcome[2] == 'red':
                if int(outcome[1]) > minNeededRed:
                    minNeededRed = int(outcome[1])
            if outcome[2] == 'green':
                if int(outcome[1]) > minNeededGreen:
                    minNeededGreen = int(outcome[1])
            if outcome[2] == 'blue':
                if int(outcome[1]) > minNeededBlue:
                    minNeededBlue = int(outcome[1])
            
    # Get the power of the set & add to the sum
    power = minNeededRed * minNeededBlue * minNeededGreen
    sum += power


print(sum)
