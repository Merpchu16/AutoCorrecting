from spellchecker import SpellChecker

spell = SpellChecker()

# find those words that may be misspelled
misspelled = spell.unknown(['something', 'is', 'hapenning', 'here'])

for word in misspelled:
    # Get the one `most likely` answer
    print(spell.correction(word))

    # Get a list of `likely` options
    print(spell.candidates(word))

# from spellchecker import 

# spell = Speller(lang='en')
# word = 'applee'


# correction = spell.correction(word)
# candidates = spell.candidates(word)


# def autocorrect(text):
#     words = text.split()
#     corrected_words = []
#     for word in words:
#         corrected_word = spell.correction(word)
#         corrected_words.append(corrected_word)
#     return ' '.join(corrected_words)
