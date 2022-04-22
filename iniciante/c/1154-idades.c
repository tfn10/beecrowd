#include <stdio.h>
#include <stdbool.h>

int main(){
    int count = 0, idade;
    float idades_totais = 0, media;
    while (true){
        scanf("%d", &idade);
        if (idade < 0){
            break;
        }
        idades_totais += idade;
        count++;
    }
    media = idades_totais / count;
    printf("%.2f\n", media);

    return 0;
}
