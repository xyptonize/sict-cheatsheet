#!/usr/bin/env python3
from caesar import getKey, getTranslatedMessage
from freq import char_frequency, xmod26

if __name__ == '__main__':

    # 3 caesar.py кодыг инпорт файлаар оруулж текст файлыг шифрлэж шинэ файл үүсгэх код бичих.
    with open("plaintext.txt", 'r') as f:
        plaintext = f.read()
    print("Plain text : ")
    print(plaintext,"\n\n\n")
    # 4 ASCII текст файл шифрлэх.
    cipher_text = getTranslatedMessage('e', plaintext, xmod26(getKey()))

    with open("ciphertext.txt", 'w') as f:
        f.write(cipher_text)

    print("Encrypted text : ")
    print(cipher_text,"\n\n\n")
    decryptedtext = getTranslatedMessage('d', cipher_text, xmod26(getKey()))
    with open("decryptedtext.txt", 'w') as f:
        f.write(decryptedtext)
    print("Decrypted text : ")
    print(decryptedtext,"\n\n\n")
    # 5. Текст файлын тэмдэгтийн давтамж магадлалыг ол
    frequency = char_frequency(plaintext)

    for i, j in frequency.items():
        print("{} character frequency {}".format(i, j,))

    for i, j in frequency.items():
        print("{} character probability {}/{}".format(i, j, len(plaintext)))