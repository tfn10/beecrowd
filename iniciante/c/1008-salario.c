#include <stdio.h>

int main(){
    int n_funcionario, horas_trabalhas;
    float valor_por_hora, salario;
    scanf("%d %d %f", &n_funcionario, &horas_trabalhas, &valor_por_hora);
    salario = horas_trabalhas * valor_por_hora;
    printf("NUMBER = %d\nSALARY = U$ %.2f\n", n_funcionario, salario);
    return 0;
}
