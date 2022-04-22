#include <stdio.h>

int main(){
    int a = 0, b = 1, aux, n, i;
    scanf("%d", &n);
    for(i = 0; i < n; i++){
        if (i != n - 1){
            printf("%d ", a);
        }
        else{
            printf("%d\n", a);
        }
        aux = a;
        a = b;
        b += aux;
    }

    return 0;
}
