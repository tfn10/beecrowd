#include <stdio.h>

int main(){
    int valor, i, limite;
    scanf("%d", &valor);
    if (valor % 2 == 0){
        limite = valor;
    }
    else{
        limite = valor + 1;
    }
    for (i = 1; i < limite; i = i + 2){
        printf("%d\n", i);
    }
    return 0;
}
