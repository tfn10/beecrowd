#include <stdio.h>
#include <math.h>

int main(){
    int i, valor, limite, quadrado;
    scanf("%d", &valor);
    if (valor % 2 == 0){
        limite = valor + 1;
    }
    else{
        limite = valor;
    }
    for (i = 2; i < limite; i = i + 2){
        quadrado = pow(i , 2);
        printf("%d^2 = %d\n", i, quadrado);
    }
    return 0;
}
