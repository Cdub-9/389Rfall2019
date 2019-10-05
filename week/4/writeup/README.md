# Writeup 2 - Pentesting

Name: Cooper Willetts
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: Cooper Willetts

## Assignment Writeup

### Part 1 (45 pts)

1. Correct Flag - CMSC389R - {p1ng_as_a_$erv1c3}
2. Input used to obtain correct flag = '157.230.179.99 && cat home/flag.txt'
3. My thought process was to first play around with the server and various commands, valid and invalid. I looked up how the ping command worked as well as played around with it locally. I also read the wikipedia page and other online sources about how exactly various forms of command injection attacks work, and how to possible implement them on Eric's Server. My idea is that I essentially needed to 'overwhelm' or trick the server into giving me information I wanted, without the server breaking or realizing my acts. I found that if you add '&&' onto the ip address given, the shell will also execute the function given after &&. After I was able to figure out this vulnerability, I had full access to the root directory of the server. From there, I began searching around in some of the directories, attempting to locate the flag. I was able to concatenate a couple of commands and land on the command of '157.230.179.99 && cat home/flag.txt' which brought me the desired flag.
4. One suggestion Eric could implement in the server is adding some type of string manipulation so that the server only receives an IP and nothing else. In addition to this, Eric should read up about various types of command injection attacks and possible ways to avoid them. 


### Part 2 (55 pts)

I was able to develop code that utilizes the vulnerability we found in part 1 to create a working shell on the host server. I was able to do this by utilizing raw_input command within python, which would prompt the user for input, then append this input onto the the back of the IP address ping to the server. Essentially, each new input from the user creates a new ping request with the server, executing the new command entered. The server kicks the user out if you are present for more than 8 seconds, so the way around this is to just create a new connection each time a new command is entered. The only real issue I had with developing the shell was the implementation of 'cd'. This command relies on the fact that we know our previous directory, but since each time we are inputting a command, we are reconnecting to the server, we cannot save this command. My attempt around this was to just save all commands entered by the user, and if one of the commands entered was 'cd' then append the previous cd command onto the newly typed command. This method is not perfect, but it does work good enough to do basic exploration of the server. 
The next difficult of the assignment was figuring out how to 'pull' files from the server onto the host machine. After lots of searching for a magic linux command I could use to download files locally, I opted to go a different approach. My approach was to open the desired file with cat, save the output, then write to the new file using pythons IO. (I am unsure if for the second arg we are suppose to supply a directory or a file name, so I implemented it as file name EX. pull home/flag.txt ./myLocalFlag.txt)
