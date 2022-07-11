#include <iostream>
#include <vector>
#include <queue>
#include <map>
#include <string>
#include <sstream>
#include <algorithm>

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

#define Graph(T) std::vector<std::vector<T>>

template <class T>
void dfs(const Graph(T) & graph, const T& node_id, std::vector<bool>* visited) {
  if (visited->at(node_id)) return;
  std::cout << node_id << " ";
  visited->at(node_id) = true;

  for (auto adj_node_id : graph[node_id]) {
    if (visited->at(adj_node_id)) continue;
    dfs<T>(graph, adj_node_id, visited);
  }
}

int main() {
  std::string raw_str;
  std::getline(std::cin, raw_str);
  ul n = std::stoul(raw_str);

  std::vector<ul> p_list;
  std::getline(std::cin, raw_str);
  GetSplitStringVec<ul>(raw_str, &p_list);

  Graph(ul) graph(n);

  for (ul i = 0; i < n; i++) {
      std::make_heap(graph[i].begin(), graph[i].end());
  }

  for (ul i = 1; i < n; i++) {
    ul p = p_list[i - 1];
    graph[p].push_back(i);
    std::push_heap(graph[p].begin(), graph[p].end());
  }

  for (ul i = 0; i < n; i++) {
    std::sort_heap(graph[i].begin(), graph[i].end());
  }

  std::vector<bool> visited(n, false);

  dfs<ul>(graph, 0, &visited);
  std::cout << std::endl;

  return 0;
}
