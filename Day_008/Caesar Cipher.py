alphabet = 'abcdefghijklmnopqrstuvwxyz'

print('''           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
''')

def cipher():
    while True:
        user_input = input("Type 'encode' to encrypt, type 'decode' to decrypt\n")
        message = input("Type your message:\n")
        shift_input = input("Type the shift number:\n")
        shift = int(shift_input) if shift_input else 0
        
        if not message:
            print("You did not enter a message.")
            cipher()
        if user_input == 'encode':
            print(f"Here's the encoded result: {"".join(alphabet[alphabet.index(letter) + shift] if letter in alphabet else letter for letter in message.lower())}")
        elif user_input == 'decode':
            print(f"Here's the decoded result: {"".join(alphabet[alphabet.index(letter) - shift] if letter in alphabet else letter for letter in message.lower())}")
        else:
            print("You did not specify encode or decode.")
            cipher()
        retry = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
        if retry == 'yes':
            cipher()
        else:
            print("Goodbye")
            return False
cipher()