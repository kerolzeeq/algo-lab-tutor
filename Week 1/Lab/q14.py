sentence = input('Enter a sentence : ')
words = sentence.split()

reversed_words = list(reversed(words))
for words in reversed_words:
    print(words,end=' ')