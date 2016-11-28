#include <iostream>
#include <cmath>
#define DDF(X) ((X)*(X)*(X) - 7*(X)*(X) + 8*(X) + 3)/(3*(X)*(X) - 14*(X) +8)
// N-R for x^3 - 7x^2 + 8x + 3
int main() {
    float xn = -0.1f, xn1;
    int c = 1;
    do {
        xn1 = xn - DDF(xn);
        xn = xn1;
        c++;
    } while (abs(xn - xn1) > 0.0000001);
    std::cout << "End: " << c << std::endl << xn1 << std::endl;
    return 0;
}
