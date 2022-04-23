#include <stdio.h>

int main(){
    int tamanho, i, menor, posicao = 0;
    scanf("%d", &tamanho);
    
    int v[tamanho];
    for(i = 0; i < tamanho; i++){
        scanf("%d", &v[i]);
    }

    menor = v[0];
    for(i = 1; i < tamanho; i++){
        if (v[i] < menor){
            menor = v[i];
            posicao = i;
        }
    }
    printf("Menor valor: %d\n", menor);
    printf("Posicao: %d\n", posicao);

    return 0;
}
