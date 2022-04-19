#include <stdio.h>

int main(){
    int i, positivos = 0;
    float numero, media, total = 0.0;
    for (i = 0; i < 6; i++){
        scanf("%f", &numero);
        if (numero > 0.0){
            total += numero;
            positivos++;
        }
    }
    media = total / positivos;
    printf("%d valores positivos\n", positivos);
    printf("%.1f\n", media);

    return 0;
}
