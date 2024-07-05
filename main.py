import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print("Welcome to....")
print(logo.logo)
go_again = True

def ceasar(input, shift, type):
  cipher_message = ''
  for letter in input:
    if(letter in alphabet):
      old_index = alphabet.index(letter)
      if(type == 'encode'):
        new_index = (old_index + shift) % len(alphabet)
      elif(type == 'decode'):
        new_index = (old_index - shift) % len(alphabet)
      cipher_message += alphabet[new_index]
  else:
    cipher_message += letter
  return cipher_message

while(go_again == True):
  selection = input("Type 'encode' to encrypt or 'decode' to decrypt:\n")

  message = input("Type your message:\n").lower()
  shift_number = int(input("Type the shift number:\n"))
  cipher_message = ''

  if(selection == 'encode'):
    cipher_message = ceasar(input = message, shift = shift_number, type = 'encode')
    print(f"Here's the encoded result: {cipher_message}")
  elif(selection == 'decode'):
    cipher_message = ceasar(input = message, shift = shift_number, type = "decode")
    print(f"Here's the decoded result: {cipher_message}")
  else:
    print('Invalid input')

  repeat = input("Type 'yes' if you want to go again. Otherwise type 'no.\n")

  if(repeat == 'no'):
    go_again = False
  elif(repeat == 'yes'):
    go_again = True
  else:
    print('Invalid answer.')
    go_again = False

