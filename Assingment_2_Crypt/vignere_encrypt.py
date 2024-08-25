f = open("plaintext.txt", "r") #you do not have plaintext.txt
lines = f.readlines()
plaintext = lines[0].strip()
f.close()

key = "thisisnottherealkey"

def add_letter(a, b):
    num1 = ord(a.upper()) - 65
    num2 = ord(b.upper()) - 65
    summ = (num1 + num2) % 26 + 65
    return(chr(summ))
    
ciphertext = ""
key_index = 0
for i in range(len(plaintext)):
    num = ord(plaintext[i])
    if ((num >= 65 and num < 91) or (num >= 97 and num < 123)):
        ciphertext += add_letter(plaintext[i], key[key_index])
        key_index = (key_index + 1) % len(key)

f = open("vignere.txt", "w")
f.write(ciphertext)
f.close()
