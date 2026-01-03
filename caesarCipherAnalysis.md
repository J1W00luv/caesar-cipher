# Caesar Encryption Program

## **Aim:** 
	To create an encryption program that will use the caesar cipher to encrypt a user message, shift key value is random every time (and only letters should be encrypted), and decrypt a user message with the key specified by the user. To understand how a message can be encrypted and decrypted.

## **Method:**
	1. Research preparation: Find out about different ciphers used.
	2. Pre-Coding: Write a pseudocode for the program.
	3. Code & Test: Write and test the working program.

## **Problems i had during the execution:**

| Problem | Description | Solution |
| ------- | ----------- | -------- |
| Pseudocode inefficiency | The check written in pseudocode was not an efficient way to write the code. (for every character in an array, if a character from user input is in the array, then loop to find its pos. in the array). | Instead of looping for every character in an array of chars straight away I used the “not in” check first to make sure the character is a cyrillic letter before finding its position. |
| Decryption Problems | The message couldn't be decrypted correctly unless it was done in the same program running. | I forgot to change the name of the shuffled array to the one using user's key and message was decrypted using the wrong key. I changed the array used for the decryption. |


## **Testing results:**
	**Encryption**
| Input for Encryption | Encrypted Output | Key Used |
| -------------------- | ---------------- | -------- |
| “Hello World!” | “Fcjjm Umpjb!” | 50 |
| “Hey123” | “vSm123” | 40 |

	**Decryption**
| Input for Decryption | Decrypted Output | Key Used |
| -------------------- | ---------------- | -------- |
| “Fcjjm Umpjb!” | “Hello World!” | 50 |
| “MN” | “Hi” | 31 |


## **Conclusion:**
	I have successfully written an encryption program that uses caesar cipher. It encrypts the message usign a randomly generated encryption key, and asks for one before decrypting the user's message. The testing showed that the program worked correctly. I have learned about encryption methods and practiced writing code.

## **Next steps:**
	My program could be improved by asking the user if they want the key to be randomly generated for encrytion or they want to enter one. Also use subroutines.



