#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <sys/stat.h>
#include <stdlib.h>
#include <fcntl.h>
#include <openssl/rand.h>
#include <time.h>

#include "crypto.h"
#include "common.h"
#define SIZE 8 
#define LEDGER_FILE "ledger.bin"
#define PERMISSIONS (S_IRUSR | S_IWUSR)

int generator(){
	char buffer[SIZE+1];
	unsigned char fd_key_hash[16];
	char chars[128] = { 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',        	'J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','-',
	'%','&','a','b','c','d','e','f','g','h','i','l','m','n','o','p','q','r','s','t','u','v','w','x','y',
	'z'}; 
	chars[55] = 0; 

	int i;
	int fd;
	unsigned char *temp;
    	unsigned char *temp_hash;
	for(i=0; i < SIZE; i++){
		buffer[i] = chars[(rand() % 54)];
		//buffer[i] = 001;	
	}
	//printf("%s\n", buffer);
	temp = md5_hash(buffer, SIZE);
	memset(temp+2, 0, 14);
	temp_hash = md5_hash(temp, 2);
	fd = open(LEDGER_FILE, O_RDONLY, PERMISSIONS);
        read(fd, fd_key_hash, 16);
	//printf("testing hash of %s\n", temp_hash);
	if (memcmp(temp_hash, fd_key_hash, 16) == 0) {
            //printf("found the password\n");
	    printf("%s\n", buffer);
	    //printf("%x\n", buffer);
	    return 10; 
        }
	return 8;




}

int main(int argc, char **argv) {
	char buffer[SIZE+1];
	unsigned char fd_key_hash[16];
	int i;
	int fd;
	int tempnum = 0; 
	unsigned char *temp;
    	unsigned char *temp_hash;
	
	
	for(i=0; i < SIZE; i++){
		srand(i + time(0));
		buffer[i] = 'A' + (rand() % 126);
		//buffer[i] = 001;	
	}
	//printf("%s\n", buffer);
	temp = md5_hash(buffer, SIZE);
	memset(temp+2, 0, 14);
	temp_hash = md5_hash(temp, 2);
	fd = open(LEDGER_FILE, O_RDONLY, PERMISSIONS);
        read(fd, fd_key_hash, 16);
	
	//printf("the needed hash is %s\n", fd_key_hash);
	i = 0;
	while(tempnum!=10){
	i = i+1;
	srand(i + time(0)); 
	tempnum= generator();
	}
	
	
	
}





