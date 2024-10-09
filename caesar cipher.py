def encrypt(text, shift):
   
    encrypted_message = ""
    for char in text:
        if char.isalpha(): 
            shift_amount = shift % 26
            base = ord('a') if char.islower() else ord('A')
            encrypted_char = chr((ord(char) - base + shift_amount) % 26 + base)
            encrypted_message += encrypted_char
        else:
            encrypted_message += char  
    return encrypted_message

def decrypt(text, shift):
   
    return encrypt(text, -shift)

def main():
    print("Encryption/Decryption")
    
    while True:
        action = input("Would you like to encrypt or decrypt a message? (Enter 'enc' or 'dec'): ").strip().lower()
        if action not in ['enc', 'dec']:
            print("Invalid choice. Please enter 'enc' or 'dec'.")
            continue
        
        message = input("Enter the message: ")
        shift = int(input("Enter the shift value: "))
        
        if action == 'enc':
            result = encrypt(message, shift)
            print(f"Encrypted message: {result}")
        elif action == 'dec':
            result = decrypt(message, shift)
            print(f"Decrypted message: {result}")
        
        another = input("Would you like to perform another operation? (yes/no): ").strip().lower()
        if another != 'yes':
            break

if __name__ == "__main__":
    main()
