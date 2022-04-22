#include <stdio.h>

int main(){
    int n_teste, i, j, x, y, soma;
    scanf("%d", &n_teste);
    for (i = 0; i < n_teste; i++){
        soma = 0;
        scanf("%d %d", &x, &y);
        if (x % 2 == 0){
            x++;
        }
        for (j = 0; j < y; j++){
            soma += x;
            x += 2;
        }
        printf("%d\n", soma);
    }
    return 0;
}
