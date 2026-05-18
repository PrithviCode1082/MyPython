sentence = input("Enter any sentence with more than 4-5 words: ")

# printing first 5 words
print(sentence[0:5])

#printing last 5 words
print(sentence[len(sentence) - 5 : len(sentence)])

#printing every other character
print(sentence[0:len(sentence):2])

#printing sentence reversed
print(sentence[::-1])