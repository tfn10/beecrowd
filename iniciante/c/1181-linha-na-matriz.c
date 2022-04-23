#include <stdio.h>

int main(){
    double matriz[12][12], soma = 0.0, media; 
    int i, j, linha;
    char operacao;
    scanf("%d %c", &linha, &operacao);
    for(i = 0; i < 12; i++){
        for(j = 0; j < 12; j++){
            scanf("%lf", &matriz[i][j]);
        }
    }
    for(i = 0; i < 12; i++){
        soma += matriz[linha][i];
    }
    if (operacao == 'S'){
        printf("%.1lf\n", soma);
    }
    else{
        media = soma / 12.0;
        printf("%.1lf\n", media);
    }
    return 0;
}
