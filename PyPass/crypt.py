
## Cryptp Algorithm

def encryption(message, n):
    ret = ""

    for i in range(len(message)):
        char = message[i]
        if not (char.isalpha()):
            ret += char
        elif (char.isupper()):
            # 65 is A in ascii
            ret += chr((ord(char) + n))
        else:
            # 97 is a in ascii
            ret += chr((ord(char) + n))

    return ret

def decryption(message, n):
    ret = ""

    for i in range(len(message)):
        char = message[i]
        if not (char.isalpha()):
            ret += char
        elif (char.isupper()):
            # 65 is A in ascii
            ret += chr((ord(char) - n))
        else:
            # 97 is a in ascii
            ret += chr((ord(char) - n))

    return ret
