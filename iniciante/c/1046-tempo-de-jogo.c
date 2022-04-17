#include <stdio.h>

int main(){
    int hora_inicial, hora_final, tempo_de_jogo;
    
    scanf("%d %d", &hora_inicial, &hora_final);

    if (hora_final > hora_inicial){
        tempo_de_jogo = hora_final - hora_inicial;
    }
    else if (hora_final < hora_inicial){
        tempo_de_jogo = 24 + hora_final - hora_inicial;
    }
    else{
        tempo_de_jogo = 24;
    }
    printf("O JOGO DUROU %d HORA(S)\n", tempo_de_jogo);
    
    return 0;
}
