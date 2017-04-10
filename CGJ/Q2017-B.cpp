#include <iostream>
#include <fstream>
using namespace std;

bool check_num(long int n) {
  string numb = to_string(n);
  long int i;
  int c = 0;
  for (i = 0; i < numb.length() - 1; i++) {
    if (numb.at(i) <= numb.at(i + 1)) {
      c++;
    }
  }
  if (c == numb.length() - 1)
    return true;
  else
    return false;
}

int main() {
  ifstream f1("/home/pavlos/ClionProjects/jam_2017_2/B-large.in");
  ofstream f2("/home/pavlos/ClionProjects/jam_2017_2/uz.out");
  string s;
  getline(f1, s);
  long int num;
  for (int i = 1; i <= 100; i++) {
    f1 >> num;
    cout << i << endl;
    int rem;
    while (num >= 0) {
      if (num > 0x10000)
        rem = 100;
      else
        rem = 1;
      if (check_num(num) == true) {
        f2 << "Case #" << i << ": " << num << endl;
        break;
      }
      num -= rem;
    }
  }
  f2.close();
  return 0;

}
