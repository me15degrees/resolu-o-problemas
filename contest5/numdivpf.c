#include <stdio.h>
#include <math.h>

int main(){
    unsigned long long number;
    int potencia = 0, power = 1;

    printf("enter an integer: ");
    scanf("%llu", &number);

    for (int i = 2; i <= number; i = i+2){
        potencia = 0;
        while (number%i == 0){
            number = number/i;
            potencia++;
        }
        if (potencia != 0)
            power *= (potencia + 1);
        if (i == 2)
            i--;
    }
    printf("numero de divisores: %d\n", power);
    return 0;
}