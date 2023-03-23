#include <stdio.h>
int secret_address;

int main(int argc, char **argv) {
    vuln_func(argv[1]);
}

void vuln_func(char *input){

printf(input);

if(secret_address)
  printf("HTB{T4rgetD3stroy3d}");

}
