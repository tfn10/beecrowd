#include <stdio.h>
#include <stdbool.h>

int z_valido(int valor_x){
    int valor_z;
    while (true){
        scanf("%d", &valor_z);
        if (valor_z > valor_x){
            break;
        }
    }
    return valor_z;
}

int main(){
    int x, z, soma = 0, i, count = 0;
    
    scanf("%d", &x);
    z = z_valido(x);

    for(i = x; ; i++){
        soma += i;
        count++;
        if (soma > z){
            break;
        }
    }

    printf("%d\n", count);

    return 0;
}