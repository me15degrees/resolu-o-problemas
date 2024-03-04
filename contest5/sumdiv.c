#include <stdio.h>
#include <math.h>

int main(){
    unsigned long long number;
    int potencia = 0, power = 1, aux;
    printf("enter an integer: ");
    scanf("%llu",&number);

    for (int i = 2; i <= number; i = i+2){
        potencia = 0;
        while (number%i == 0){
            number = number/i;
            potencia++;
        }
        if (potencia != 0){
            aux = i;
            for (int p = 0; p < potencia; p++)
                aux *= i;
            power *= ((aux - 1)/(i-1));
        }
        if (i==2)
            i--;
    }
    printf("soma de divisores: %d\n", power);
    return 0;
}