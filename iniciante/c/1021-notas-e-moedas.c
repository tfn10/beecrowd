#include <stdio.h>
#include <math.h>

int main(){
    int i, nota, moeda, resto;
    int notas[6] = {10000, 5000, 2000, 1000, 500, 200};
    int moedas[6] = {100, 50, 25, 10, 5, 1};
    float entrada;

    scanf("%f", &entrada);
    resto = lround(100.0 * entrada);

    printf("NOTAS:\n");
    for(i = 0; i < 6; i++){
        nota = resto / notas[i];
        resto = resto % notas[i];
        printf("%d nota(s) de R$ %d.00\n", nota, notas[i] / 100);
    }

    printf("MOEDAS:\n");
    for(i = 0; i < 6; i++){
        moeda = resto / moedas[i];
        resto = resto % moedas[i];
        printf("%d moeda(s) de R$ %.2f\n", moeda, (float) moedas[i] / 100);
    }

    return 0;

}