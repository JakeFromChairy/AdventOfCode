input = open("../resources/input.txt","r")
lines = input.read().splitlines()

sum = 0
redMax = 12
greenMax = 13
blueMax = 14

for line in lines:
    gameIsPossible = True

    # Split line into title and results
    info = line.split(':')
    title = info[0]
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
            # then check for impossible games
        
            if outcome[2] == 'red':
                if int(outcome[1]) > redMax:
                    gameIsPossible = False
                    break
            if outcome[2] == 'green':
                if int(outcome[1]) > greenMax:
                    gameIsPossible = False
                    break
            if outcome[2] == 'blue':
                if int(outcome[1]) > blueMax:
                    gameIsPossible = False
                    break
        
        if gameIsPossible == False:
            break
            
    if gameIsPossible:
        gameID = int(title.split(' ')[1])
        sum += gameID



print(sum)
