from collections import Counter

# English letter frequency (approximate)
english_frequency = {
    'a': 0.08167, 'b': 0.01492, 'c': 0.02782, 'd': 0.04253,
    'e': 0.12702, 'f': 0.02228, 'g': 0.02015, 'h': 0.06094,
    'i': 0.06966, 'j': 0.00153, 'k': 0.00772, 'l': 0.04025,
    'm': 0.02406, 'n': 0.06749, 'o': 0.07507, 'p': 0.01929,
    'q': 0.00095, 'r': 0.05987, 's': 0.06327, 't': 0.09056,
    'u': 0.02758, 'v': 0.00978, 'w': 0.02360, 'x': 0.00150,
    'y': 0.01974, 'z': 0.00074
}

def caesar_decrypt(ciphertext, shift):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            shift_amount = shift % 26
            new_char = chr(((ord(char) - shift_amount - 65) % 26) + 65) if char.isupper() else \
                         chr(((ord(char) - shift_amount - 97) % 26) + 97)
            decrypted_text += new_char
        else:
            decrypted_text += char
    return decrypted_text

def score_text(text):
    text = text.lower()
    letter_counts = Counter(filter(str.isalpha, text))
    total_letters = sum(letter_counts.values())
    
    score = 0
    for letter, count in letter_counts.items():
        frequency = count / total_letters if total_letters > 0 else 0
        score += frequency * english_frequency.get(letter, 0)
    return score

def caesar_cracker(ciphertext):
    best_score = float('-inf')
    best_decryption = ""
    
    print("Attempting to crack the Caesar cipher...\n")
    
    for shift in range(1, 26):
        decrypted_text = caesar_decrypt(ciphertext, shift)
        text_score = score_text(decrypted_text)
        
        if text_score > best_score:
            best_score = text_score
            best_decryption = decrypted_text

    print(f"Best match with highest score: {best_score}")
    print(f"Decrypted text: {best_decryption}")

# Example usage
encrypted_message = input('Enter message to be decrypted:')
caesar_cracker(encrypted_message)
