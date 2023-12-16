# Init the sum
sum = 0

# Pipe the file line by line and do per line
File.foreach("../resources/input.txt") do |line|
    # Get the first and last digit
    numbers = line.scan(/\d/)
    
    # Add the first and last digits as string, convert to an int, accumulate
    sum += (numbers[0] + numbers[-1]).to_i
    
end

puts sum
