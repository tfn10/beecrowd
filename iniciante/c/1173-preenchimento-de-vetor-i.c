#include <stdio.h>

int main(){
    int v[10], i, aux;
    scanf("%i", &aux);
    v[0] = aux;
    for (i = 1; i < 10; i++){
        v[i] = 2 * v[i - 1];
    }
    for (i = 0; i < 10; i++){
        printf("N[%i] = %i\n", i, v[i]);
    }
}
