#include <stdio.h>

int main(){
    float a, b, c;
    double media;
    scanf("%f %f %f", &a, &b, &c);
    media = (2 * a + 3 * b + 5 * c)/10;
    printf("MEDIA = %.1lf\n", media);
    return 0;
}
