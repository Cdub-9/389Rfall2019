# Writeup 10 - Crypto I

Name: Cooper Willetts 
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: Cooper Willetts 


## Assignment details

### Part 1 (45 Pts)
1 - Structure - The structure of the ledger file is 16 bytes of hash to begin the file, then proceeding it are the information ledger information. 
2 - Crypto - Md5 hash, aes128 encrpy and decrypt 
3 - Info from Ledger - Binary file of random values, not super long
4 - Confidentiality - Ensures confidentiality by storing the data within a binary file that is very hard to decrypt. THe encryption key is derived by taking a password, hashing it, then taking the first 2 bytes of the hash, and hashing it again. Then comparing this to the first 16 bytes of the .bin file. 
5 - Integrity - Program ensures integrity by checked that the ciphertext from the file matches an expected hash.
6 - Authenticity - Ensures that only people with the correct key can view the file. 
7 - Vector -  The initialization vector is generated via user input, hashed, then the first 2 bytes of the hash are hashed again and this result is stored within a struct parameter. 
### Part 2 (45 Pts)
See the crack file 

### Part 3 (10 Pts)
I believe that the ideal balance within a system lies somewhere closer to ideologies like Kerckoff's Principle. The longer a system is in place, the more people will learn about it and understand it, which guarantees over time that the obsurity of the system will be broken down. For example, if we are aware 2 parties are using a symmetric key system to contact each other, we cannot do anything about it even though there is not obsurity left in the system. If our system were to solely rely on obsurity, over time it will be eventually be broken, but if there is obsurity and ideas of Kerckoffs principle implemented within the algorithm, it will be the most secure. 
