#include <iostream>
#include <vector>
#include <queue>
using namespace std;

enum Color { WHITE, GRAY, BLACK }; // Colors to represent the state of each vertex

void BFS(vector<vector<int>>& graph, int start) {
    int n = graph.size();
    vector<Color> colors(n, WHITE); // Initialize all vertices to white
    queue<int> q;

    q.push(start);
    colors[start] = GRAY;

    while (!q.empty()) {
        int u = q.front();
        q.pop();
        cout << "Visited: " << u << endl;

        for (int v : graph[u]) {
            if (colors[v] == WHITE) {
                q.push(v);
                colors[v] = GRAY;
            }
        }

        colors[u] = BLACK;
    }
}

int main() {
    // Example graph as an adjacency list
    vector<vector<int> > graph = {
        {1, 2},     // 0 is connected to 1 and 2
        {0, 3, 4},  // 1 is connected to 0, 3, and 4
        {0, 5},     // 2 is connected to 0 and 5
        {1},        // 3 is connected to 1
        {1},        // 4 is connected to 1
        {2}         // 5 is connected to 2
    };

    BFS(graph, 0); // Start BFS from vertex 0

    return 0;
}
