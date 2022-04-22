#include <stdio.h>
#include <stdbool.h>

int entrada_valida(){
    int valor;
    while (true){
        scanf("%d", &valor);
        if (valor > 0){
            break;
        }
    }
    return valor;
}

int main(){
    int a, n, i, soma = 0;
    a = entrada_valida();
    n = entrada_valida();
    for (i = 0; i < n; i++){
        soma += a + i;
    }
    printf("%d\n", soma);
    return 0;
}
