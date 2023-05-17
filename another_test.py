import difflib
import re
from Levenshtein import distance

# Initiates the class Autocorrector
class Autocorrector:
    def __init__(self):
        # Makes a list named dictionary
        self.dictionary = []
        self.total_edit_distance = 0

    # A function that uses the data from dictionary_file, makes it underscored and finds words within it
    def load_dictionary(self, dictionary_file):
        with open(dictionary_file, 'r') as f:
            file_data = f.read().lower()
            # Uses regular expression to find all the words in the file data
            self.dictionary = re.findall('\w+', file_data)

    # A function that finds the most similar words to the given word from the loaded dictionary
    def find_most_similar_word(self, word):
        # Uses the difflib module to get the closest matches from the dictionary based on similarity
        closest_words = difflib.get_close_matches(word, self.dictionary, n=5, cutoff=0.8)
        return closest_words

    # A function that corrects a word if it is not in the dictionary
    def correct_word(self, word):
        if word in self.dictionary:
            # If the word is in the dictionary, return it as it is
            return word
        else:
            similar_words = self.find_most_similar_word(word)
            if similar_words:
                # If similar words are found, select the closest word and calculate the edit distance
                closest_word = similar_words[0]
                self.total_edit_distance += distance(word, closest_word)
                return closest_word
            else:
                # If no similar words are found, return None
                return None

    # A function to check and send out the corrected sentence
    def correct_sentence(self, sentence):
        words = sentence.split()
        corrected_words = []
        for word in words:
            corrected_word = self.correct_word(word)
            if corrected_word is not None:
                corrected_words.append(corrected_word)
            else:
                # If a word cannot be corrected, return a prompt
                return "Sorry, I'm not smart enough to know that word."
        corrected_sentence = " ".join(corrected_words)
        return corrected_sentence

    # A function to get the total edit distance
    def get_total_edit_distance(self):
        return self.total_edit_distance

# Prints everything out into the terminal
def main():
    autocorrector = Autocorrector()
    dictionary_file = 'theProject.txt'
    autocorrector.load_dictionary(dictionary_file)

    user_input = input("Enter a sentence: ")
    corrected_sentence = autocorrector.correct_sentence(user_input)
    total_edit_distance = autocorrector.get_total_edit_distance()

    print("Is this what you meant?: ", corrected_sentence)
    print("Total edit distance: ", total_edit_distance)

if __name__ == "__main__":
    main()
