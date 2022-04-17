#include <stdio.h>
#include <stdbool.h>

// Verifica se três lados formam um triângulo
bool eh_triangulo(float lado_a, float lado_b, float lado_c){
    if (lado_a + lado_b > lado_c && lado_b + lado_c > lado_a && lado_a + lado_c > lado_b){
        return true;
    }
    return false;
}

int main(){
    float a, b, c, perimetro, area;

    // Entrada do usuário
    scanf("%f", &a);
    scanf("%f", &b);
    scanf("%f", &c);

    // Calcula o perímetro do triângulo
    if (eh_triangulo(a, b, c)){
        perimetro = a + b + c;
        printf("Perimetro = %.1f\n", perimetro);
    }
    // Calcula a área do trapézio
    else{
        area = ((a + b) * c)/2;
        printf("Area = %.1f\n", area);
    }

    return 0;
}
