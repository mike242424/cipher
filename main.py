alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print("Welcome to the cipher program.")

go_again = True

def encrypt(input, shift):
  cipher_message = ''
  for letter in input:
    old_index = alphabet.index(letter)
    new_index = (old_index + shift) % len(alphabet)
    cipher_message += alphabet[new_index]
  return cipher_message

def decrypt(input, shift):
  cipher_message = ''
  for letter in input:
    old_index = alphabet.index(letter)
    new_index = (old_index - shift) % len(alphabet)
    cipher_message += alphabet[new_index]
  return cipher_message

while(go_again == True):
  selection = input("Type 'encode' to encrypt or 'decode' to decrypt:\n")

  if(selection == 'encode'):
    message = input("Type your message:\n").lower()
    shift_number = int(input("Type the shift number:\n"))

    encrypted_message = encrypt(input = message, shift = shift_number)

    print(f"Here's the encoded result: {encrypted_message}")

    repeat = input("Type 'yes' if you want to go again. Otherwise type 'no.\n")

    if(repeat == 'no'):
      go_again = False
    elif(repeat == 'yes'):
      go_again = True
    else:
      print('Invalid answer.')
      go_again = False

  elif(selection == 'decode'):
    message = input("Type your message:\n")
    shift_number = int(input("Type the shift number:\n"))

    decrypted_message = decrypt(input = message, shift = shift_number)

    print(f"Here's the decoded result: {decrypted_message}")

    repeat = input("Type 'yes' if you want to go again. Otherwise type 'no.\n")

    if(repeat == 'no'):
      go_again = False
    elif(repeat == 'yes'):
      go_again = True
    else:
      print('Invalid answer.')
      go_again = False

  else:
    print('Invalid input')