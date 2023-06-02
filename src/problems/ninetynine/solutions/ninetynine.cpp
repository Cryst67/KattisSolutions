#include <cmath>
#include <iostream>

int main() {
  int n = 1;
  std::cout << n << std::endl;

  while (true) {
    std::cin >> n;
    if (n > 98) break;

    n += std::min(3 - n % 3, 2);

    std::cout << n << std::endl;
  }
}