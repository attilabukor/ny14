#include <iostream>
#include <ostream>
#include <string>
#include <cmath>
#include <list>
#include <map>

std::map<std::pair<uint64_t, int>, long> stone_cache;

uint64_t blink(long stone, int count) {
  std::pair<uint64_t, int> cache_key(stone, count);
  if (count == 0) {
    //std::cout << stone << std::endl;
    return 1;
  }

  if (stone == 0) {
    return blink(1, count - 1);
  }

  auto it = stone_cache.find(cache_key);
  if (it != stone_cache.end()) {
    return stone_cache[cache_key];
  }

  uint64_t log;

  if (stone < 10 || (stone >= 100 && stone < 1000) ||
      (stone >= 10000 && stone < 100000) ||
      (stone >= 1000000 && stone < 10000000) ||
      (stone >= 100000000 && stone < 1000000000) ||
      (stone >= 10000000000 && stone < 100000000000) ||
      (stone >= 1000000000000 && stone < 10000000000000) ||
      (stone >= 100000000000000 && stone < 1000000000000000) ||
      (stone >= 10000000000000000 && stone < 100000000000000000)) {
    uint64_t res = blink(stone * 2024, count - 1);
    stone_cache[cache_key] = res;
    return res;
  }

  uint64_t divisor;
  if (stone >= 10 && stone < 100) {
    divisor = 10;
  } else if (stone >= 1000 && stone < 10000) {
    divisor = 100;
  } else if (stone >= 100000 && stone < 1000000) {
    divisor = 1000;
  } else if (stone >= 10000000 && stone < 100000000) {
    divisor = 10000;
  } else if (stone >= 1000000000 && stone < 10000000000) {
    divisor = 100000;
  } else if (stone >= 100000000000 && stone < 1000000000000) {
    divisor = 1000000;
  } else if (stone >= 10000000000000 && stone < 100000000000000) {
    divisor = 10000000;
  } else if (stone >= 1000000000000000 && stone < 10000000000000000) {
    divisor = 100000000;
  } else if ((log = (uint64_t )log10(stone)) % 2 == 1) {
    divisor = pow(10, (uint64_t)(log + 1) / 2);
  }

  if (divisor > 0) {
    uint64_t res = blink(stone / divisor, count - 1) + blink(stone % divisor, count - 1);
    stone_cache[cache_key] = res;
    return res;
  }

  uint64_t res = blink(stone * 2024, count - 1);
  stone_cache[cache_key] = res;
  return res;
}


void print(const std::list<uint64_t>& stones) {
  for (uint64_t stone : stones) {
    std::cout << stone << " ";
  }
  std::cout << std::endl;
}

int main() {
  std::string chunk;
  std::list<uint64_t> stones;
  while (std::getline(std::cin, chunk, ' ')) {
    stones.emplace_back(std::stoi(chunk));
  }

  uint64_t num_stones = 0;
  for (const auto& stone : stones) {
    num_stones += blink(stone, 75);
  }
  std::cout << num_stones << std::endl;

  return 0;
}
