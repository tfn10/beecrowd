#include <stdio.h>

int main(){
    float notas[4], media, nota_exame;
    int i;

    for(i = 0; i < 4; i++){
        scanf("%f", &notas[i]);
    }

    media = (2.0 * notas[0] + 3.0 * notas[1] + 4.0 * notas[2] + notas[3]) / 10;

    printf("Media: %.1f\n", media);
    if (media >= 7.0){
        printf("Aluno aprovado.\n");
    }
    else if (media < 5.0){
        printf("Aluno reprovado.\n");
    }
    else{
        printf("Aluno em exame.\n");
        scanf("%f", &nota_exame);
        printf("Nota do exame: %.1f\n", nota_exame);
        media = (media + nota_exame)/2;
        if (media >= 5.0){
            printf("Aluno aprovado.\n");
        }
        else{
            printf("Aluno reprovado.\n");
        }
        printf("Media final: %.1f\n", media);
    }

    return 0;
}
