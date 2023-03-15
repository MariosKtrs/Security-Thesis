#include <stdio.h>
#include <stdlib.h>

int target;

void vuln(char *string)
{

printf(string);

if(target) 
   printf("you have modified the target\n");
}

int main (int  argc, char **argv)
{

if(argc == 1 || argc > 2)
  printf("You should run the program in the following format : ./vuln [your_input]");
else
  vuln(argv[1]);
}
