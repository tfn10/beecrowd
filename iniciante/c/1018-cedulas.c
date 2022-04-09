#include <stdio.h>

int main(){
    int numero, i, resto, quantidade;
    int notas[6] = {100, 50, 20, 10, 5, 2};   
    
    scanf("%d", &numero);

    resto = numero;
    for(i = 0; i < 6; i++){
        quantidade = resto / notas[i];
        
        printf("%d nota(s) de R$ %d,00\n", quantidade, notas[i]);

        resto = resto % notas[i];
    }

    printf("%d nota(s) de R$ 1,00\n", resto);
    
    return 0;
}
