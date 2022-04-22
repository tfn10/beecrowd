#include <stdio.h>

int main(){
    int n, i, j, count = 1;
    scanf("%d", &n);
    for(i = 0; i < n; i++){
        for(j = 0; j < 3; j++){
            printf("%d ", count);
            if (j != 2){
                count++;
            }
            else{
                count += 2;
            }
        }
        printf("PUM\n");
    }
    return 0;
}
