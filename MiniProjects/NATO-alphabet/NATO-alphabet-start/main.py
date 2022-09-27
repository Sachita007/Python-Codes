

import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")




# Create a dictionary in this format:
# Keyword Method with iterrows()
nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}

def nato_alpha():
    word = (input("Enter a word:")).lower()
    # Create a list of the phonetic code words from a word that the user inputs.
    try:
        list = [nato_dict[let.title()] for let in word]
    except KeyError:
        print("Sorry, only letters in the alphabets please.")
        nato_alpha()
    else:
        print(list)

nato_alpha()