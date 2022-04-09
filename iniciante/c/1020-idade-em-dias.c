#include <stdio.h>

int main(){
    int anos, meses, dias, n;
    
    scanf("%d", &n);
    
    anos = n / 365;
    meses = (n - anos * 365) / 30;
    dias = n - anos * 365 - meses * 30;
    
    printf("%d ano(s)\n", anos);
    printf("%d mes(es)\n", meses);
    printf("%d dia(s)\n", dias);

    return 0;
}
