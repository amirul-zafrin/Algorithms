#include <iostream>
#include <cmath>

using namespace std;

bool isPrime(int n);

int main()
{
  int n, m;
  cin >> n >> m;

  if (n >= m)
  {
    cout << "NO";
  }
  if (!isPrime(m))
  {
    cout << "NO";
    return 0;
  }
  for (int i = n + 1; i < m-1; i++)
  {
    if (isPrime(i))
    {
      cout << "NO";
      return 0;
    }
  }
  cout << "YES" << endl;
}

bool isPrime(int n)
{
  if (n <= 3) return true;
  if (n % 2 == 0 || n % 3 == 0) return false;

  for (int i = 5; i*i<= n; i+=6)
  {
    if (n % i == 0 || n % (i + 2) == 0) return false;
  }
  return true;
}
