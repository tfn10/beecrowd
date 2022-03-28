#include <stdio.h>
#include <math.h>

int main(){
    double a, b, c, pi = 3.14159;
    double area_triangulo_retangulo, area_circulo, area_trapezio, area_quadrado, area_retangulo;
    
    scanf("%lf %lf %lf", &a, &b, &c);
    area_triangulo_retangulo = a * c / 2;
    area_circulo = pi * pow(c, 2);
    area_trapezio = (a + b) * c / 2;
    area_quadrado = b * b;
    area_retangulo = a * b;
    printf("TRIANGULO: %.3f\n", area_triangulo_retangulo);
    printf("CIRCULO: %.3f\n", area_circulo);
    printf("TRAPEZIO: %.3f\n", area_trapezio);
    printf("QUADRADO: %.3f\n", area_quadrado);
    printf("RETANGULO: %.3f\n", area_retangulo);
    return 0;
}
