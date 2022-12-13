#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main() {

    // c++ 속도 향상을 위한... 주문 (?)
    // https://jaimemin.tistory.com/1521
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    // 동적 string 배열
    vector<string> v;
    int n;
    cin >> n;
    v.resize(n);
    string person, inout;
    for (int i = 0; i < n; i++) {
        cin >> person >> inout;
        v[i] = person;
    }

    // 역순 정렬
    sort(v.rbegin(), v.rend());

    for (int i = 0; i < v.size(); i++) {
        if (i + 1 < v.size() && v[i] == v[i + 1]) i++; // 동일한 입력값이 있다면 pass(정렬되어 있으므로)
        else cout << v[i] << '\n';
    }
    return 0;
}
