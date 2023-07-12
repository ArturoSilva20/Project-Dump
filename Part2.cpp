#include <iostream>
#include <vector>

int sum(int x, int y) {
    return (x + y);
}


std::vector<int> largest_sum(std::vector<int> V) {
    int b = 0;
    int e = 1;
    int n = V.size();
    for (int i = 0; i < (n - 1); i++) {
        for (int j = i + 1; j < n; j++) {
            //std::cout << i << ',' << j << '\n';
            if (sum(V[i], V[j]) > sum(V[b], V[e])) {
                b = i;
                e = j;
            }
        }
    }

    return { b, e };
}

int main()
{

    std::vector<int> input = { 6,1, 9, -33, 7, 2, 9, 1, -3, 8, -2, 9, 12, -4 };
    std::vector<int> output = largest_sum(input);
    std::cout << "Largest sum pair: " << input[output[0]] << ',' << input[output[1]] << '\n';


}
