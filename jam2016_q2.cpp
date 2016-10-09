#include <iostream>
using namespace std;

class Stack {
public:
    Stack(string s) { cakes = s; }

    int count(string patt) {
        int counter = 0, z;
        z = cakes.find(patt);
        while (z != -1) {
            z = cakes.find(patt, z + patt.size());
            counter++;
        }
        return counter;
    }

    ~Stack() {;}

private:
    string cakes;
};


int main() {
    int T;
    cin >> T;
    for (int i = 1; i <= T; i++) {
        int minimum = 0;
        string file_cakes;
        cin >> file_cakes;
        Stack happy(file_cakes);
        minimum += happy.count("+-");
        minimum += happy.count("-+");
        minimum++;
        if (file_cakes.at(file_cakes.length() - 1) == '-')
            cout << "Case #" << i << ": " << minimum << endl;
        else
            cout << "Case #" << i << ": " << minimum - 1 << endl;
    }

    return 0;
}