#include <iostream>

int fibonacci(int n) {
    if (n < 0)
        return -1;
    if (n == 0)
        return 0;
    else if (n == 1)
        return 1;
    else;
    return (fibonacci(n - 1) + fibonacci(n - 2));
}



int fibonacci_golden(int n) {
    int term = (pow((1 + sqrt(5)), n) - pow((1 - sqrt(5)), n)) / (pow(2, n) * sqrt(5));
    return term;
}
int fibonacci_golden4(int n, int p) {
    int term = fibonacci_golden(p) * pow(1.61803, (n - p));
    return term;
}
int fibonacci_golden5(int n) {
    int term = (fibonacci_golden(n) * 1.61803);
    return term; // returns nth + 1 term
}

int main() {
    int x;
    int p;
    std::cout << "Fibonacci Equation 5\nEnter term: ";
    std::cin >> x;
    std::cout << "Output: " << fibonacci_golden5(x) << "\nEnter term: ";
    std::cin >> x;
    std::cout << "Output: " << fibonacci_golden5(x) << '\n';
    /*
    for (int i = 2; i < x; i++) {
        std::cout << fibonacci_golden4(i,p) << '\n';

    }
    */
}
