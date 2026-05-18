def checker(word):
    check = [",", "'", "!", " ", ".", ";"]
    new_word = ""
    for ch in check:
        if ch in word:
            word = word.replace(ch, "")

    return word

common_words = {}

with open("Text.txt", 'r') as reader:
    paragraph = reader.read().strip().split(" ")
    for word in paragraph:
        new_word = checker(word)
        if new_word in common_words:
            common_words[new_word] += 1
        else:
            common_words[new_word] = 1


unique_dict = {}
for k, v in common_words.items():
    if v not in unique_dict.values():
        unique_dict[k] = v
        print(f"{k} - {v}")

