#include <iostream>

using namespace std;

int main()
{
  int dim, x, y, z, xsum(0), ysum(0), zsum(0);
  cin >> dim;

  while (dim--)
  {
    cin >> x >> y >> z;
    xsum += x;
    ysum += y;
    zsum += z;
  }

  if (xsum == 0 && ysum == 0 && zsum == 0)
  {
    cout << "YES" << endl;
  } 
  else 
  {
    cout << "NO" << endl;
  }
  return 0;
}
