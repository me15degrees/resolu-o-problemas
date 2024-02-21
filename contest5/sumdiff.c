#include <stdio.h>
#include <math.h>

int main() {
    unsigned long long number;
    int sumPF = 0;

    printf("Enter an integer: ");
    scanf("%llu", &number);

    while (number % 2 == 0) {
        sumPF += 2;
        number = number / 2;
    }

    for (int i = 3; i <= sqrt(number); i = i + 2) {
        while (number % i == 0) {
            sumPF += i;
            number = number / i;
        }
    }

    if (number > 2)
        sumPF += number;

    printf("Sum of prime factors: %d\n", sumPF);

    return 0;
}
