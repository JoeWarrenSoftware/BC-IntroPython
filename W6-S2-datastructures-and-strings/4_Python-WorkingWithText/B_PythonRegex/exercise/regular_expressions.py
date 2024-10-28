import re

pattern = r'\d+'

inputText1 = 'The price is 100 dollars'

# The search return contains a result object where the group shows the first occurrence 
match = re.search(pattern, inputText1)

print(f"Match Found: {match.group()}")

inputText2 = 'The price is 100 dollars, discounted from 200 dollars!'

allMatches = re.findall(pattern, inputText2)

print(f"Match Found: {allMatches}")

#Replace the numbers in the text with XX
hiddenNumbers = re.sub(pattern, "XX", inputText2)
print(f"Replaced Text: {hiddenNumbers}")

# This pattern is true for the strings 12/2020 and also 12
optionalPattern = r'?:/\d{4}'

inputDate1 = '12/20/2024'
inputDate2 = '12/20'
inputDate3 = '12/20/'

matchComplex = re.search(optionalPattern, inputDate1)

print(f"inputDate1: {matchComplex.group()}")