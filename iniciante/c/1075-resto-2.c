#include <stdio.h>

int main(){
    int valor, i, count = 0;
    scanf("%d", &valor);
    for (i = 1; i < 10000; i++){
        if (i % valor == 2){
            printf("%d\n", i);
        }
    }
    return 0;
}
