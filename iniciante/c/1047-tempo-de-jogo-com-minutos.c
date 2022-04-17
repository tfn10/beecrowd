#include <stdio.h>

int main(){
    int hora_inicial, minuto_inicial, hora_final, minuto_final, hora_jogada, minuto_jogado, minuto_total;

    // Entrada do usuário
    scanf("%d", &hora_inicial);
    scanf("%d", &minuto_inicial);
    scanf("%d", &hora_final);
    scanf("%d", &minuto_final);

    // Imprime o tempo que durou o jogo
    if (hora_inicial == hora_final && minuto_inicial == minuto_final){
        hora_jogada = 24;
        minuto_jogado = 0;
    }
    else{
        minuto_total = hora_final * 60 + minuto_final - (hora_inicial * 60 + minuto_inicial);
        if (minuto_total > 0){
            hora_jogada = minuto_total / 60;
            minuto_jogado = minuto_total % 60;
        }
        else{
            minuto_total+= 24 * 60;
            hora_jogada = minuto_total / 60;
            minuto_jogado = minuto_total % 60;
        }
    }
    printf("O JOGO DUROU %d HORA(S) E %d MINUTO(S)\n", hora_jogada, minuto_jogado);

    return 0;
}
