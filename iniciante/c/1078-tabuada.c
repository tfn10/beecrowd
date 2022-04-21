#include <stdio.h>

int main(){
    int numero, i;
    scanf("%d", &numero);
    for (i = 1; i < 11; i++){
        printf("%d x %d = %d\n", i, numero, i * numero);
    }
    return 0;
}
