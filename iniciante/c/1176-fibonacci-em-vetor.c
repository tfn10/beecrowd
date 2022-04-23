#include <stdio.h>

unsigned long long int fibonacci_vetor(int n){
    unsigned long long int a = 0, b = 1, aux;
    int i;
    for(i = 0; i <= n; i++){
        if (i == n){
            return a;
        }
        aux = a;
        a = b;
        b += aux;
    }
}

int main(){
    unsigned long long int fib;
    int n_teste, numero, i;
    scanf("%d", &n_teste);
    for(i = 0; i < n_teste; i++){
        scanf("%d", &numero);
        fib = fibonacci_vetor(numero);
        printf("Fib(%d) = %llu\n", numero, fib);
    }
    return 0;
}
