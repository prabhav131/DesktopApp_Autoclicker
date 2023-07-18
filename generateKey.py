from cryptography.fernet import Fernet

def generate():
    key = Fernet.generate_key()
    with open("universal.key","wb") as key_files:
        key_files.write(key)