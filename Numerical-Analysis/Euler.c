#include <math.h>
#include <stdio.h>
double f(double x, double y) {
  return -100*y + 5*pow(x, 1.5)*(1 + 40*x);
}

int main() {
  double const h0 = 0.0227;
  double yn = 0.0;
  for (double xn = 0; xn <= 1.0; xn += h0) {
    yn += f(xn, yn)*h0;
    printf("x = %14.4f y =  %14.4f\n", xn, yn);
  }
  yn = 0;
  for (double xn = 0; xn <= 1.0; xn += h0/2) {
    yn += f(xn, yn)*h0/2;
    printf("x = %14.4f y =  %14.4f\n", xn, yn);
  }
  return 0;
}
