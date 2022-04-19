#include <stdio.h>

int main(){
    int n_teste, i, dentro = 0, fora = 0, valor;
    scanf("%d", &n_teste);
    for (i = 0; i < n_teste; i++){
        scanf("%d", &valor);
        if (valor >= 0 && valor <= 20){
            dentro++;
        }
        else{
            fora++;
        }
    }
    printf("%d in\n", dentro);
    printf("%d out\n", fora);
    return 0;
}
