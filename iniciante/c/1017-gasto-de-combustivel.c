#include <stdio.h>

int main(){
    float tempo_gasto, velocidade_media, litros;
    scanf("%f %f", &tempo_gasto, &velocidade_media);
    litros = velocidade_media * tempo_gasto / 12;
    printf("%.3f\n", litros);
    return 0;
}
