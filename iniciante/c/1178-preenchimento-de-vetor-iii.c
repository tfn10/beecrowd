#include <stdio.h>

int main(){
    double n[100], numero;
    int i;
    scanf("%lf", &numero);
    n[0] = numero;
    printf("N[0] = %.4lf\n", n[0]);
    for(i = 1; i < 100; i++){
        n[i] = n[i - 1] / 2.0;
        printf("N[%d] = %.4lf\n", i, n[i]);
    }
    return 0;
}
