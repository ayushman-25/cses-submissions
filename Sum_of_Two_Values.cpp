#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, x; cin >> n >> x;
    map<int, int> mp;
    for (int i = 0; i < n; i++) {
        int v; cin >> v;
        if (mp[x - v]) {
            cout << mp[x - v] << " " << i + 1;
            return 0;
        }
        mp[v] = i + 1;
    }
    cout << "IMPOSSIBLE";
}