# Vigenère Cipher with support for multilingual characters, emojis, handling spaces/newlines, and input validation.

# Define alphabets including multilingual characters, emojis, English letters, numbers, and symbols
chinese_alphabet = "的一是了我不人在他有这个上们来到时大地为子中你说生国年就那和要她出也得里后自以会家可下而过天去能对小多然于心学之都好看起发工还"
japanese_alphabet = "あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをん"
korean_alphabet = "ㅂㅈㄷㄱㅅㅛㅕㅑㅐㅔㅂㅈㄷㄱㅅㅛㅕㅑㅐㅔㅂㅈㄷㄱㅅㅛㅕㅑㅐㅔㅂㅈㄷㄱㅅㅛㅕㅑㅐㅔ"
russian_alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
ukrainian_alphabet = "абвгґдежзийклмнопрстуфхцчшщьюя"
emoji_alphabet = "😀😁😂🤣😃😄😅😆😉😊😋😎😍😘😗😙😚😜😝😛"
english_alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers_and_symbols = "0123456789?&@“$();:/-‘.,-/[]{}#%^*+=•¥£€><~|\\_ "

# Combine all alphabets into a single character set (including space)
all_alphabets = (
    chinese_alphabet + japanese_alphabet + korean_alphabet +
    russian_alphabet + ukrainian_alphabet + emoji_alphabet +
    english_alphabet + numbers_and_symbols
)

# Create dictionaries to map each character to an index and vice versa
char_to_index = {char: idx for idx, char in enumerate(all_alphabets)}
index_to_char = {idx: char for idx, char in enumerate(all_alphabets)}
alphabet_length = len(all_alphabets)

def validate_input(input_text: str) -> None:
    """Validates that all characters in input_text are part of the allowed alphabet."""
    for char in input_text:
        if char not in char_to_index:
            raise ValueError(f"Invalid character '{char}' in input. Only characters in the defined alphabet are allowed.")

def extend_key(message: str, key: str) -> str:
    """Extend the key to match the length of the message."""
    return (key * (len(message) // len(key))) + key[:len(message) % len(key)]

def vigenere_encrypt(message: str, key: str) -> str:
    """Encrypt the message using the Vigenère cipher, ignoring spaces/newlines."""
    # Validate inputs
    validate_input(message)
    validate_input(key)
    
    extended_key = extend_key(message, key)
    encrypted_message = []
    
    for i, char in enumerate(message):
        if char in char_to_index:
            if char in " \n":  # Keep spaces and newlines as-is
                encrypted_message.append(char)
            else:
                char_index = char_to_index[char]
                key_index = char_to_index[extended_key[i]]
                encrypted_index = (char_index + key_index) % alphabet_length
                encrypted_message.append(index_to_char[encrypted_index])
        else:
            encrypted_message.append(char)  # Add unknown characters as-is
    
    return ''.join(encrypted_message)

def vigenere_decrypt(encrypted_message: str, key: str) -> str:
    """Decrypt the message using the Vigenère cipher, ignoring spaces/newlines."""
    # Validate inputs
    validate_input(encrypted_message)
    validate_input(key)
    
    extended_key = extend_key(encrypted_message, key)
    decrypted_message = []
    
    for i, char in enumerate(encrypted_message):
        if char in char_to_index:
            if char in " \n":  # Keep spaces and newlines as-is
                decrypted_message.append(char)
            else:
                char_index = char_to_index[char]
                key_index = char_to_index[extended_key[i]]
                decrypted_index = (char_index - key_index) % alphabet_length
                decrypted_message.append(index_to_char[decrypted_index])
        else:
            decrypted_message.append(char)  # Add unknown characters as-is
    
    return ''.join(decrypted_message)