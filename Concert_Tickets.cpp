#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    multiset<int> h;
    for (int i = 0; i < n; i++) {
        int x; cin >> x;
        h.insert(x);
    }
    for (int i = 0; i < m; i++) {
        int ti; cin >> ti;
        auto it = h.upper_bound(ti);
        if (it == h.begin()) {
            cout << "-1\n";
            continue;
        }
        it--;
        cout << *it << '\n';
        h.erase(it);
    }
}