#include <stdio.h>
#include <stdbool.h>

void eh_perfeito(int n){
    int i, soma = 0;
    for(i = 1; i < n / 2 + 1; i++){
        if (n % i == 0){
            soma += i;
        }
    }
    if (soma == n){
        printf("%d eh perfeito\n", n);
    }
    else{
        printf("%d nao eh perfeito\n", n);
    }
}

int main(){
    int n_teste, i, numero;
    scanf("%d", &n_teste);
    for (i = 0; i < n_teste; i++){
        scanf("%d", &numero);
        eh_perfeito(numero);
    }
    return 0;
}
