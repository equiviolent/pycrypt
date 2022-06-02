message = "Know the Ropes"
encryption = ""

i = len(message) - 1

while (i >=  0):
    encryption += message[i]
    i -= 1
print("The encrypted message is : ", encryption)

decryption = ""

j = len(encryption) - 1

while (j >= 0):
    decryption += encryption[j]
    j -= 1
print("The decrypted message is : ", decryption)
