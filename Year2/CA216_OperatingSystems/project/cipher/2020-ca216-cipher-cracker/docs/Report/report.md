
# Cracking the Substitution Cipher - (CA216 Operating Systems)
##### Name: _**Vincent Achukwu**_
##### Student Number: _**17393546**_
#
#
#
## Introduction
The objective of this assignment is to decrypt files containing messages using Caesar Cipher or Substitution Cipher. As this module mainly deals with processes and threads, the ciphertext must be cracked as fast as possible with the use of threads, processes, etc.

Below, I will explain my approach to tackling this problem for each cipher crack method. In this report, I go through the substitution cipher program, after which in the end I briefly describe how the Caesar cipher code works. I will explain the results of the tests for decrypting the files provided to us. Below, I describe how I made the multiprocessing version of the program, as this was the fastest version of the Substitution Cipher programs.


## Substitution Cipher
##### How to run code
The code can be run in the command line as follows (in the src directory):
```python3 subCipherMultiprocessing.py ENCRYPTED-FILE.TXT``` where the text file is an encrypted file stored in the Substitution cipher directory.
When specifying the encrypted file, it's path will be joined when you run it, as the path is specified at the top of my program. Example, for "russell-cipher.txt":
```bash
python3 subCipherMultiprocessing.py russell-cipher.txt
```
should work, instead of you specifying the directory since russell-cipher.txt is joined to its directory when you run it.
##### Approach:
My approach to figure out how to encrypt/decrypt text was by starting with a string. I then researched about Substitution Ciphers. A Substitution Cipher is more complicated than Caesar Cipher since it has 26! possible keys. Caesar cipher allows for the brute force approach, but clearly, this isn't the case for the Substitution Cipher approach.
The most common method used to decrypt text is using frequency analysis. In English, there are groups of letters or words which may appear more often than others. The most common English letters are "e", "t", "a", "o", "i" and so on. This approach allows for decrypting the text using frequency analysis of the encrypted text and matching the letters to the English letters based on most to least frequent. However, this method mostly works when the encrypted text is very long for the probabilities to match up. I didn't get great results using a small set of texts but got some better results from a longer text. Mapping letter frequencies of encrypted text to English letters didn't seem to be the best option.

