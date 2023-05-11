
import jamspell

# Create a JamSpell object with the path to the model file
spell_checker = jamspell.TSpellCorrector()
model_path = "path/to/model"
spell_checker.LoadLangModel(model_path)

def autocorrect(word):
    # Use the Correct method of the JamSpell object to autocorrect the word
    corrected_word = spell_checker.FixFragment(word)
    return corrected_word

autocorrect('aple')


autocorrect('banna')


autocorrect('grape')
