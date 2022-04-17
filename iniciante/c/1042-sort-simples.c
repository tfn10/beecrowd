#include <stdio.h>

void imprime(int a[]){
    printf("%d\n", a[0]);
    printf("%d\n", a[1]);
    printf("%d\n", a[2]);
}

int main(){
    int valores[3], i, j, aux, v[3];

    // Perde a entrada para o usuário
    for (i = 0; i < 3; i++){
        scanf("%d", &valores[i]);
    }

    // Copia o conteúdo do vetor valores para
    for (i = 0; i < 3; i++){
        v[i] = valores[i];
    }

    // Ordena um vetor em ordem crescente
    for (i = 0; i < 3; i++){
        for (j = i + 1; j < 3; j++){
            if (valores[i] > valores[j]){
                aux = valores[i];
                valores[i] = valores[j];
                valores[j] = aux;
            }
        }
    }

    imprime(valores);
    printf("\n");
    imprime(v);
    
    return 0;
}
