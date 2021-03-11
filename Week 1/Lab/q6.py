word = input('Enter a word: ')
check = ''.join(reversed(word))

if check.lower()==word.lower():
    print(f'{word} is a Palindrome.')
else:
    print(f'{word} is NOT a Palindrome.')