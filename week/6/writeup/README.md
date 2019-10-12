# Writeup 6 - Binaries I

Name: Cooper Willetts
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: Cooper Willetts

## Assignment Writeup

### Part 1 (50 pts)

Flag  = CMSC389R-{di5a55_0r_d13}

### Part 2 (50 pts)

There were various methods as to how we provided to the program. The first and most obvious ways was through command line arguments. Another method that was utilized for reading data was the utilization of environmental variables. Finally, the last method of input to the program was file input. 
The first check that took place was check 1 which dealt with the checking the input from the user and comparing it to the string 'Oh God'. The second check that took place was the check dealing with the environmental variable. Within this check it compared the string entered backwards compared to our compared input, thus when the check wanted us to get the string 'seye ym' we needed to enter 'my eyes' into the proper environmental variable 'FOOBAR'. The final check had to do with file input. In the case we needed to create the file 'sesame' and enter the proper data into it. We were able to tell what needed to be entered into the file by finding the ascii values of each char being compared. After we looked at all the values we were left with the string ' they burn', which we needed to add into the sesame file. All the checks used a type of char comparison for each letter of the input comparing the input char to the char of the desired string. The checks differed by checks 1 and 2 used loops, while check 3 utilized just a bunch of if statements. 
I am pretty sure that the flag was stored in memory as a 32-bit integer. I have come to this conclusion based on the fact that within the update flag method, the registers are dealing solely with dword, which is a 32 bit integer representation. The flag being stored as a type of integer also makes sense for as to why it did not reveal itself when I tried to use strings crackme. The flag was being stored within the base pointer, so when we went to actually print it, we printed the 32 bit integer representation of the flag, which printed as our desired flag. 

Final input to obtain the flag was:
$$: export FOOBAR=" my eyes" 
$$: touch sesame
$$: echo " they burn" >> sesame
$$: ./crackme "Oh God" 