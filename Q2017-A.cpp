#include <iostream>
#include <fstream>
using namespace std;

class Stack {
 public:
  int len_row;
  int len_flipper;
  string row;

  Stack(string s) {
    cakes = s;
    row = s;
    len_row = cakes.find(' ');
    string kappa = cakes.substr(len_row, cakes.length());
    pancakes = cakes.substr(0, len_row - 1);
    len_flipper = stoi(kappa);
  }

  int count(string patt) {
    int counter = 0, z;
    z = pancakes.find(patt);
    while (z != -1) {
      z = pancakes.find(patt, z + patt.size());
      counter++;
    }
    return counter;
  }

  ~Stack() {;}

 private:
  string cakes;
  string pancakes;
};


int main() {
  ifstream f1("/home/pavlos/ClionProjects/jam2017_1/B-small-attempt0.in");
  ofstream f2("/home/pavlos/ClionProjects/jam2017_1/Hz.out");
  int T = 100;
  //f1 >> T;
  string s;
  getline(f1, s);
  for (int i = 1; i <= T; i++) {
    int sets = 0;
    string file_cakes;
    getline(f1, file_cakes);
    Stack happy(file_cakes);
    sets += happy.count("+-");
    sets += happy.count("-+");
    if (happy.len_flipper >= happy.len_row) {
      if (sets == 0 && happy.row.at(0) == '+')
        f2 << "Case #" << i << ": " << 0 << endl;
      else if (sets == 0 && happy.row.at(0) == '-')
        f2 << "Case #" << i << ": " << 1 << endl;
      else if (sets != 0 || happy.row.at(0) == '-')
        f2 << "Case #" << i << ": " << "IMPOSSIBLE" << endl;
    } else {
      f2 << "Case #" << i << ": " << sets << endl;
    }
  }
  f2.close();
  return 0;
}