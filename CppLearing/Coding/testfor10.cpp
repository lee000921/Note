#include <iostream>
#include <algorithm>
#include <vector>
#include <list>
#include <numeric>
using namespace std;
int main()
{
    vector<int> a{1,2,3,4,5,6,7,3,2,4,5,10};
    list<string> l{"hello","world","hello","abcnsd","ssaa"};
    auto ans = count(a.begin(),a.end(),2);
    ans = count(l.begin(),l.end(),"hello");

    auto res = accumulate(a.cbegin(),a.cend(),0);
    cout << res << endl;
    return 0;
}