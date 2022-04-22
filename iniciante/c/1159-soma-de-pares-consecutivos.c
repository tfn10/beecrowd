#include <stdio.h>
#include <stdbool.h>

int main(){
    int i, j, x, soma_pares;
    while (true){
        soma_pares = 0;
        scanf("%d", &x);
        if (x == 0){
            break;
        }
        if (x % 2 != 0){
            x++;
        }
        for (i = 0, j = x; i < 5; i++, j += 2){
            soma_pares += j;
        }
        printf("%d\n", soma_pares);
    }
    return 0;
}
