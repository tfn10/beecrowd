#include <stdio.h>

int main(){
    int n_valores, i, valor;
    scanf("%d", &n_valores);
    for (i = 0; i < n_valores; i++){
        scanf("%d", &valor);
        if (valor == 0){
            printf("NULL\n");
        }
        else{
            if (valor % 2 == 0){
                printf("EVEN ");
            }
            else{
                printf("ODD ");
            }
            if (valor > 0){
                printf("POSITIVE\n");
            }
            else{
                printf("NEGATIVE\n");
            }
        }
    }
    return 0;
}
