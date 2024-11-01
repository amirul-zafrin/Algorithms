#include <iostream>

using namespace std;

int main()
{
  long long number;
  cin >> number;

  int count;

  while(number != 0)
  {
    if (number % 10 == 4 || number % 10 == 7)
    {
      count++;
    }
    number /= 10;
  }

  if (count == 4 || count == 7)
  {
    cout << "YES" << endl;
  } else {
    cout << "NO" << endl;
  }
  return 0;
}
