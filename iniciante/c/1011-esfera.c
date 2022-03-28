#include <stdio.h>
#include <math.h>

int main(){
    int raio;
    double volume_esfera, pi = 3.14159;
    scanf("%d", &raio);
    volume_esfera = (4.0/3.0) * pi * pow(raio, 3);
    printf("VOLUME = %.3lf\n", volume_esfera);
    return 0;
}
