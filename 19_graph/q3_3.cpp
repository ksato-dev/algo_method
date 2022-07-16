#include <iostream>
#include <vector>
#include <queue>
#include <map>
#include <string>
#include <sstream>
#include <algorithm>

#define Graph(T) std::vector<std::vector<T>>
typedef unsigned long long ull;
typedef unsigned long ul;

template <class T>
void GetSplitStringVec(const std::string& raw_data, std::vector<T>* v) {
  // ref split string: https://marycore.jp/prog/cpp/std-string-split/
  std::stringstream ss{raw_data};
  std::string buf;
  while (std::getline(ss, buf, ' ')) {
    T data;
    std::istringstream iss(buf);
    iss >> data;
    v->push_back(data);
  }
}

int main() {
    std::string raw_string;
    std::getline(std::cin, raw_string);
    std::vector<int> hw;
    GetSplitStringVec<int>(raw_string, &hw);
    const int h = hw[0];
    const int w = hw[1];

    std::getline(std::cin, raw_string);
    std::vector<int> xy0_xy1;
    GetSplitStringVec<int>(raw_string, &xy0_xy1);
    const int x0 = xy0_xy1[0];
    const int y0 = xy0_xy1[1];
    const int x1 = xy0_xy1[2];
    const int y1 = xy0_xy1[3];

    std::vector<std::vector<int>> dist(h);
    std::vector<std::string> s_map(h);
    for (int i = 0; i < h; i++) {
        std::getline(std::cin, raw_string);
        s_map[i] = raw_string;
        dist[i] = std::vector<int>(w, -1);
    }
    dist[x0][y0] = 0;

    std::queue<std::pair<int, int>> todo;
    todo.push(std::make_pair(x0, y0));

    std::vector<int> dj_list = {1, 0, -1, 0};
    std::vector<int> di_list = {0, 1, 0, -1};

    while (!todo.empty()) {
        auto curr_cell = todo.front();
        todo.pop();
        const int curr_i = curr_cell.first;
        const int curr_j = curr_cell.second;

        for (int k = 0; k < 4; k++) {
            const int next_i = curr_i + di_list[k];
            const int next_j = curr_j + dj_list[k];

            const bool flag_i = (0 <= next_i && next_i < h);
            const bool flag_j = (0 <= next_j && next_j < w);
            if (!flag_i || !flag_j) continue;

            const bool flag_black = (s_map[next_i][next_j] == 'B');
            if (flag_black) continue;

            const bool flag_visited = (dist[next_i][next_j] != -1);
            if (flag_visited) continue;

            dist[next_i][next_j] = dist[curr_i][curr_j] + 1;
            todo.push(std::make_pair(next_i, next_j));
        }
    }

    std::cout << dist[x1][y1] << std::endl;

    return 0;
}
