#include <stdio.h>

int soma_impares(int numero1, int numero2){
    int soma = 0, i, aux;
    if(numero1 > numero2){
        aux = numero1;
        numero1 = numero2;
        numero2 = aux;
    }
    for(i = numero1 + 1; i < numero2; i++){
        if(i % 2 != 0){
            soma += i;
        }
    }
    return soma;
}

int main(){
    int n_teste, i, n1, n2;
    scanf("%d", &n_teste);
    for(i = 0; i < n_teste; i++){
        scanf("%d %d", &n1, &n2);
        printf("%d\n", soma_impares(n1, n2));
    }
    return 0;
}
