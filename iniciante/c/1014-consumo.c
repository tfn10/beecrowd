#include <stdio.h>

int main(){
    int distancia_total;
    float combustivel_gasto, consumo_medio;
    scanf("%d %f", &distancia_total, &combustivel_gasto);
    consumo_medio = distancia_total / combustivel_gasto;
    printf("%.3f km/l\n", consumo_medio);
    return 0;
}
