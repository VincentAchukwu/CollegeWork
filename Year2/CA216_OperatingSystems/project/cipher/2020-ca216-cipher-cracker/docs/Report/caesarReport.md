# Cracking the Substitution Cipher - (CA216 Operating Systems)
## Introduction
The objective of this assignment is to decrypt files containing messages using Caesar Cipher or Substitution Cipher. As this module mainly deals with processes and threads, the ciphers must be cracked as fast as possible with the use of threads, processes, etc.

Below, I will explain my approach to tackling this problem for each cipher crack method. Then I will explain the results of the tests for decrypting the files provided to us. I will describe how I made the multithreaded version of the Caesar Cipher program, as this was the fastest version of the Caesar Cipher programs, and the fastest version of the substitution cipher program, which was multiprocessing.


## Caesar Cipher
##### How to run code
The code can be run in the command line as follows (in the src directory):
```python3 caesarCipher.py ENCRYPTED-FILE.TXT```
When specifying the encrypted file (provided it's located in the caesar-cipher directory), it's path will be joined when you run it, as the path is specified at the top of my program.
##### Approach:
My approach to figure out how to encrypt/decrypt text was by starting off with a string. I then researched about ciphers, in particular Caesar Cipher. I understood the workaround for the key and how it shifts the letters given a key. Once I got the encrypt method working, it was easy to get the decrypt method working, which simply does the opposite.
``` decryption formula --> (letterIndex + key) % len(alphabet)```
I tested the code, using different keys, and it worked out well. My next step was to read text from a file, encrypting it and decrypting it back (again by knowing/hardcoding the key first). I got that working using a Shakespeare poem, and some other texts, copying and pasting to the file I'm reading from. I then had to plan how to generate a key, given the encrypted text. I used a [site](https://cryptii.com/pipes/caesar-cipher "site") as a guide for me to compare the expected result with mine. On the [site](https://cryptii.com/pipes/caesar-cipher "site"), you can alter the key, the plain text, and it would encrypt it, and also decrypt. What I did was copied and pasted the encrypted text for testing.

##### Finding the shift key
So as I worked around how to generate the shift key given the encrypted text, I figured it out by using a for loop, where the iterator (going within the range of the length of the alphabet), it would decrypt the word using the current iterator of the loop (say "i") by shifting the encrypted word "i" places.
```python
for i in range(len(alphabet)):
    # test key...
    # if word in dictionary..return key..else loop
```
It then checks if that word is in the dictionary of English words (text file). If it is, then return that iterator, or specifically, that shift key. Else, the loop continues.
The reason I'm using the longest word of the first line of the encrypted text file is that it's guaranteed to be a proper word, unlike two or three letter words that would easily match, and the shift key would be returned which may be wrong.
Words like "ab", "no", "hi", "op", "so", etc or three-letter words may not be the actual word we're trying to get, and testing only the longest word helps find an actual word. However, I believe that this is a brute force approach by testing all possible shift keys until the right one.

Eventually, I decided to refactor my code using object-oriented programming, using classes and objects to make the code more structured and readable.
The main method creates an instance of the class caesarCipher() as cc.
```python
cc = caesarCipher()
```
It then reads the encrypted text file as a command-line argument and stores the contents of the file in a list, splitting it by the newline character.
In doing so, the program can then keep the format of the decrypted file content the same as the encrypted file content (i.e, if the encrypted file has newline characters or paragraphs, the decrypted file will look exactly the same, for output elegancy..).
The file is loaded from the caesar-cipher directory which is then joined via ```os.path.join() ```. The caesar-cipher directory is specified as a variable at the top of the program, as well as the directory where the dictionary is located (```caesar_dir``` and ```dict_dir``` respectively.)
Next, we call the key generator method to find the key. If the key doesn't return a None type, then we proceed, else we print that the key was invalid and the program ends. Once the key is found, the shift key is printed, and decryption takes place. I created a list called ```dec_list``` which will contain the decrypted version of the sentences. Multithreading process begins by looping through each  sentence in the cipher text list, in which another loop iterates each word in that sentence and decrypts it. The decrypt method appends the decrypted word to a temporary list, and after the loop finishes the threading, that list of words is then joined back to form the sentence in its decrypted form via ```" ".join(tmp_lst)``` and is appended to ```dec_list```.
It does this for each sentence and once multithreading finishes, I call the ``save_key_dec`` method in the ``caesarCipher`` class which writes the key and decrypted text to ```caesar_dir``` in their appropriate filenames. All decrypted text files and the key is written in the same file location as their corresponding encrypted text files.

##### Testing:
I use the time module to time the code, starting and ending the time at the beginning and end of the main method respectively.
At first, I did not use threading or processing and simply allowed the program to run as a single thread (no use of the threading or processing module). It was quite fast at doing so.

The results of testing the sample encrypted text you provided is below (as well as another text file I downloaded from gutenberg using the book [sherlock holmes](https://www.gutenberg.org/files/1661/1661-h/1661-h.htm#chap06 "sherlock holmes") ):

|          | Single-threaded | Multi-threaded | Multi-processed |
|----------|-----------------|----------------|-----------------|
|two-cities|       0.1       |      0.15      |      2.14       |
|sherlock  |       0.16      |      1.2       |      error      |

#### Analysis
Based on these stats, allowing the program to run without the use of multithreading or multiprocessing was faster, and multiprocessing was a lot slower. This is due to the fact that processing involves starting the process and context-switch, which takes longer than threading. There is more overhead involved with multiprocessing, thus making it slower as a result. 

#### Conclusion
I believe multithreading should've been faster, but I think the reason it wasn't is because of the way I implemented multi-threading, doing it word by word. Maybe I should've done the threading for each sentence instead of each word, or better yet, shift the whole string in one go. This may have made it faster, but it may or may not be the best approach.







Substitution Cipher:

<!-- SPECIFY HOW TO RUN THE PROGRAM FIRST -->



(Do differently:
    caesar:
        check every word in the first line of the encrypted file.
        have better-structured code
        use locks
        have better multithreading method
        better key finding method

)


################################                  👇                    ################################
################################                                        ################################
################################                                        ################################
################################   DO NOT FORGET TO REMOVE COLOURING    ################################
################################                                        ################################
################################                                        ################################
################################                  👆                    ################################
