# CA4005 Assignment 1 - Symmetric File Encryption Using Password and Salt

The aim of this assignment is to perform symmetric encryption of a file using the block cipher AES where the key is derived from a password and a salt.

The password you use should be encoded using UTF-8 and be considered to be "strong". The salt will be a randomly generated 128-bit value. The password (p) and salt (s) will be concatenated together (p||s) and hashed 200 times using SHA-256. The resulting digest (H200(p||s)) will then be used as your 256-bit AES key (k).

You will then encrypt an input binary file using AES in CBC mode with the 256-bit key k and a block size of 128-bits. The IV for this encryption (i) will be a randomly generated 128-bit value. You will use the following padding scheme (as given in the notes): if the final part of the message is less than the block size, append a 1-bit and fill the rest of the block with 0-bits; if the final part of the message is equal to the block size, then create an extra block starting with a 1-bit and fill the rest of the block with 0-bits.

You will then encrypt your password using RSA with the encryption exponent (e) and my public modulus (N). This is done by calculating pe (mod N). This will use your own implementation of modular exponentiation rather than a library method for this purpose. For the purpose of this assignment no padding should be added to the password before encryption (although this would normally be done).

The encryption exponent (e) is 65537 and my public modulus (N) has the following value (in hexadecimal):

`c406136c 12640a66 5900a9df 4df63a84 fc855927 b729a3a1 06fb3f37 9e8e4190`  
`ebba442f 67b93402 e535b18a 5777e649 0e67dbee 954bb021 75e43b64 81e7563d`  
`3f9ff338 f07950d1 553ee6c3 43d3f814 8f71b4d2 df8da7ef b39f846a c07c8652`  
`01fbb35e a4d71dc5 f858d9d4 1aaa856d 50dc2d27 32582f80 e7d38c32 aba87ba9`

The implementation language must be Java. Your program must implement the interface Assignment1Interface provided and should take an additional filename in the command line and output to standard output the result of encrypting this file. The input binary file will be the Java class file resulting from compiling your program.

You will have to make use of the BigInteger class (java.math.BigInteger), the security libraries (java.security.\*) and the crypto libraries (javax.crypto.\*). You must not make use of the methods provided by the BigInteger class to implement the modular exponentiation; all modular exponentiation must be done using one of the two square and multiply algorithms described in the motes (left-to-right method or right-to-left method). You can however make use of the crypto libraries to perform the AES encryption and the SHA-256 hashing.

Once your implementation is complete, you should create a zip file called Assignment1.zip that contains the following files:

- Salt.txt - your 128-bit salt value (s) in hexadecimal (32 hex digits with no white space).
- IV.txt - your 128-bit IV (i) in hexadecimal (32 hex digits with no white space).
- Password.txt - your password (p) encrypted using RSA as described above in hexadecimal.
- Assignment1.java - your program code file.
- Assignment1.class - the result of compiling the above code file, which was encrypted.
- Encryption.txt - the AES encryption of the above class file produced using: "java Assignment1 Assignment1.class > Encryption.txt" (in hexadecimal with no white space).
- A declaration that this is solely your own work (except elements that are explicitly attributed to another source).

When I receive your submission on Loop I will decrypt your password p using my RSA private key. Using this password and your salt s I will then generate your AES key k using SHA-256. I will decrypt the AES ciphertext using your AES key and IV, which should match the submitted Java class file for a correct submission.

This assignment is due **10am on Monday 1st November 2021. Submissions without the declaration will not be assessed. This assignment carries 15 marks and late submissions will have 1.5 marks deducted for each 24 hours the assignment is overdue.**

The following are some common mistakes you should avoid on this assignment:

1. Not converting the password into corresponding bytes using UTF-8 encoding. 

2. Not concatenating the bytes for the password and salt correctly e.g. adding BigIntegers, concatenating them in the wrong order, etc.

3. Hashing the password the wrong number of times.

4. Converting BigInteger values to an array of bytes incorrectly - note that the BigInteger method toByteArray() uses a twos complement representation and may add an extra leading zero-valued byte if the first bit is set. 

5. Padding incorrectly: none of the padding mechanisms provided by the Java libraries corresponds to the required padding; you will need to use the NoPadding option and implement the padding yourself.

6. Padding with the characters ‘0’ and '1' rather than the bit values 1 and 0..

7. Giving decimal values rather than hexadecimal.

8. Giving negative hex values.
