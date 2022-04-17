#include <stdio.h>

int main(){
    int a, b;

    // Entrada do usuário
    scanf("%d", &a);
    scanf("%d", &b);

    // Verifica se a e b são múltiplos entre si
    if (b % a == 0 || a % b == 0){
        printf("Sao Multiplos\n");
    }
    else{
        printf("Nao sao Multiplos\n");
    }

    return 0;
}
