#include <stdio.h>

int main(){
    char nome_vendedor;
    double salario_fixo, total_vendas, salario;
    scanf("%s %lf %lf", &nome_vendedor, &salario_fixo, &total_vendas);
    salario = salario_fixo + total_vendas * 0.15;
    printf("TOTAL = R$ %.2lf\n", salario);
    return 0;
}
