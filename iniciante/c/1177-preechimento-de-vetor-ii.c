#include <stdio.h>

int main(){
    int numero, n[1000], i, count = 0;
    scanf("%d", &numero);
    for(i = 0; i < 1000  ; i++){
        n[i] = count;
        printf("N[%d] = %d\n", i, n[i]);
        count++;
        if (count == numero){
            count = 0;
        }
    }
    return 0;
}
