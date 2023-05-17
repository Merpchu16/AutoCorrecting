# # from spellchecker import SpellChecker

# # spell = SpellChecker()

# # # find those words that may be misspelled
# # misspelled = spell.unknown(['something', 'is', 'hapenning', 'here'])

# # for word in misspelled:
# #     # Get the one `most likely` answer
# #     print(spell.correction(word))

# #     # Get a list of `likely` options
# #     print(spell.candidates(word))

# # from spellchecker import 

# # spell = Speller(lang='en')
# # word = 'applee'


# # correction = spell.correction(word)
# # candidates = spell.candidates(word)


# # def autocorrect(text):
# #     words = text.split()
# #     corrected_words = []
# #     for word in words:
# #         corrected_word = spell.correction(word)
# #         corrected_words.append(corrected_word)
# #     return ' '.join(corrected_words)


# # from spellchecker import SpellChecker
# # from Levenshtein import distance

# # # create a SpellChecker object
# # spell = SpellChecker()

# # # ask for the user's possible misspelled sentance
# # sentence = input("Enter a sentence: ")

# # # split the sentence
# # words = sentence.split()

# # # variables to track the number of corrected words and total edit distance
# # num_corrected = 0
# # total_edit_distance = 0

# # # loop through each word in the sentence
# # for i, word in enumerate(words):
# #     # find the corrected spelling of the word
# #     corrected_word = spell.correction(word)
    
# #     # calculate the edit distance between the original word and the corrected word
# #     edit_distance = distance(word, corrected_word)
    
# #     # update the total edit distance
# #     total_edit_distance += edit_distance
    
# #     # check if the word was corrected
# #     if word != corrected_word:
# #         # update the number of corrected words
# #         num_corrected += 1
        
# #         # replace the original word with the corrected word
# #         words[i] = corrected_word

# # # join the corrected words back into a sentence
# # corrected_sentence = " ".join(words)

# # # output the corrected sentence and summary statistics
# # print("Is this what you meant?: ", corrected_sentence)
# # print("Number of corrected words: ", num_corrected)
# # print("Total edit distance: ", total_edit_distance)


# # from spellchecker import SpellChecker
# # from Levenshtein import distance

# # # Create a SpellChecker object
# # spell = SpellChecker()

# # # Load a custom dictionary
# # custom_dictionary = ["python", "code", "spellchecker", "autocorrect"]

# # # Add the custom dictionary to the spell checker
# # spell.word_frequency.load_words(custom_dictionary)

# # # Function to find the corrected spelling of a word
# # def get_corrected_word(word):
# #     return spell.correction(word)

# # # Function to calculate the edit distance between two words
# # def calculate_edit_distance(word1, word2):
# #     return distance(word1, word2)

# # # Function to correct the sentence
# # def correct_sentence(sentence):
# #     # Split the sentence into words
# #     words = sentence.split()

# #     # Variables to track the number of corrected words and total edit distance
# #     num_corrected = 0
# #     total_edit_distance = 0

# #     # Loop through each word in the sentence
# #     for i, word in enumerate(words):
# #         # Find the corrected spelling of the word
# #         corrected_word = get_corrected_word(word)

# #         # Calculate the edit distance between the original word and the corrected word
# #         edit_distance = calculate_edit_distance(word, corrected_word)

# #         # Update the total edit distance
# #         total_edit_distance += edit_distance

# #         # Check if the word was corrected
# #         if word != corrected_word:
# #             # Update the number of corrected words
# #             num_corrected += 1

# #             # Replace the original word with the corrected word
# #             words[i] = corrected_word

# #     # Join the corrected words back into a sentence
# #     corrected_sentence = " ".join(words)

# #     # Return the corrected sentence and summary statistics
# #     return corrected_sentence, num_corrected, total_edit_distance

# # # Ask for the user's sentence
# # sentence = input("Enter a sentence: ")

# # # Correct the sentence
# # corrected_sentence, num_corrected, total_edit_distance = correct_sentence(sentence)

# # # Output the corrected sentence and summary statistics
# # print("Is this what you meant?:", corrected_sentence)
# # print("Number of corrected words:", num_corrected)
# # print("Total edit distance:", total_edit_distance)


# from spellchecker import SpellChecker
# from Levenshtein import distance

# class SpellCheckerApp:
#     def __init__(self):
#         self.spell = SpellChecker()
#         self.num_corrected = 0
#         self.total_edit_distance = 0

#     def load_dictionary(self, dictionary_file):
#         with open(dictionary_file, 'r') as f:
#             dictionary_words = f.read().splitlines()
#         self.spell.word_frequency.load_words(dictionary_words)

#     def spell_check_sentence(self, sentence):
#         words = sentence.split()
#         corrected_words = []
        
#         for word in words:
#             corrected_word = self.spell.correction(word)
#             edit_distance = distance(word, corrected_word)
#             self.total_edit_distance += edit_distance
            
#             if word != corrected_word:
#                 self.num_corrected += 1
#                 corrected_words.append(corrected_word)
#             else:
#                 corrected_words.append(word)
        
#         corrected_sentence = " ".join(corrected_words)
#         return corrected_sentence

#     def run(self):
#         dictionary_file = 'dictionary.txt'
#         self.load_dictionary(dictionary_file)

#         sentence = input("Enter a sentence: ")
#         corrected_sentence = self.spell_check_sentence(sentence)

#         print("Original sentence: ", sentence)
#         print("Corrected sentence: ", corrected_sentence)
#         print("Number of corrected words: ", self.num_corrected)
#         print("Total edit distance: ", self.total_edit_distance)

# app = SpellCheckerApp()
# app.run()
