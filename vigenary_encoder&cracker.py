import string
from collections import Counter

def vigenere_encrypt(plaintext, keyword):
    encrypted_text = []
    keyword_repeated = (keyword * (len(plaintext) // len(keyword))) + keyword[:len(plaintext) % len(keyword)]

    for p, k in zip(plaintext, keyword_repeated):
        if p.isalpha():
            shift = ord(k.lower()) - ord('a')
            if p.isupper():
                encrypted_text.append(chr((ord(p) - ord('A') + shift) % 26 + ord('A')))
            else:
                encrypted_text.append(chr((ord(p) - ord('a') + shift) % 26 + ord('a')))
        else:
            encrypted_text.append(p)  # Non-alphabet characters remain unchanged

    return ''.join(encrypted_text)

def vigenere_decrypt(ciphertext, keyword):
    decrypted_text = []
    keyword_repeated = (keyword * (len(ciphertext) // len(keyword))) + keyword[:len(ciphertext) % len(keyword)]

    for c, k in zip(ciphertext, keyword_repeated):
        if c.isalpha():
            shift = ord(k.lower()) - ord('a')
            if c.isupper():
                decrypted_text.append(chr((ord(c) - ord('A') - shift) % 26 + ord('A')))
            else:
                decrypted_text.append(chr((ord(c) - ord('a') - shift) % 26 + ord('a')))
        else:
            decrypted_text.append(c)

    return ''.join(decrypted_text)

def frequency_analysis(text):
    frequencies = Counter(filter(str.isalpha, text.lower()))
    total_letters = sum(frequencies.values())
    frequency_list = {letter: (count / total_letters) for letter, count in frequencies.items()}
    return frequency_list

def index_of_coincidence(ciphertext):
    frequencies = Counter(filter(str.isalpha, ciphertext.lower()))
    n = sum(frequencies.values())
    if n <= 1:
        return 0
    ic = sum(count * (count - 1) for count in frequencies.values())
    return ic / (n * (n - 1))

def guess_key_length(ciphertext):
    likely_lengths = []
    for key_length in range(1, 21):
        chunks = ['' for _ in range(key_length)]
        for i, char in enumerate(ciphertext):
            if char.isalpha():
                chunks[i % key_length] += char
        
        avg_ic = sum(index_of_coincidence(chunk) for chunk in chunks) / key_length
        likely_lengths.append((key_length, avg_ic))

    likely_lengths.sort(key=lambda x: x[1], reverse=True)
    return likely_lengths[0][0]  # Return the most likely key length

def deduce_key(ciphertext, key_length):
    chunks = ['' for _ in range(key_length)]
    for i, char in enumerate(ciphertext):
        if char.isalpha():
            chunks[i % key_length] += char

    key = ''
    english_freq_order = 'etaoinshrdlcumwfgypbvkjxqz'  # Common letter frequency in English
    for chunk in chunks:
        freq = frequency_analysis(chunk)
        # Get the letter most common in the chunk
        most_common_letter = max(freq, key=freq.get)
        # Calculate the shift assuming most common letter corresponds to 'e'
        shift = (ord(most_common_letter) - ord('e')) % 26
        key += chr(shift + ord('a'))

    return key

def crack_vigenere(ciphertext):
    key_length = guess_key_length(ciphertext)
    print(f"Guessed key length: {key_length}")
    
    guessed_key = deduce_key(ciphertext, key_length)
    print(f'Deduced key: {guessed_key}')
    
    decrypted_text = vigenere_decrypt(ciphertext, guessed_key)
    return decrypted_text

def main():
    choice = input("Do you want to encrypt (E) or decrypt (D)? ").strip().upper()

    if choice == 'E':
        plaintext = input("Enter plaintext: ")
        keyword = input("Enter keyword: ")
        encrypted_text = vigenere_encrypt(plaintext, keyword)
        print(f'Encrypted text: {encrypted_text}')
    
    elif choice == 'D':
        ciphertext = input("Enter ciphertext: ")
        keyword = input("Enter the key: ")
        decrypted_text = vigenere_decrypt(ciphertext, keyword)
        print(f'Decrypted text: {decrypted_text}')
    
    else:
        print("Invalid choice. Please choose 'E' for encrypt or 'D' for decrypt.")

if __name__ == '__main__':
    main()
