#include <iostream>
#include <cmath>
using namespace std;

bool isPrime(long long int potential, int& m_div) {
    if (potential < 2) return false;
    for (int i = 2; i <= sqrt(potential); i++) {
        if (potential % i == 0) {
            m_div = i;
            return false;
        }
    }
    m_div = 0;
    return true;
}

long long int BaseInterpreter(long long int potential, int base) {
    //Interpretation: jc(N-1)*base^(N-1) + jc(N-2)*base^(N-2) + .. + jc(0),
    // jc(i) in set {0, 1}, i = 0, .., N-1
    int arr[32], r, i = 0;
    long long int sum = 0;
    while (potential != 0) {
        r = potential % 2;
        arr[i++] = r;
        potential /= 2;
    }
    for (int j = i - 1; j >= 0; j--)
        sum += arr[j] * pow(base, j);
    return sum;
}

void Dec2Bin(long long int num) {
    int arr[32], i = 0, r;
    while (num != 0) {
        r = num % 2;
        arr[i++] = r;
        num /= 2;
    }
    for (int j = i - 1; j >= 0; j--)
        cout << arr[j];
}

int main() {
    int n = 1;
    cout << "Case #1:" << endl;
    for (int i = 0; i <= 16383; i++) {
        long long int potential = 2 * i + 32769; //Bit shifting and 1{N-2}1 type coin
        int divisor = 0;
        bool cond1 = isPrime(potential, divisor);
        if (!cond1) {
            int divisors[9] = {0, 0, 0, 0, 0, 0, 0, 0, 0};
            int s = 0;
            for (int j = 2; j <= 10; j++) {
                long long int derived = BaseInterpreter(potential, j);
                bool cond2 = isPrime(derived, divisor);
                if (!cond2)
                    divisors[j - 2] = divisor;
            }
            for (int j = 0; j <= 9; j++)
                if (divisors[j] == 0)
                    s++;
            if (s == 0) {
                n++;
                Dec2Bin(potential);
                cout << " ";
                for (int j = 0; j < 9; j++)
                    cout << divisors[j] << " ";
                cout << endl;
            }
            if (n > 50) return 0;
        }
    }
}
