encrypt_tab = "qwertyuiopasdfghjklzxcvbnm1234567890"
decrypt_tab = "dsapoiuytrewq0987654321mnbvcxzlkjhgf"

while True:
    choice = input("1. Encrypt your message \n2. Decrypt your message \n3. Exit\n")
    if choice == "1":
        # encrypt
        message = str(input("Enter the message to encrypt:\n")).lower()
        message_encrypt = str.maketrans(encrypt_tab, decrypt_tab)
        print(message.translate(message_encrypt))
    elif choice == "2":
        # decrypt
        message = str(input("Enter the message to decrypt:\n")).lower()
        message_decrypt = str.maketrans(decrypt_tab, encrypt_tab)
        print(message.translate(message_decrypt))
    elif choice == "3":
        # exit
        break
    else:
        print("Wrong input. Choose again.")

