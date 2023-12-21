# AES_Twilio-Notifications
File Encryption and Decryption with AES and Twilio Notifications
Code Logic:

Encryption:

Reads data from a file named 'plaintext.txt'.
Generates a random AES key of 16 bytes.
Creates an AES cipher in CBC mode with the generated key.
Encrypts the data, pads it using PKCS7 padding, and saves the initialization vector (IV) and ciphertext to 'ciphertext.bin'.
Saves the encryption key to 'key.bin'.
Twilio Notification (Encryption):
Uses Twilio to send a notification indicating that a file has been encrypted.

Decryption:

Reads the initialization vector and ciphertext from 'ciphertext.bin'.
Reads the encryption key from 'key.bin'.
Creates an AES cipher with the key and IV.
Decrypts the ciphertext, removes padding, and saves the decrypted data to 'decrypted.txt'.
Twilio Notification (Decryption):
Uses Twilio to send a notification indicating that the decryption of a file is complete.

The code demonstrates a file encryption process using AES in CBC mode, storing keys and IVs separately, and subsequently decrypting the file to recover the original data. Twilio is used for notifications indicating successful encryption and decryption processes.
