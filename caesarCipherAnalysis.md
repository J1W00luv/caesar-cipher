# Title: Caesar Encryption Program

## **Aim:** 
	To create an encryption program that will use the caesar cipher to encrypt a user message, shift key value is random every time (and only letters should be encrypted). To understand how a message can be encrypted and decrypted.

## **Method:**
	1. Research preparation: Find out about different ciphers used.
	2. Pre-Coding: Write a pseudocode for the program.
	3. Code & Test: Write and test the working program.

## **Problems i had during the execution:**

| Problem | Description | Solution |
| ------- | ----------- | -------- |
| Pseudocode inefficiency | The check written in pseudocode was not an efficient way to write the code. (for every character in an array, if a character from user input is in the array, then loop to find its pos. in the array). | Instead of looping for every character in an array of chars straight away I used the “not in” check first to make sure the character is a cyrillic letter before finding its position. |



## **Testing results:**
	
| Input for Encryption | Encrypted Output | Input for Decryption | Decrypted Output |
| -------------------- | ---------------- | -------------------- | ---------------- |
| “Hello World!” | “TqxxA iADxp!” | “TqxxA iADxp!” | “Hello World!” |
| “Hey123” | “MjD123” | “MjD123” | “Hey123” |


## **Conclusion:**
	I have successfully written an encryption program that uses caesar cipher. The testing showed that the program worked correctly. I have learned about encryption methods and practiced writing code.

## **Next steps:**
	My program could be improved by printing to the user the key that was used to encrypt data, and asking for the key when decrypting the message.