At first, I tested the code, using different keys with different sample text (hardcoding the key), and it worked out fairly well. My next step was to make the program read text from a file, encrypting it and decrypting it back (again by knowing/hardcoding the key first). I got that working using the files you provided, and some other texts, copying and pasting from the file I'm reading from. I then had to plan how to generate a key, given the encrypted text. I used a [site](https://cryptii.com/pipes/alphabetical-substitution "site") as a guide for me to compare the expected result with mine. On the [site](https://cryptii.com/pipes/alphabetical-substitution "site"), you can alter the key, the plain text, and it would encrypt it and also decrypt. What I did was copied and pasted the encrypted text for testing. But again, I didn't get great results by mapping frequencies.
I came across this [article](http://practicalcryptography.com/cryptanalysis/stochastic-searching/cryptanalysis-simple-substitution-cipher/ "article") during my research. In the [article](http://practicalcryptography.com/cryptanalysis/stochastic-searching/cryptanalysis-simple-substitution-cipher/ "article"), it describes [stochastic searching](https://www.geeksforgeeks.org/introduction-hill-climbing-artificial-intelligence/ "stochastic searching") (or hill-climbing algorithm). For this to work, we need a way to check how similar a piece of text is to English using a fitness measure or rating. If a piece of text is very similar to English, it gets a high score (or high fitness) while jumbled text will receive a low score.

We use a fitness measure based on the quadgrams statistics, which can be deduced using large texts like books. This is provided by the article already, hence I used their [stats](http://practicalcryptography.com/cryptanalysis/letter-frequencies-various-languages/english-letter-frequencies/ "stats") (which is also provided in tests directory).

Some of the stats of the quadgrams are quite small, so using the log of the quadgrams of English text and multiplying each of the quadgrams probabilities, we can get the probability of it being English, i.e it's fitness. Since multiplying small probabilities can lead to numeric underflow in floating-point numbers, the logarithm of each probability is taken.
Example, the total probability the text "Easter" is english is
```log(p("Easter")) = log(p("East")) + log(p("aste")) + log(p("ster"))```
which is used as the fitness of the decrypted text.

I refactored the code to use Object Oriented Programming to make it more structured. The main method starts the timer to time the code. The quadgrams stats are loaded from the tests directory and the path is joined to the quadgrams file. I also inserted the path of the ngram code to be able to import it, since it is not in the src/Version-for-grading directory. I then load the quadgrams stats using the ngram score method to store the data in a dictionary.
Next, I create an instance of the class and pass in a multiprocessing queue to it.
```python
ss = SubCipher(q)
```
The cipher file is loaded via ```ss.loadfile(subCipher_dir)``` in the class, which passes in the ```subCipher_dir``` as its arguments. ```subCipher_dir``` is specified at the top of the program, which is joined via ```os.path.join(subCipher_dir, sys.argv[1])```. So when you run the program, you can simply specify the text file itself.
After the program is executed, the execution time is printed, as well as where the decrypted file and the key were written (in this case, the Substitution Cipher directory).


##### Testing:
I use the time module to time the code, starting and ending the time at the beginning and end of the main method respectively.
At first, I did not use threading or processing and simply allowed the program to run as a single thread. Later, after refactoring, I implemented multithreading and multiprocessing

The results of testing the sample encrypted text you provided is below:

| | Single-threaded | Multi-threaded | Multi-processed |
|----------|-----------------|----------------|-----------------|
|two-cities| 19 | 24 | 12 |
|russell | 8 | 11 | 7 |

#### Analysis
Based on these stats, multiprocessing was the fastest on average. The time taken is never the same due to the way the algorithm finds the key via the hill-climbing approach. I calculated the average by running the programs 10 times. Also, the program stops after 20 iterations if a better key was not found. This also allows for the program to end execution and not run infinitely. My machine has 4 cores, hence 4 processes were running and testing the keys. Context switching time and other processes are some contributing factors that may make multiprocessing a little slower at times. If I'm correct, the processes are CPU bound as they depend on the CPU to run, hence they sped up these processes. CPU bound tasks are programs that spend most of their time performing calculations in the CPU (mathematical computations, image processing, etc). If the calculations can be performed independently of each other, we can split them up among the available CPU cores, therefore, gaining a significant boost to processing speed.
Multithreading was slower here due to the fact it runs on the one core and in shared memory space.

I also used another text file I downloaded from Gutenberg using the book [sherlock holmes](https://www.gutenberg.org/files/1661/1661-h/1661-h.htm#chap06 "sherlock holmes"). However, the program took a while to run and I couldn't record the results for it (other than the fact that the CPU was being consumed). I did manage to run it with Caesar Cipher.

#### Conclusion
I didn't expect the multiprocessing and single-threaded program to almost be the same in execution time, but I think the reason is because of the way I implemented multi-processing.

#### Additional comments (Caesar Cipher)
For Caesar cipher, the tests are as follows:
| | Single-threaded | Multi-threaded | Multi-processed |
|----------|-----------------|----------------|-----------------|
|two-cities| 0.1 | 0.15 | 2.14 |
|sherlock | 0.16 | 1.2 | error |

Based on these stats, allowing the program to run without the use of multithreading or multiprocessing was faster, and multiprocessing was a lot slower. This is because the processing involves context-switch, which takes longer than threading. There is more overhead involved with multiprocessing, thus making it slower as a result. I got an error with the large text file (sherlock) using multiprocessing with Caesar cipher because of an OS error.
```bash
OSError: too many open files
```
I believe this was the case because of how I implemented multiprocessing and multithreading by decrypting word by word of the encrypted text. (To test sherlock_caesar.txt, you can move it to the ```files/caesar-cipher``` directory)

I believe multithreading should've been faster. Maybe I should've done the threading for each sentence instead of each word, or better yet, shift the whole string in one go. This may have made it faster, but it may or may not be the best approach.

#### What I'd do differently:
1. Substitution Cipher:
    * have better-structured code
    * use locks/mutexes
    * use frequency analysis approach more accurately
1. Caesar Cipher:
    * check every word in the first line of the encrypted file.
    * have better-structured code
    * use locks
    * have better multithreading/processing method
    * better key finding method

#### Sources
* _Online cipher solver_: https://cryptii.com/pipes/alphabetical-substitution
* _Stochastic Search Article_: http://practicalcryptography.com/cryptanalysis/stochastic-searching/cryptanalysis-simple-substitution-cipher/
* _Geeksforgeeks Hill-climbing Algorithm_: https://www.geeksforgeeks.org/introduction-hill-climbing-artificial-intelligence/
* _Hill-climbing video_: https://youtu.be/oSdPmxRCWws