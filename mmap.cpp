#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <sys/mman.h>
#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <fcntl.h>
#include <string.h>
using namespace std;
//#define BUF_SIZE 4096            // use a buffer size of 4096 bytes
#define OUTPUT_MODE 0700
int main(int argc, char** argv) {
    //char buffer[BUF_SIZE];
    int rd_count, wt_count;
  /* Make sure the command line is correct */
  if (argc != 3) {
      cout << "\n" << "enter input file name, output file name: pgm will exit otherwise" << "\n";
      exit(1);
  }
  /* Open the specified file */
  int fd = open(argv[1], O_RDWR);
  if (fd < 0)
  {
    cout << "\n" << "input file cannot be opened" << "\n";
    exit(1);
  }
  int out_fd = open(argv[2], O_RDWR | O_CREAT | O_TRUNC, 0664);
  if (out_fd < 0) {
    cout << "\n" << "output file cannot be created" << "\n";
    exit(1);
  }


  struct stat stats;

  if (stat(argv[1], &stats) == 0)
    cout << endl << "file size " << stats.st_size;
  else
    cout << "Unable to get file properties.\n";
  /* Get the page size  */
  int pagesize = getpagesize();
  cout << endl << "page size is " << pagesize << "\n";

  int filesize = stats.st_size;
  lseek(out_fd, filesize - 1, SEEK_SET);
  write(out_fd, "", 1);
  lseek(out_fd, 0, SEEK_SET);
  off_t offset = 0;
  while (filesize > 0) {
    if (filesize < pagesize) {
      pagesize = filesize;
      filesize = 0;
    } else {
       filesize -= pagesize;
    }
    char* data = (char*)mmap(NULL, pagesize, PROT_READ | PROT_WRITE, MAP_SHARED, fd, offset);
    /* Did the mapping succeed ? */
    if (!data)
    {
      cout << "\n" << "mapping did not succeed" << "\n";
      exit(1);
    }
    char* dest = (char*)mmap(NULL, pagesize, PROT_READ | PROT_WRITE, MAP_SHARED, out_fd, offset);
    if (dest == MAP_FAILED) {
      cout << "\n" << "destination mapping did not succeed" << "\n";
      exit(1);
    }

    memcpy(dest, data, pagesize);

    /* Unmap the shared memory region */
    munmap(data, pagesize);
    munmap(dest, pagesize);

    lseek(fd, pagesize, SEEK_SET);
    lseek(out_fd, pagesize, SEEK_SET);
    offset += pagesize;
  }


  /* Close the file */
  close(fd);
  close(out_fd);
  return 0;
}
