from YW import letters, wordsInString

strings = [
    'this is a sentence',
    'apple banana kiwi',
    'folklore evermore midnights',
    'new york paris san francisco'
    '2006'
]

for s in strings:
    # print(s) 
    print(s)
    words = wordsInString(s)
    letters_with_spaces= letters(s) 
    print('\n')
