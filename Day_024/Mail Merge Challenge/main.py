#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("Input/Names/invited_names.txt") as name_list:
    for name in name_list:
        with open("Input/Letters/starting_letter.txt") as letter:
            letter = letter.read()
            letter = letter.replace("[name]", name.strip())
            with open(f"Output/ReadyToSend/letter_for_{name.strip()}.txt", mode="w") as completed_letter:
                completed_letter.write(letter)
