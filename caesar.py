print("caesar algorithm")

# 3%26 ==>  3/26=0   0*26+3=3 

def caesar_cipher_Enc(text, key):
    result = ""
    
    # Traverse the text  loop in text for each char
    for i in range(len(text)):
        char = text[i]
        
        # Encrypt uppercase characters    65+3-65=3%26=3+65=68(D)
        if char.isupper():
            result += chr((ord(char) + key - 65) % 26 + 65)
        # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + key - 97) % 26 + 97)
        else:
            result +=''  # Non-alphabetic characters remain the same
    
    return result

def caesar_cipher_Dec(text, key):
    result = ""
    
    # Traverse the text  loop in text for each char
    for i in range(len(text)):
        char = text[i]
        
        # Encrypt uppercase characters   ascii of A --> 65     
        if char.isupper():
            result += chr((ord(char) - key - 65) % 26 + 65)
        # Encrypt lowercase characters  ascii of a --> 97
        elif char.islower():
            result += chr((ord(char) - key - 97) % 26 + 97)
        else:
            result += ''  # Non-alphabetic characters remain the same
    
    return result

# Example usage

while 1:
    
  ch=input("if you want encrept enter EN if you want decrypt enter DE ")

  if ch=="EN":
    plain=input("enter your plaintext :")
    text = "sa"
    key = int(input("enter key : "))
    encrypted_text = caesar_cipher_Enc(plain, key)
    print("Encrypted:", encrypted_text)


  elif ch=="DE":
     cipher=input("enter your ciphertext :")
     text = "sa"
     key = int(input("enter key : "))
     decrypted_text = caesar_cipher_Dec(cipher, key)
     print("decrypted:", decrypted_text)

  else :
    print("invalid input")