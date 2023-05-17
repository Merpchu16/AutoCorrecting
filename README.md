# AutoCorrecting

Hello! Welcome to my autocorrector in python.
To begin, please install these two libraries below

# pip install pyspellchecker
# pip install python-Levenshtein
# pip install difflib


Run the program and in the terminal you will see:
# Enter a sentence: 
There you will enter your desired sentance, be it mispelled or even correct type it in!
Next, you'll enter your sentance and the following will pop up
## Corrected sentence:
## Number of corrected words:
## Total edit distance: 
 Here, my program gives you the corrected sentance
 Then, how many words it corrected
 and lastly the total of edits it had to make inbetween.

 # How this runs...
So this program runs by 
First, the code imports necessary libraries: difflib, re, and Levenshtein. These libraries provide functions for string matching and calculating edit distances.

Next, a class named Autocorrector is defined. This class represents an autocorrector object and contains various methods to perform autocorrection.

The Autocorrector class has two attributes: dictionary and total_edit_distance.

dictionary is a list that will store the words from the loaded dictionary file.
# fun fact!
## You can change or even add more files to expand the autocorrectors efficency, by adding a .txt file and attributing it to the dictionary_file near the bottom of the code.


## total_edit_distance 

is an integer that will keep track of the total edit distance calculated during word correction.
## The __init__ method 
is a special method that gets executed when an Autocorrector object is created. It initializes the dictionary and total_edit_distance attributes.

## The load_dictionary method 
takes a dictionary_file parameter, reads the file, and populates the dictionary list with the words from the file. It converts all the words to lowercase using the lower() method and extracts them using regular expression matching with re.findall().

## The find_most_similar_word method 
takes a word parameter and uses the get_close_matches function from difflib library to find the most similar words to the given word in the dictionary. It returns a list of the closest words found.

## The correct_word method
takes a word parameter and checks if the word is present in the dictionary. If it is, the method returns the word itself as it is already correct. If the word is not found, it uses find_most_similar_word to find similar words and calculates the edit distance using distance function from Levenshtein library. The closest word with the lowest edit distance is returned as the corrected word.

## The c_sentence method 
takes a sentence parameter and splits it into individual words. It iterates over each word and calls correct_word to get the corrected version. If a word cannot be corrected, it returns a message saying the autocorrector doesn't know that word. Finally, it joins the corrected words into a sentence and returns it.

## The get_total_edit_distance method
simply returns the value of the total_edit_distance attribute.

## The main function
is where the program starts its execution. It creates an instance of the Autocorrector class, sets the dictionary_file variable to the name of the dictionary file, and calls the load_dictionary method to load the dictionary.

It prompts the user to enter a sentence and reads the input using the input function.

It calls the c_sentence method of the Autocorrector object to correct the sentence entered by the user and assigns the corrected sentence to the ctd_sentence variable.

It calls the get_total_edit_distance method to retrieve the total edit distance and assigns it to the total_edit_distance variable.

Finally, it prints the corrected sentence and the total edit distance on the terminal.