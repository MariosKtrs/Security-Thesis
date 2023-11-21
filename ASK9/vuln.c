#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

int target;

void vuln(char *string)
{
    printf(string);

    if(target) {
        printf("FLAG{B1N4RY_SM4SH3R}\n");
    }
}

int main(int argc, char **argv)
{

    vuln(argv[1]);
}
