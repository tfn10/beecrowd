#include <stdio.h>

int main(){
    int i, valor, maior = 0, posicao = 0;
    for (i = 0; i < 100; i++){
        scanf("%d", &valor);
        if (valor > maior){
            maior = valor;
            posicao = i + 1;
        }
    }
    printf("%d\n", maior);
    printf("%d\n", posicao);
    return 0;
}
