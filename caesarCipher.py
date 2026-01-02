# Caesar Cipher Program
import string
import random

# 1 create an array of characters
chars = string.ascii_letters
chars = list(chars)

# 2 copy the array and move it by no. of chars
shuffledArray = chars.copy()
num = random.randint(0, 52)

firstHalf = shuffledArray[:num]
secondHalf = shuffledArray[num:]

shuffledArray = secondHalf + firstHalf

# 3 get user input and encrypt it
userInput = input("Enter your message: ")
encryptedMessage = ["" for x in range(len(userInput))]

for x in range(len(userInput)):
    if userInput[x] not in chars:
        encryptedMessage[x] = userInput[x]
    else:
        for y in range(len(chars)):
            if userInput[x] == chars[y]:
                encryptedMessage[x] = shuffledArray[y]

# 4 display the result
encryptedMessage = ''.join(encryptedMessage)
print(encryptedMessage)

# 5 get user input and decrypt it
userInput = input("Enter your encrypted message: ")
decryptedMessage = ["" for x in range(len(userInput))]

for x in range(len(userInput)):
    for y in range(len(chars)):
        if userInput[x] == shuffledArray[y]:
            decryptedMessage[x] = chars[y]
    if userInput[x] not in shuffledArray:
        decryptedMessage[x] = userInput[x]

# 6 display the result
decryptedMessage = ''.join(decryptedMessage)
print(decryptedMessage)