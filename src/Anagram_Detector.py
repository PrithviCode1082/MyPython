# Anagram Detector
# Check if two strings are anagrams.
# Then group a list of words into anagram clusters (e.g. [eat, tea, ate] → one cluster).

words = ["listen", "silent", "enlist", "rat", "tar", "art", "evil", "live", "veil", "vile",
 "elbow", "below", "state", "taste", "brag", "grab", "night", "thing", "dusty", "study", "cat", "act",
  "stew", "west", "save", "vase", "cider", "cried", "binary", "brainy"]

anagram = {}

def util(word):
    original = "".join(sorted(word))
    if original in anagram.keys():
        anagram[original].append(word)
    else:
        anagram[original] = []
        anagram[original].append(word)

for word in words:
    util(word)

i = 1
for k, v in anagram.items():
    print(f"{i}) {k}: ")
    for word in anagram[k]:
        print(f"    {word}")
    i += 1