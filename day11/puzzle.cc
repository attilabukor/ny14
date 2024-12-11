#include <iostream>
#include <ostream>
#include <string>
#include <cmath>
#include <list>

void blink(std::list<long>& stones) {
  for (auto it = stones.begin(); it != stones.end(); ++it) {
    if (*it == 0) {
      *it = 1;
    } else {
      long log = (long)log10(*it);
      if (log % 2 == 1) {
        long divisor = pow(10, (long)(log + 1) / 2);
        *it /= divisor;
        stones.insert(it, *it % divisor);
      } else {
        *it *= 2024;
      }
    }
  }
}

void print(const std::list<long>& stones) {
  for (long stone : stones) {
    std::cout << stone << " ";
  }
  std::cout << std::endl;
}

int main() {
  std::string chunk;
  std::list<long> stones;
  while (std::getline(std::cin, chunk, ' ')) {
    stones.emplace_back(std::stoi(chunk));
  }

  for (long i = 0; i < 75; ++i) {
    blink(stones);
  }

  int size = 0;
  for (const auto& stone : stones) {
    size++;
  }
  std::cout << size << std::endl;

  return 0;
}
