import string

def skip_symbols(word):
    return word in ["/", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "-", "[", "]", ":", ";", "'", ",", ".", "?", " "]

def word_logic(word, op, key):
    if(word not in lowercase and word in uppercase):
        if op == "enc":
            return uppercase[uppercase.index(word) - key]
        else:
            if(uppercase.index(word) + key > 25):
                return uppercase[(uppercase.index(word) + key) - 26]
            else:
                return uppercase[(uppercase.index(word) + key)]
    else:
        if op == "enc":
            return lowercase[lowercase.index(word) - key]
        else:
            if(lowercase.index(word) + key > 25):
                return lowercase[(lowercase.index(word) + key) - 26]
            else:
                return lowercase[(lowercase.index(word) + key)]


def encrypt(text):
    e_key = int(input("Enter encryption key: "))
    encrypted_text = ""
    for word in text:
        if skip_symbols(word): 
            encrypted_text += word
            continue
        encrypted_text += word_logic(word, "enc", e_key)
    print(text)
    print(encrypted_text)
    return [encrypted_text, e_key]

def decrypt(enc_text, d_key):
    decrypted_text = ""
    for word in enc_text:
        if skip_symbols(word): 
            decrypted_text += word
            continue
        decrypted_text += word_logic(word, "dec", d_key)
    print(enc_text)
    print(decrypted_text)




lowercase = list(string.ascii_lowercase)
uppercase = list(string.ascii_uppercase)

text = input("Enter some words: ")
e_text, e_key = encrypt(text)
decrypt(e_text, e_key)

