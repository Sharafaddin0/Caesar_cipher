# Greetings to the Caesar ciphor
print("Welcome to the Caesar ciphor!")

# Import logo and list of letters from art.py
from art import logo, alphabet
print(logo)

# Create encrypt functions that take "text" and "shift" as inputs
# def encrypt(plain_text, shift_amount):
#   cipher_text = ""
#   for letter in plain_text:
#     position = alphabet.index(letter)
#     new_position = position + shift_amount
#     cipher_text += alphabet[new_position]
#   print(f'Your encoded text is {cipher_text}')

# Create decrypt function that takes "text" and "shift" as inputs
# def decrypt(cipher_text, shift_amount):
#   plain_text = ""
#   for letter in cipher_text:
#     position = alphabet.index(letter)
#     new_position = position - shift_amount
#     plain_text += alphabet[new_position]
#   print(f'Your decoded text is {plain_text}')  

  
# Combination of encrypt and decrypt functions
def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for letter in start_text:
    # Fixing the code to keep the letter/spaces/number when the code is encoded/decoded
    if letter in alphabet:
      position = alphabet.index(letter)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      end_text += letter
  print(f'Here is {cipher_direction}d result: {end_text}')   
  
# Create the loop when user wants to continue to run the program. 
# If user wants to restart the cipher program
should_end = False
while not should_end:

  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  # Avoid the mistake when user enters larger shift amount than the number of letters in alphabet
  shift = shift % 26

  caesar(start_text = text, shift_amount = shift, cipher_direction = direction) 
  
  end = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if end == 'no':
    should_end = True
    print("Arrivederci! This is the end.")
