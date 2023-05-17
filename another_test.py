import difflib
import re
from Levenshtein import distance

class Autocorrector:
    def __init__(self):
        self.dictionary = []
        self.total_edit_distance = 0
    
    def load_dictionary(self, dictionary_file):
        with open(dictionary_file, 'r') as f:
            file_data = f.read().lower()
            self.dictionary = re.findall('\w+', file_data)
    
    def find_most_similar_word(self, word):
        closest_words = difflib.get_close_matches(word, self.dictionary, n=5, cutoff=0.8)
        return closest_words
    
    def correct_word(self, word):
        if word in self.dictionary:
            return word
        else:
            similar_words = self.find_most_similar_word(word)
            if similar_words:
                closest_word = similar_words[0]
                self.total_edit_distance += distance(word, closest_word)
                return closest_word
            else:
                return None
    
    def c_sentence(self, sentence):
        words = sentence.split()
        corrected_words = []
        for word in words:
            corrected_word = self.correct_word(word)
            if corrected_word is not None:
                corrected_words.append(corrected_word)
            else:
                return "Sorry, I'm not smart enough to know that word."
        corrected_sentence = " ".join(corrected_words)
        return corrected_sentence
    
    def get_total_edit_distance(self):
        return self.total_edit_distance


def main():
    autocorrector = Autocorrector()
    dictionary_file = 'dictionary.txt'
    autocorrector.load_dictionary(dictionary_file)

    user_input = input("Enter a sentence: ")
    ctd_sentence = autocorrector.c_sentence(user_input)
    total_edit_distance = autocorrector.get_total_edit_distance()

    print("Is this that you meant?: ", ctd_sentence)
    print("Total edit distance: ", total_edit_distance)


if __name__ == "__main__":
    main()
