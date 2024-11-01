#include <iostream>
#include <string>

using namespace std;

int main()
{
  int num;
  cin >> num;
  string stones;
  cin >> stones;

  int removed = 0;

  for (int i=0; i<num; i++) {
    if (i == 0){
      continue;
    }
    if(stones[i] == stones[i-1])
    {
      removed++;
    }
  }
  cout << removed << endl;
  return 0;
}
