#include <stdio.h>

int main(){
    int i = 0;
    float nota, soma = 0, media;
    while (i < 2){
        scanf("%f", &nota);
        if (nota < 0.0 || nota > 10.0){
            printf("nota invalida\n");
        }
        else{
            soma += nota;
            i++;
        }
    }
    media = soma / 2;
    printf("media = %.2f\n", media);

    return 0;
}
