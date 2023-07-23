#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

void nuller(){
    setbuf(stdin, NULL);
    setbuf(stdout, NULL);
    setbuf(stderr, NULL);
}

void kampung_halaman(){
    char flag[300];
    FILE *f;
    if ((f = fopen("flag.txt", "r")) == NULL){
        printf("Loh flagnya mana :(....\n");
         exit(1);
    }
    fscanf(f,"%s",flag);
    printf("%s", flag);
    fclose(f);
    exit(1);
}

int main(){
    nuller();
    char buff[512];
    printf("Eh boo, kau tak pulang ke kampung ta?\n");
    scanf("%s",buff);
    printf("oh macem tu!\n");
    return;
}