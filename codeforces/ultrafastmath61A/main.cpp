#include <iostream>
#include <string>

using namespace std;

int main()
{
  string first, second;

  cin >> first >> second;

  for (size_t i = 0; i < first.length(); i++)
  {
    if (first[i] == second[i])
    {
      first[i] = '0';
    }
    else 
    {
      first[i] = '1';
    }
  }
  cout << first << endl;
  
  return 0;
}
