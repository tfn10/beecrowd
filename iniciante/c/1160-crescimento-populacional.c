#include <stdio.h>
#include <stdbool.h>

int main(){
    int n_teste, i, populacao_a, populacao_b, anos;
    float crescimento_a, crescimento_b;
    scanf("%d", &n_teste);
    for (i = 0; i < n_teste; i++){  
        scanf("%d %d %f %f", &populacao_a, &populacao_b, &crescimento_a, &crescimento_b);
        anos = 0;
        while (true){
            anos++;
            populacao_a = populacao_a * (1.0 + crescimento_a / 100.0);
            populacao_b = populacao_b * (1.0 + crescimento_b / 100.0) ;
            if (populacao_a > populacao_b || anos > 100){
                break;
            }
        }
        if (anos > 100){
            printf("Mais de 1 seculo.\n");
        }
        else{
            printf("%d anos.\n", anos);
        }
    }
    return 0;
}
