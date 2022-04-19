#include <stdio.h>

int main(){
    int positivos = 0, i;
    float numero;
    for (i = 0; i < 6; i++){
        scanf("%f", &numero);
        if (numero > 0.0){
            positivos++;
        }
    }
    printf("%d valores positivos\n", positivos);
    return 0;
}
