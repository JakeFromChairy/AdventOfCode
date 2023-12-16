sum = 0
redMax = 12
greenMax = 13
blueMax = 14


File.foreach("../resources/input.txt", chomp: true) do |line|
    gameIsPossible = true
    
    # Split line into title and results
    info = line.split(':')
    title = info[0]
    results = info[1]
    
    # Split the results into individual rounds
    rounds = results.split(';')
    
    rounds.each { |round|
        # Split the round into counts...
        counts = round.split(',')
        
        counts.each { |count|
            outcome = count.split(' ')
                        
            # And the count into value and color
            # NOTE the difference compared to python where ruby's split will
            # simply be: ['#', 'color']
            # then check for impossible games
            if outcome[1] == 'red'
                if (outcome[0]).to_i > redMax
                    gameIsPossible = false
                    break
                end
            end
            
            if outcome[1] == 'green'
                if (outcome[0]).to_i > greenMax
                    gameIsPossible = false
                    break
                end
            end
            
            if outcome[1] == 'blue'
                if (outcome[0]).to_i > blueMax
                    gameIsPossible = false
                    break
                end
            end
            
        } # end of counts.each
        
        if gameIsPossible == false
            break
        end
        
    }# end of rounds.each
    
    if gameIsPossible
        gameID = (title.split(' ')[1]).to_i
        sum += gameID
    end
    
end


puts sum
