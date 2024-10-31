#include <iostream>
#include <cstring>

using namespace std;

int main()
{
  string word;
  cin >> word;
  int lowC=0, upC=0;
  for (int i=0; i<word.size(); i++){
    if(isupper(word[i])) {
      upC++;
    } else {
      lowC++;
    }
  }

  if (upC > lowC) {
    char ch;
    for(int i=0; i<word.size(); i++){
      ch=toupper(word[i]);
      cout << ch;
    }
  } else {
    char ch;
    for(int i=0; i<word.size(); i++){
      ch=tolower(word[i]);
      cout << ch;
    }
  }
  return 0;
}
