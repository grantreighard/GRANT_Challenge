# Solution for https://www.hackerrank.com/challenges/validating-credit-card-number/problem

import sys
import re

data = [line.rstrip().split('\n') for line in sys.stdin.readlines()]

for i in range(1, len(data)):
    text = data[i][0]
    text_without_dashes = "".join(text.split("-"))
    correct_with_dashes = re.search("[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{4}", text)
    correct_without_dashes = re.search("[0-9]{16}", text)
    starts_with_four_five_or_six = text[0] == "4" or text[0] == "5" or text[0] == "6"
    four_consecutive = re.search(r'(\d)\1{3}', text_without_dashes)
    
    output = "Invalid"
    if starts_with_four_five_or_six:
        if correct_with_dashes or correct_without_dashes:
            if not four_consecutive:
                output = "Valid"
    
    print(output)