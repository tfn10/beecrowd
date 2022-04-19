#include <stdio.h>

int main(){
    int i, numero, pares = 0;
    for (i = 0; i < 5; i++){
        scanf("%d", &numero);
        if (numero % 2 == 0){
            pares++;
        }
    }
    printf("%d valores pares\n", pares);
    return 0;
}
