#include <stdio.h>

int main(){
    int i, j, inicial = 7;
    for(i = 1; i <= 9; i += 2){
        for(j = inicial; j >= inicial - 2; j--){
            printf("I=%d J=%d\n", i, j);
        }
        inicial += 2;
    }
    return 0;
}
