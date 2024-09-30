def encrypt_text(plaintext, n):
    ans = ""
    # iterate over the given text
    for i in range(len(plaintext)):
        ch = plaintext[i]
        
        if ch == " ":
            ans += " "
        elif ch.isupper():
            ans += chr((ord(ch) + n - 65) % 26 + 65)
        else:
            ans += chr((ord(ch) + n - 97) % 26 + 97)
    
    return ans

plaintext = input('Enter text to encrypt: ')
n = int(input('Enter Shift: ')) #Left Shift
print("Plain Text is: ", plaintext)
print("Shift pattern is: ", n)
print("Cipher Text is: ", encrypt_text(plaintext, n))
