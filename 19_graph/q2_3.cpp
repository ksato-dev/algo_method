#include <iostream>
#include <vector>
#include <queue>
#include <map>
#include <string>
#include <sstream>
#include <algorithm>

typedef unsigned long long ull;
typedef unsigned long ul;

#define rep(T, i, n) for (T i = 0; i < (T)(n); i++)
#define Graph(T) std::vector<std::vector<T>>

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

template <class T>
const T dfs(const Graph(T) & graph, const T& node_id, const T& depth,
            std::vector<bool>* visited) {
  T ret_depth = depth;
  if (visited->at(node_id)) return ret_depth;
  visited->at(node_id) = true;

  for (auto adj_node_id : graph[node_id]) {
    if (visited->at(adj_node_id)) continue;
    // ret_depth = std::max(ret_depth, dfs<T>(graph, adj_node_id, depth + 1, visited));
    ret_depth = dfs<T>(graph, adj_node_id, depth + 1, visited);
  }
  return ret_depth;
}

int main() {
  std::string raw_str;
  std::getline(std::cin, raw_str);
  ul n = std::stoul(raw_str);

  std::vector<ul> p_list;
  std::getline(std::cin, raw_str);
  GetSplitStringVec<ul>(raw_str, &p_list);

  Graph(ul) graph(n);
  rep(ul, i, n - 1) {
    // 子から親への参照を登録
    graph[i + 1].push_back(p_list[i]);
  }

  // 子から根までの深さを調べる。
  std::cout << 0 << std::endl;  // 根は深さ０
  rep(ul, i, n - 1) {
    std::vector<bool> visited(n, false);
    ul depth = dfs<ul>(graph, i + 1, 0, &visited);
    std::cout << depth << std::endl;
  }

  return 0;
}
