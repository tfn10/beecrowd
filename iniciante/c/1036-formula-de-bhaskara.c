#include <stdio.h>
#include <math.h>


float delta(float a, float b, float c){
    return pow(b, 2) - 4 * a * c; 
}

void raizes(float a, float b, float valor_de_delta){
    float r1, r2;

    r1 = (-1 * b + sqrt(valor_de_delta)) / (2 * a);
    r2 = (-1 * b - sqrt(valor_de_delta)) / (2 * a);
    
    printf("R1 = %.5f\n", r1);
    printf("R2 = %.5f\n", r2);
}

int main(){
    float valor_a, valor_b, valor_c, valor_delta;
    
    scanf("%f", &valor_a);
    scanf("%f", &valor_b);
    scanf("%f", &valor_c);

    valor_delta = delta(valor_a, valor_b, valor_c);

    if (valor_delta < 0 || valor_a == 0){
        printf("Impossivel calcular\n");
    }
    else{
        raizes(valor_a, valor_b, valor_delta);
    }
    return 0;
}
