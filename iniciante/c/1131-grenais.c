#include <stdio.h>
#include <stdbool.h>


int novo_grenal(){
    int continuar;
    while (true){
        printf("Novo grenal (1-sim 2-nao)\n");
        scanf("%d", &continuar);
        if (continuar == 1 || continuar == 2){
            break;
        }
    }
    return continuar;
}


int main(){
    int gols_gremio, gols_inter, continuar_grenal;
    int vitoria_gremio = 0, vitoria_inter = 0, empate = 0, total_grenal = 0;
    while (true){
        scanf("%d %d", &gols_inter, &gols_gremio);

        if (gols_gremio > gols_inter){
            vitoria_gremio++;
        }
        else if (gols_gremio == gols_inter){
            empate++;
        }
        else{
            vitoria_inter++;
        }

        total_grenal++;
        
        continuar_grenal = novo_grenal();
        if (continuar_grenal == 2){
            break;
        }
    }
    printf("%d grenais\n", total_grenal);
    printf("Inter:%d\n", vitoria_inter);
    printf("Gremio:%d\n", vitoria_gremio);
    printf("Empates:%d\n", empate);
    if (vitoria_gremio > vitoria_inter){
        printf("Gremio venceu mais\n");
    }
    else if (vitoria_gremio < vitoria_inter){
        printf("Inter venceu mais\n");
    }
    else{
        printf("Nao houve vencedor\n");
    }
    return 0;
}
