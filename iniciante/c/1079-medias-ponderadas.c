#include <stdio.h>

int main(){
    int n_teste, i, j;
    float media, notas[3];
    scanf("%d", &n_teste);
    for (i = 0; i < n_teste; i++){
        for (j = 0; j < 3; j++){
            scanf("%f", &notas[j]);
        }
        media = (2 * notas[0] + 3 * notas[1] + 5 * notas[2])/10;
        printf("%.1f\n", media);
    }
}
