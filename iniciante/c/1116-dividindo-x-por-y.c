#include <stdio.h>

int main(){
    int n_teste, i;
    float x, y, divisao;
    scanf("%d", &n_teste);
    for (i = 0; i < n_teste; i++){
        scanf("%f %f", &x, &y);
        if (y == 0.0){
            printf("divisao impossivel\n");
        }
        else{
            divisao = x / y;
            printf("%.1f\n", divisao);
        }
    }
    return 0;
}
