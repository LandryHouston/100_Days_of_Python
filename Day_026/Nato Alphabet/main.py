import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for index, row in df.iterrows()}

word = input("Enter a word: ").upper()

output_list = [phonetic_dict[letter] for letter in word]
print(' '.join(output_list))