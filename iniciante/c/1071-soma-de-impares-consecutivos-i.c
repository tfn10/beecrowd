#include <stdio.h>

int main(){
    int n1, n2, aux, i, soma_impares = 0;
    scanf("%d %d", &n1, &n2);
    if (n2 < n1){
        aux = n2;
        n2 = n1;
        n1 = aux;
    }
    for (i = n1 + 1; i < n2; i++){
        if (i % 2 != 0){
            soma_impares += i;
        }
    }
    printf("%d\n", soma_impares);
    return 0;
}
