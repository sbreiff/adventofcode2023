# Advent of Code Day 1


def find_digit(text_input, words=False):
    number_words = {
        'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 
        'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9', 
        'ten': '10', 'eleven': '11', 'twelve': '12', 'thirteen': '13', 'fourteen': '14', 
        'fifteen': '15', 'sixteen': '16', 'seventeen': '17', 'eighteen': '18', 'nineteen': '19',
        'twenty': '20', 'thirty': '30', 'forty': '40', 'fifty': '50', 
        'sixty': '60', 'seventy': '70', 'eighty': '80', 'ninety': '90', 'hundred': '100' 
    }
    for d in '0123456789':
        if d in text_input:
            return d
    if words:
        for word in number_words.keys():
            if word in text_input:
                return number_words[word][0]
    return None
        

def get_numbers(text_input, words=False):
    first_digit = None
    last_digit = None
    for i in range(1, len(text_input) + 1):
        start = text_input[:i]
        end = text_input[len(text_input)-i:]
        if not first_digit:
            first_digit = find_digit(start, words=words)
        if not last_digit:
            last_digit = find_digit(end, words=words)
        if first_digit and last_digit:
            break
    return int(''.join([first_digit, last_digit]))


def sum_digits(data, words=False):
    return sum([get_numbers(line.strip(), words=words) for line in data if line])


if __name__ == '__main__':
    with open('input.txt') as infile:
        input_data = infile.readlines()
    
    print('Part 1 Answer: ', sum_digits(input_data))
    print('')
    print('Part 2 Answer: ', sum_digits(input_data, words=True))
    