#include <stdio.h>
#include <math.h>

int main(){
    float n = 3.14159;
    float raio;
    double area_do_circulo;
    scanf("%f", &raio);
    area_do_circulo = n * pow(raio, 2);
    printf("A=%.4lf\n", area_do_circulo);
    return 0;
}
