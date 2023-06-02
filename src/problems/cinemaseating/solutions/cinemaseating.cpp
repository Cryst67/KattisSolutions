#include <iostream>
#include <vector>
using namespace std;

auto main() -> int {
    int R, C; cin >> R >> C;
    vector<vector<int>> grid(R, vector<int>(C));
    int n; cin >> n;
    for(int i = 0; i < n; i++){
        int r, c; cin >> r >> c;
        grid[r - 1][c - 1] = 1;
    }
    vector<int> v;
    for(int i = 0; i < 9; i++){
        v.push_back(0);
    }
    for(int i = 0; i < R; i++){
        for(int j = 0; j < C; j++){
            int neighbors = 0;
            if(grid[i][j] == 1){
                if(i != 0 && grid[i - 1][j] == 1) neighbors += 1; //up
                if(i != R - 1 && grid[i + 1][j] == 1) neighbors +=1; //down
                if(j != 0 && grid[i][j - 1] == 1) neighbors += 1; //left
                if(j != C - 1 && grid[i][j + 1] == 1) neighbors += 1; //right
                if(i != 0 && j != 0 && grid[i - 1][j - 1] == 1) neighbors += 1; //diag top-left
                if(i != 0 && j != C - 1 && grid[i - 1][j + 1] == 1) neighbors += 1; //diag top-right
                if(i != R - 1 && j != 0 && grid[i + 1][j - 1] == 1) neighbors += 1; //diag bottom-left
                if(i != R - 1 && j != C - 1 && grid[i + 1][j + 1] == 1) neighbors += 1; //fiag bottom-right
                v[neighbors] += 1;
            }
        }
    }
    for(auto k : v){
        cout << k << ' ';
    }
    cout << '\n';
    return 0;
}