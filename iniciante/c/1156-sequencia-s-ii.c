#include <stdio.h>

int main(){
    double s = 0;
    int i, count = 0;
    for (i = 1; i <= 39; i += 2){
        s += i/pow(2, count);
        count++;
    }
    printf("%.2lf\n", s);
    return 0;
}
