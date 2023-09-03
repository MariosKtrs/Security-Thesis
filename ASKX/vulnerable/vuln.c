#include <stdio.h>
#include <string.h>

int overflow(){
  char password[16];
  printf("Guess the password: ");
  gets(password);

  if (strcmp(password, "corr3ctpassw0rd"))
      printf("try again");
  else
      success();
}

int main(int argc, char *argv[])
{
      overflow();
}

void success()
{
      printf("\nFLAG{Wh0_l3t_th3_Buff3r_0v3rfl0w}\n");
      return;
}
