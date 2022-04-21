#include <stdio.h>
#include <stdbool.h>

void soma_sequencia(int n1, int n2){
    int i, aux, soma = 0;

    if (n1 > n2){
        aux = n1;
        n1 = n2;
        n2 = aux;
    }
    
    for(i = n1; i <= n2; i++){
        soma += i;
        printf("%d ", i);
    }
    printf("Sum=%d\n", soma);
}

int main(){
    int a, b;
    while (true){
        scanf("%d %d", &a, &b);
        if (a <= 0 || b <= 0){
            break;
        }
        soma_sequencia(a, b);
    }
    return 0;
}
