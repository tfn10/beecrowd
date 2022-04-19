#include <stdio.h>

int main(){
    int i, valor, inicial;
    scanf("%d", &valor);
    if (valor % 2 == 0){
        inicial = valor + 1;
    }
    else{
        inicial = valor;
    }
    for (i = inicial; i <= inicial + 10; i = i + 2){
        printf("%d\n", i);
    }
    return 0;
}
