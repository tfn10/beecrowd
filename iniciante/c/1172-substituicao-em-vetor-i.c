#include <stdio.h>

int main(){
    int v[10], i;
    for (i = 0; i < 10; i++){
        scanf("%d", &v[i]);
        if (v[i] <= 0){
            v[i] = 1;
        }
        printf("X[%d] = %d\n", i, v[i]);
    }
    return 0;
}
