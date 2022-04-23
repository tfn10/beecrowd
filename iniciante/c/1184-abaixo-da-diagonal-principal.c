#include <stdio.h>

int main(){
    double matriz[12][12], soma = 0.0, media, count = 0.0; 
    int i, j, inicial = 1;
    char operacao;
    scanf("%c", &operacao);
    for(i = 0; i < 12; i++){
        for(j = 0; j < 12; j++){
            scanf("%lf", &matriz[i][j]);
        }
    }
    for(i = 1; i < 12; i++){
        for(j = 0; j < inicial; j++){
            soma += matriz[i][j];
            count = count + 1.0;
        }
        inicial++;
    }
    if (operacao == 'S'){
        printf("%.1lf\n", soma);
    }
    else{
        media = soma / count;
        printf("%.1lf\n", media);
    }
    return 0;
}
