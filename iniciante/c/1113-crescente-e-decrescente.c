#include <stdio.h>
#include <stdbool.h>

int main(){
    int x, y;
    while (true){
        scanf("%d %d", &x, &y);
        if (x > y){
            printf("Decrescente\n");
        }
        else if (x < y){
            printf("Crescente\n");
        }
        else{
            break;
        }
    }
    return 0;
}
