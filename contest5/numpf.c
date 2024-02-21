#include <stdio.h>
#include <math.h>

int main(){
    unsigned long long number;
    int numPF = 0;

    printf("enter an integer: ");
    scanf("%llu", &number);

    for (int i = 2; i <= number; i = i + 2) {
        while (number % i == 0) {
            number = number / i;
            numPF++;
        }
        if (i == 2)
            i--;
    }
    printf("número de fatores primos: %d\n", numPF);
    return 0;
}
