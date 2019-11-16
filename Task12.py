word = input('Напишите любое слово: ')

print(word)

letter = input('Напишите любую букву: ')

if word.count(letter) > 1:
    print(word.find(letter))
    print(word.rfind(letter))
elif word.count(letter) == 1:
    print(word.find(letter))
else:
    print('Здесь нет этой буквы.')