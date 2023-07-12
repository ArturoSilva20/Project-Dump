//alpha thread function prints all words starting with an alphabet
//numeric thread function should print all words starting with a number
//main should not print
#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <iostream>
#include <sys/types.h>
#include <unistd.h>
#include <ctype.h>

int x = 0;
void *numeric(void * arg){
  char*message;
  message = (char*)arg;
  printf("numeric: %s\n", message);
  return NULL;
  pthread_exit(0);
}
void *alpha(void * arg){
  char*message;
  message = (char*)arg;
  printf("alpha: %s\n", message);
  return NULL;
  pthread_exit(0);
}
int main(int argc, char const *argv[]) {

  char input = 's';
  pthread_t alphabet;
  pthread_t numerical;



  for (int i = 0; i < argc-1; i++ ) {
    if (isalpha(*argv[i+1])){
        pthread_create(&alphabet, NULL, alpha, (void*)argv[i+1]);
    } else pthread_create(&numerical, NULL, numeric, (void*)argv[i+1]);
  }

  pthread_join(numerical, NULL);
  pthread_join(alphabet, NULL);


  exit(0);
}
