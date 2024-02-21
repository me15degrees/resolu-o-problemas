#include <stdio.h>
#include <math.h>

int main(int argc, char const *argv[]) {
    unsigned long long number;
    int potencia = 0;

    printf("Digite um número inteiro: ");
    scanf("%llu", &number);

    printf("Fatores primos:\n");
    while(number % 2 == 0) {
        number = number / 2;
        potencia++;
    }
    if (potencia != 0)
        printf("2^%d\n", potencia);

    for (int i = 3; number >= 9; i = i + 2) {
        potencia = 0;
        while (number % i == 0) {
            number = number / i;
            potencia++;
        }
        if (potencia != 0)
            printf("%d^%d\n", i, potencia);
    }

    if (number > 1)
        printf("%llu^1\n", number);

    return 0;
}
