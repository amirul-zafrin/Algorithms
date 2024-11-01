#include <iostream>
#include <cstring>

using namespace std;

int main()
{
  string word;

  cin >> word;

  if (!word.empty())
  {
    word[0] = toupper(word[0]);
  }
  cout << word;
}
