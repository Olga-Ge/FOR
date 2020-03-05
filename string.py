number_of_words = 0
sentence = input("give me a sentence")
for letter in sentence:
    if letter == " ":
        number_of_words = (number_of_words+1)
        print("there are", number_of_words+1, "words")
