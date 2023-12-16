# Init vars
sum = 0

reg = /(?=(\d|zero|one|two|three|four|five|six|seven|eight|nine))/
values = {
    '0' => 0,
    '1' => 1,
    '2' => 2,
    '3' => 3,
    '4' => 4,
    '5' => 5,
    '6' => 6,
    '7' => 7,
    '8' => 8,
    '9' => 9,
    'zero' => 0,
    'one' => 1,
    'two' => 2,
    'three' => 3,
    'four' => 4,
    'five' => 5,
    'six' => 6,
    'seven' => 7,
    'eight' => 8,
    'nine' => 9
}


# Pipe the file line by line and do per line
File.foreach("../resources/input.txt", chomp: true) do |line|
    # Get the first and last digits as their values
    numbers = line.scan(reg)
    
    # Note the output of Ruby's scan is different than Python's re.findall
    # when using lookahead in the regex.
    firstDigitValue = values[numbers[0][0]] * 10
    lastDigitValue = values[numbers[-1][0]]
    
    # accumulate
    sum += (firstDigitValue+lastDigitValue)

end

puts sum
