#include <stdio.h>
#include <math.h>
#define b 2
#define a 1
double f(double x) {
    return exp(-x/2) + cos(3.5*x) - 3/(x - 4);
}
int main() {
    double h = (b - a)/50.0;
    double I = f(1) + f(2);
    double xn = 1.0;
    for (int i = 1; i < 50; i++) {
        xn += h;
        I += 2*f(xn) + 2*(i%2)*f(xn);
    }
    printf("result of Simpson = %14.10f", I*h/3);
    return 0;
}
