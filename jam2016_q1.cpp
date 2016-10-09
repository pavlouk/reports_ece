#include <iostream>
using namespace std;

int store_digits(int M, int A[10]) {
    int sum = 0;
    while (M > 0) {
        int k = M % 10;
        if (A[k] != k) A[k] = k;
        M /= 10;
    }
    for (int i = 0; i <= 9; i++) sum += A[i];
    return sum;
}

int main() {
    int T, N, j;
    bool found = false;
    cin >> T;
    for (int i = 1; i <= T; i++) {
        j = 1;
        int A[10] = {-1, -1, -1, -1, -1, -1, -1, -1, -1, -1};
        cin >> N;
        while (!found) {
            int total_sum = store_digits(j * N, A);
            if (total_sum == 45) found = true;
            if (j >= 80) found = true;
            j++;
        }
        found = false;
        if (j < 80)
            cout << "Case #" << i << ": " << (j - 1) * N << endl;
        else
            cout << "Case #" << i << ": INSOMNIA" << endl;
    }
    return 0;
}