#include <stdio.h>

int main(){
    float salario, novo_salario, reajuste;
    int percentual;

    scanf("%f", &salario);
    
    if (salario >= 0.0 && salario <= 400.0){
        novo_salario = salario * 1.15;
        reajuste = novo_salario - salario;
        percentual = 15;
    }
    else if (salario >= 400.01 && salario <= 800.0){
        novo_salario = salario * 1.12;
        reajuste = novo_salario - salario;
        percentual = 12;
    }
    else if (salario >= 800.01 && salario <= 1200.0){
        novo_salario = salario * 1.1;
        reajuste = novo_salario - salario;
        percentual = 10;
    }
    else if (salario >= 1200.01 && salario <= 2000.0){
        novo_salario = salario * 1.07;
        reajuste = novo_salario - salario;
        percentual = 7;
    }
    else if (salario >= 2000.0){
        novo_salario = salario * 1.04;
        reajuste = novo_salario - salario;
        percentual = 4;
    }

    printf("Novo salario: %.2f\n", novo_salario);
    printf("Reajuste ganho: %.2f\n", reajuste);
    printf("Em percentual: %d %%\n", percentual);

    return 0;
}
