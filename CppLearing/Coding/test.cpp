#include <iostream>
#include <vector>
using namespace std;
int main()
{
    vector<int> c1{1,2,3};
    vector<int> c2{3,4,5};
    c1.swap(c2);
    for(int i=0;i<3;i++)
        cout << c1[i] << " ";
    cout << endl;
    for(int i=0;i<3;i++)
        cout << c2[i] << " ";
    cout << endl;
    vector<int> c3;
    c3.push_back(10);
    for(int i=0;i<=35;i++)
        c3.push_back(i);
    c3.reserve(100);
    cout << c3.size() << " " << c3.capacity() << endl;
    c3.shrink_to_fit();
    cout << c3.capacity() << endl;

    auto f = [](const int& a,const int& b){ return a+b; };
    cout << f(3,9) << endl;

    int a = 66;
    auto f1 = [a](int &b){ return a + b;};
    for(int i=0;i<10;i++)
    {
        cout << f1(i) << " ";
    }
    cout << endl;
    return 0;
}