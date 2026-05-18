dee type_convertegword):
    try:
        print("\nAs String: ", word)
        print("As Integer: ", int(float(word)))
        print(f"As Float: {float(word):.2f}")
    except ValueError:
        return

words = [input("Enter a word: ") for word in range(0, 3)]

# Determining the types
[print(f"{word} is of type {type(word)}") for word in words]

[type_converter(word) for word in words]
