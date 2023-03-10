with open("books/frankenstein.txt") as franky:
    file_contents = franky.read()

x = file_contents.split()


def word_count():
    counter = 0
    for word in x:
        counter += 1
    return counter


def letter_count():
    dico = {}
    for word in x:
        for letter in word:
            if letter.lower() in dico:
                dico[letter.lower()] += 1
            else:
                dico[letter.lower()] = 1
    return dico


print(letter_count())
