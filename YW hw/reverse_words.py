
list2 = []
for i in range(1,6):
    list1 = []
    word1 = input('Enter in a word: ')
    list1.append(word1)
    reverse_word = word1[::-1]
    list1.append(reverse_word)
    list2.append(list1)
    print(reverse_word)
print(list2)