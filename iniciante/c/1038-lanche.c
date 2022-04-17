#include <stdio.h>

int main(){
    int codigo, quantidade;
    float total = 0;

    scanf("%d", &codigo);
    scanf("%d", &quantidade);

    if (codigo == 1){
        total = 4.0 * quantidade;
    }
    else if (codigo == 2){
        total = 4.5 * quantidade;
    }
    else if (codigo == 3){
        total = 5.0 * quantidade;
    }
    else if (codigo == 4){
        total = 2.0 * quantidade;
    }
    else if (codigo == 5){
        total = 1.5 * quantidade;
    }

    printf("Total: R$ %.2f\n", total);

    return 0;
}