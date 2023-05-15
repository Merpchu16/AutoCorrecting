# from spellchecker import SpellChecker

# spell = SpellChecker()

# # find those words that may be misspelled
# misspelled = spell.unknown(['something', 'is', 'hapenning', 'here'])

# for word in misspelled:
#     # Get the one `most likely` answer
#     print(spell.correction(word))

#     # Get a list of `likely` options
#     print(spell.candidates(word))

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


from spellchecker import SpellChecker
from Levenshtein import distance

# create a SpellChecker object
spell = SpellChecker()

# ask for the user's possible misspelled sentance
sentence = input("Enter a sentence: ")

# split the sentence
words = sentence.split()

# variables to track the number of corrected words and total edit distance
num_corrected = 0
total_edit_distance = 0

# loop through each word in the sentence
for i, word in enumerate(words):
    # find the corrected spelling of the word
    corrected_word = spell.correction(word)
    
    # calculate the edit distance between the original word and the corrected word
    edit_distance = distance(word, corrected_word)
    
    # update the total edit distance
    total_edit_distance += edit_distance
    
    # check if the word was corrected
    if word != corrected_word:
        # update the number of corrected words
        num_corrected += 1
        
        # replace the original word with the corrected word
        words[i] = corrected_word

# join the corrected words back into a sentence
corrected_sentence = " ".join(words)

# output the corrected sentence and summary statistics
print("Is this what you meant?: ", corrected_sentence)
print("Number of corrected words: ", num_corrected)
print("Total edit distance: ", total_edit_distance)
