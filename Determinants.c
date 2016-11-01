#include <stdio.h>
#include <math.h>

#define PERS 0.5 * pow(10.0, -5.0)

double det2x2(double a, double b, double c, double d) {
    return a * d - c * b;
}

double det3x3(double A[3][3]) {
    return A[0][0] * det2x2(A[1][1], A[1][2], A[2][1], A[2][2])
           - A[1][0] * det2x2(A[0][1], A[0][2], A[2][1], A[2][2])
           + A[2][0] * det2x2(A[0][1], A[0][2], A[1][1], A[1][2]);
}

double det4x4(double A[4][4]) {
    double a1[3][3] = {{A[1][1], A[1][2], A[1][3]},
                       {A[2][1], A[2][2], A[2][3]},
                       {A[3][1], A[3][2], A[3][3]}};
    double a2[3][3] = {{A[0][1], A[0][2], A[0][3]},
                       {A[2][1], A[2][2], A[2][3]},
                       {A[3][1], A[3][2], A[3][3]}};
    double a3[3][3] = {{A[0][1], A[0][2], A[0][3]},
                       {A[1][1], A[1][2], A[1][3]},
                       {A[3][1], A[3][2], A[3][3]}};
    double a4[3][3] = {{A[0][1], A[0][2], A[0][3]},
                       {A[1][1], A[1][2], A[1][3]},
                       {A[2][1], A[2][2], A[2][3]}};
    return A[0][0] * det3x3(a1) - A[1][0] * det3x3(a2) + A[2][0] * det3x3(a3) - A[3][0] * det3x3(a4);
}

double f1(double x1, double x2, double x3, double x4) { return 3 * x2 + x3 * x4 - 7.9; }

double f2(double x1, double x2, double x3, double x4) { return x1 - 2 * x2 + x3 + 4 * x4 - 20.7; }

double f3(double x1, double x2, double x3, double x4) { return pow(x1, 3.0) + pow(x3, 3.0) + x4 - 21.218; }

double f4(double x1, double x2, double x3, double x4) { return pow(x1, 2.0) + 2 * x1 * x2 + pow(x4, 3.0) - 15.88; }

int main() {
    double x1 = 1.0, x2 = 1.0, x3 = 1.0, x4 = 1.0;
    double d1, d2, d3, d4;
    int c = 0;
    do {
        double B[4][4] = {{0.0,           3.0,    x4,  x3},
                          {1.0,           2.0,    1.0, 4.0},
                          {3 * x1 * x1,   2.0,    1.0, 4.0},
                          {2 * (x1 + x2), 2 * x1, 0.0, 3 * x4 * x4}};
        double B1[4][4] = {{-f1(x1, x2, x3, x4), 3.0,    x4,  x3},
                           {-f2(x1, x2, x3, x4), 2.0,    1.0, 4.0},
                           {-f3(x1, x2, x3, x4), 2.0,    1.0, 4.0},
                           {-f4(x1, x2, x3, x4), 2 * x1, 0.0, 3 * x4 * x4}};
        double B2[4][4] = {{0.0,           -f1(x1, x2, x3, x4), x4,  x3},
                           {1.0,           -f2(x1, x2, x3, x4), 1.0, 4.0},
                           {3 * x1 * x1,   -f3(x1, x2, x3, x4), 1.0, 4.0},
                           {2 * (x1 + x2), -f4(x1, x2, x3, x4), 0.0, 3 * x4 * x4}};
        double B3[4][4] = {{0.0,           3.0,    -f1(x1, x2, x3, x4), x3},
                           {1.0,           2.0,    -f2(x1, x2, x3, x4), 4.0},
                           {3 * x1 * x1,   2.0,    -f3(x1, x2, x3, x4), 4.0},
                           {2 * (x1 + x2), 2 * x1, -f4(x1, x2, x3, x4), 3 * x4 * x4}};
        double B4[4][4] = {{0.0,           3.0,    x4,  -f1(x1, x2, x3, x4)},
                           {1.0,           2.0,    1.0, -f2(x1, x2, x3, x4)},
                           {3 * x1 * x1,   2.0,    1.0, -f3(x1, x2, x3, x4)},
                           {2 * (x1 + x2), 2 * x1, 0.0, -f4(x1, x2, x3, x4)}};
        d1 = det4x4(B1) / det4x4(B);
        d2 = det4x4(B2) / det4x4(B);
        d3 = det4x4(B3) / det4x4(B);
        d4 = det4x4(B4) / det4x4(B);
        x1 += d1;
        x2 += d2;
        x3 += d3;
        x4 += d4;
        c++;
        printf("%d %15.5f  %15.5f  %15.5f  %15.5f  %15.5f  %15.5f  %15.5f  %15.5f   %15.5f  %15.5f  %15.5f  %15.5f\n",
               c,
               x1, x2, x3, x4, d1, d2, d3, d4, f1(x1, x2, x3, x4), f2(x1, x2, x3, x4), f3(x1, x2, x3, x4),
               f4(x1, x2, x3, x4));
    } while (fabs(d1) > PERS || fabs(d2) > PERS || fabs(d3) > PERS || fabs(d4) > PERS);

    return 0;
}