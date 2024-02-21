#include <stdio.h>

int main() {
    unsigned long long number;
    int potencia = 0, numPF = 0;

    printf("Digite um número inteiro: ");
    scanf("%llu", &number);

    for (unsigned long long i = 2; i <= number; i = (i == 2) ? 3 : i + 2) {
        potencia = 0;
        while (number % i == 0) {
            number = number / i;
            potencia++;
        }
        if (potencia != 0)
            numPF++;
    }
    printf("Número de fatores primos distintos: %d\n", numPF);

    return 0;
}
