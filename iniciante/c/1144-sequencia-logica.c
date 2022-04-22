#include <stdio.h>

void imprime(int x, int prod){
    if (x != 3){
        printf("%d ", prod);
    }
    else{
        printf("%d\n", prod);
    }
}

int main(){
    int n, i, j, produto;
    scanf("%d", &n);
    for (i = 1; i <= n; i++){
        produto = 1;
        for (j = 1; j <= 3; j++){
            produto *= i;
            imprime(j, produto);
        }

        produto = 1;
        for (j = 1; j <= 3; j++){
            produto *= i;
            if (j == 1){
                imprime(j ,produto);
            }
            else{
                imprime(j, produto + 1);
            }
        }
    }
    return 0;
}
