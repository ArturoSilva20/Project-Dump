#include <iostream>
#include <vector>
#include <string>

bool check_same(std::string x, std::string y, int z){
    for (char j : x) {
        if (j != y[z])
            return 0;
        z++;
    }
    return 1;
}

void Find_target_string (std::string Array_A, std::vector<std::string> Array_B, std::vector<int> & Output_order, std::vector<std::string>& Output_array) {
    int i = 0;
    
    while (i < Array_A.size()) {
        for (std::string x: Array_B) {
            if (check_same(x, Array_A, i)) {
                Output_order.push_back(i);
                Output_array.push_back(x);    
            } 
        }
        i++;
    }
} 

int main() {
    std::string Array_A = "torranceoaklandrialtomarcooxnardchinofresnoirvineclovissimiorange";
    std::vector<std::string> Array_B = { "oxnard", "irvine", "orange", "marco" };
    std::vector<std::string> output_array;
    std::vector<int> output_order;

    Find_target_string(Array_A, Array_B, output_order, output_array);

    for (std::string x : output_array) {
        std::cout << x << ' ';
    }
    std::cout << '\n';
    for (int x : output_order) {
        std::cout << x << ' ';
    }
    std::cout << '\n';

}
