//Knapsack problem but with stocks

#include <iostream>
#include <vector>

using namespace std;



bool verify_combinations(int M, vector<vector<int>> items, vector<vector<int>> candidate) {
    int total_weight = 0;
    for (int i = 0; i < candidate.size(); i++) {
        total_weight += candidate[i][0];
    }
    if (total_weight <= M) {
        return true;
    }
    else {
        return false;
    }
        
}

int total_value(vector<vector<int>> candidate) {
    int total_value = 0;
    for (int i = 0; i < candidate.size(); i++) {
        total_value += candidate[i][1];
    }
    return total_value;
}

vector<vector<vector<int>>> generate_stock_combinations(vector<vector<int>> set) {
    vector<vector<vector<int>>> subset;
    vector<vector<int>> empty;
    subset.push_back(empty);
    for (int i = 0; i < set.size(); i++)
    {
        vector<vector<vector<int>>> subsetTemp = subset;

        for (int j = 0; j < subsetTemp.size(); j++)
            subsetTemp[j].push_back(set[i]);

        for (int j = 0; j < subsetTemp.size(); j++)
            subset.push_back(subsetTemp[j]);  
    }
    return subset;
}

vector<vector<int>> stock_maximization(int M, vector<vector<int>> items) {
    vector<vector<int>> best;
    best.clear();

    vector<vector<vector<int>>> stock_combinations = generate_stock_combinations(items);

    for (int i = 0; i < stock_combinations.size(); i++) {

        if (verify_combinations(M, items, stock_combinations[i])) {
            if (best.empty() || total_value(stock_combinations[i]) > total_value(best)) {
                best = stock_combinations[i];
            }
        }
    }

    return best;
}


void knapsack_dynammic(int M, vector<vector<int>>items) {
    int n = items.size();
    
    //int* mat = new int [n+1][M+1];
    int** mat;
    
    mat = new int* [n + 1];
    for (int i = 0; i < n + 1; i++) {
        mat[i] = new int [M + 1];
    }

    for (int i = 0; i < M; i++) {
        mat[0][i] = 0;
    }
    for (int i = 0; i < n; i++) {
        mat[n][0] = 0;
    }
    for (int i = 1; i < n; i++) {
        for (int j = 1; j < M; j++) {
            mat[i][j] = -1;
        }
    }

    for (int i = 1; i < n; i++) {
        for (int j = 0; j < M; j++) {
            mat[i][j] = max(mat[i - 1][j], mat[i - 1][j - items[i][0]] + items[i][1]);
        }
    }
    
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < M; j++) {
            cout << mat[i][j] << ' ';
        }
        cout << '\n';
    }
    
}




int main()
{
    vector<vector<int>> set = { {1,2},{3,3},{5,6},{6,7} };
    vector<vector<int>> greatest = stock_maximization(10, set);
    for (vector<int> x : greatest) {
        for (int y : x) {
            cout << y << ' ';
        }
        cout << '\n';
    }

    knapsack_dynammic(10, set);
}
