#include <stdio.h>
#include <stdbool.h>

int main(){
    int i = 0, decisao, count = 0;
    float nota, soma = 0, media;
    while (i < 2){
        scanf("%f", &nota);
        if (nota < 0.0 || nota > 10.0){
            printf("nota invalida\n");
        }
        else{
            soma += nota;
            i++;
            count++;
        }
        
        if (i == 2){
            media = soma / count;
            printf("media = %.2f\n", media);
            while (true){
                printf("novo calculo (1-sim 2-nao)\n");
                scanf("%d", &decisao);
                if (decisao == 1 || decisao == 2){
                    i = 0;
                    break;
                }
            }
        }
    }

    return 0;
}
