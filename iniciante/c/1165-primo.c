#include <stdio.h>
#include <stdbool.h>

bool eh_primo(int numero){
    int i;
    if (numero != 2){
        for (i = 2; i < numero / 2 + 1; i++){
            if (numero % i == 0){
                return false;
            }
        }
    }
    return true;
}

int main(){
    int n_teste, i, valor;
    scanf("%d", &n_teste);
    for (i = 0; i < n_teste; i++){
        scanf("%d", &valor);
        if (eh_primo(valor)){
            printf("%d eh primo\n", valor);
        }
        else{
            printf("%d nao eh primo\n", valor);
        }
    }
}
