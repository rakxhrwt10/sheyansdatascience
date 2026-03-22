#include <iostream>
using namespace std;
int main()
{

    int arr[5] = {2, 2, 2, 2, 5};
    int key = 2;
    int mid;
    int i = 0;
    int j = sizeof(arr) / sizeof(arr[0]) - 1;
    int ans=-1;

    while (i <= j)
    {
        mid = i + (j - 1) / 2;

        if (arr[mid] == key)
        {
          ans=mid;
            cout << "element persent at first occurence " << ans;
            return 0;
        }

        else if (arr[mid] > key)
        {

            j = mid - 1;
        }

        else
        {

            i = mid + 1;
        }
    }
    cout << "element not found";
}