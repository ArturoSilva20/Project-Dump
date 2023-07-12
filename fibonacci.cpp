/*
fib0 = 0
fib1 = 1
fibn = fibn-1 + fibn-2
*/

#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <vector>
#include <iostream>
#include <sys/types.h>
#include <unistd.h>
// enter numbers that the program will generate
// create thread that generates numbers
// numbers stored in global data structure std::vector<int> v;
//iterative when calculating
// parent will wait until child thread finishes

std::vector<int> sequence;

void *mythread(void *arg){

    int fibn, num = *((int *)arg);
    sequence.push_back(0);
    sequence.push_back(1);

    for (int i= 0; i< num; i++) {
      fibn = *(sequence.end()-1) + *(sequence.end()-2);
      sequence.push_back(fibn);
    }
   return NULL;
}


int main() {
  int num;
  std::cout<< "Enter: ";
  std::cin>> num;
  pthread_t t1;
  num -= 2;
  pthread_create(&t1, NULL, mythread, &num);
  pthread_join(t1,NULL);

  for (int i=0; i< sequence.size(); i++) {
    std::cout << sequence[i] << ' ';
  }
  std::cout << '\n';

  return 0;
}
