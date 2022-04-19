#include <stdio.h>

int main(){
    float salario, imposto;

    scanf("%f", &salario);
    
    if (salario >= 0.0 && salario <= 2000.0){
        printf("Isento\n");
    }
    else{
        if (salario >= 2000.01 && salario <= 3000.0){
            imposto = (salario - 2000.0) * 0.08;
        }
        else if (salario >= 3000.01 && salario <= 4500.0){
            imposto = 1000.0 * 0.08 + (salario - 3000.0) * 0.18;
        }
        else{
            imposto = 1000 * 0.08 + 1500.0 * 0.18 + (salario - 4500) * 0.28;
        }
        printf("R$ %.2f\n", imposto);
    }
    return 0;
}
