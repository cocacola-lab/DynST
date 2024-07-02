#include <bits/stdc++.h>
using std::cin;
using std::cout;
using std::cerr;

const double PI = acos(-1);
const double EARTH_RADIUS_KM = 6371.0;

double toRadians(double degrees) {
    return degrees * PI / 180.0;
}

double calculateDistance(double lat1, double lon1, double lat2, double lon2) {
    lat1 = toRadians(lat1);
    lon1 = toRadians(lon1);
    lat2 = toRadians(lat2);
    lon2 = toRadians(lon2);

    double dlon = lon2 - lon1;
    double dlat = lat2 - lat1;
    double a = pow(sin(dlat / 2), 2) + cos(lat1) * cos(lat2) * pow(sin(dlon / 2), 2);
    double c = 2 * atan2(sqrt(a), sqrt(1 - a));

    return EARTH_RADIUS_KM * c;
}

struct PointPair {
    double d;
    int i, j;
};


struct UnionFind {
    int n;
    std::vector<int> parent;
    UnionFind(int _n) : n(_n), parent(_n) {
        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }
    }
    int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }
    void merge(int x, int y) {
        int xx = find(x), yy = find(y);
        if (xx != yy) {
            parent[xx] = yy;
        }
    }
    bool same(int x, int y) {
        return find(x) == find(y);
    }
};

signed main(int argc, char* argv[]) {
    assert(argc >= 2);
    assert(freopen(argv[1], "r", stdin));
    assert(freopen(argv[2], "w", stdout));

    int n;
    cin >> n;
    std::vector<std::pair<double, double>> a(n);
    for (int i = 0; i < n; i++) cin >> a[i].first >> a[i].second;
    cerr << "the number of points: " << n << "\n";

    std::vector<bool> exist(n, true);
    int cnt_erase = 0;

    for (int i = 0; i < n; i++) {
        if (a[i].first < -90 || a[i].first > 90 || a[i].second < -180 || a[i].second > 180) {
            exist[i] = false;
            cnt_erase++;
        }
    }

    std::vector<PointPair> b;

    cerr << "the number of points that are out of range: " << cnt_erase << "\n";

    for (int i = 0; i < n; i++) {
        if (!exist[i]) continue;
        for (int j = i + 1; j < n; j++) {
            if (!exist[j]) continue;
            double d = calculateDistance(a[i].first, a[i].second, a[j].first, a[j].second);
            if (d < 50)b.push_back({ d, i, j });
        }
    }
    std::sort(b.begin(), b.end(), [](const PointPair& a, const PointPair& b) { return a.d < b.d; });
    auto uf = UnionFind(n);
    int cnt1 = 0, cnt2 = 0;

    std::vector<std::vector<std::pair<int, double>>> G(n);

    std::vector<std::pair<int, int>>  edges;

    for (int id = 0; id < (int)b.size(); id++) {
        auto i = b[id].i, j = b[id].j;
        auto d = b[id].d;

        if (!uf.same(i, j)) {
            uf.merge(i, j);
            cnt1++;
            G[i].push_back({ j, d });
            G[j].push_back({ i, d });
            edges.push_back({ i, j });
        }
    }

    std::vector<PointPair> one_degree_edges;
    for (int i = 0; i < n; i++) {
        if (!exist[i]) continue;
        for (int j = 0; j < n; j++) {
            if (i == j || !exist[j]) continue;
            if (G[i].size() <= 1) {
                double d = calculateDistance(a[i].first, a[i].second, a[j].first, a[j].second);
                if (d < 10) one_degree_edges.push_back({ d, i, j });
            }
        }
    }
    std::sort(one_degree_edges.begin(), one_degree_edges.end(), [](const PointPair& a, const PointPair& b) { return a.d < b.d; });
    std::vector<bool> vis(n);
    for (int id = 0; id < (int)one_degree_edges.size(); id++) {
        auto i = one_degree_edges[id].i, j = one_degree_edges[id].j;
        auto d = one_degree_edges[id].d;
        if (!vis[i] && !vis[j]) {
            std::vector<double> dis(n, 1e9);
            dis[i] = 0;

            // spfa
            std::queue<int> q;
            q.push(i);
            while (!q.empty()) {
                int u = q.front();
                q.pop();
                for (auto p : G[u]) {
                    auto v = p.first;
                    auto w = p.second;
                    if (dis[v] > dis[u] + w) {
                        dis[v] = dis[u] + w;
                        q.push(v);
                    }
                }
            }
            if (dis[j] > d * 4) {
                vis[i] = vis[j] = 1;
                G[i].push_back({ j, d });
                G[j].push_back({ i, d });
                cnt2++;
                edges.push_back({ i,j });
            }
        }
    }

    cerr << "totol edges: " << " " << cnt1 + cnt2 << "\n";
    cerr << "extra edges: " << " " << cnt2 << "\n";

    cout << "from,to,cost\n";
    for (int i = 0; i < (int)edges.size(); i++) {
        cout << edges[i].first << "," << edges[i].second << ",1\n";
    }

    return 0;
}