sum = 0


File.foreach("../resources/input.txt", chomp: true) do |line|
    minNeededRed = 0
    minNeededBlue = 0
    minNeededGreen = 0
    
    # Split line into title and results
    info = line.split(':')
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
            # then check values to determine minimum needed per game
            if outcome[1] == 'red'
                if (outcome[0]).to_i > minNeededRed
                    minNeededRed = (outcome[0]).to_i
                end
            elsif outcome[1] == 'green'
                if (outcome[0]).to_i > minNeededGreen
                    minNeededGreen = (outcome[0]).to_i
                end
            elsif outcome[1] == 'blue'
                if (outcome[0]).to_i > minNeededBlue
                    minNeededBlue = (outcome[0]).to_i
                end
            end
            
        } # end of counts.each
    }# end of rounds.each
    
    # Get the power of the set & add to the sum
    power = minNeededRed * minNeededBlue * minNeededGreen
    sum += power
    
end


puts sum
