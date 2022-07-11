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

//! 子孫の数を調べる (ver1)
template <class T>
const T dfs(const Graph(T) & graph, const T& node_id,
            std::vector<bool>* visited) {
  if (visited->at(node_id)) return 0;
  visited->at(node_id) = true;

  T ret_children_cnt = 1;
  for (auto adj_node_id : graph[node_id]) {
    if (visited->at(adj_node_id)) continue;
    ret_children_cnt += dfs<T>(graph, adj_node_id, visited);
  }
  return ret_children_cnt;
}

//! 子孫の数を調べる (ver2)
template <class T>
void dfs(const Graph(T) & graph, const T& node_id, std::vector<bool>* visited,
         T* cnt) {
  if (visited->at(node_id)) return;
  visited->at(node_id) = true;

  (*cnt)++;
  for (auto adj_node_id : graph[node_id]) {
    if (visited->at(adj_node_id)) continue;
    dfs<T>(graph, adj_node_id, visited, cnt);
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
  rep(ul, i, n - 1) {
    // 親から子への参照を登録
    ul p = p_list[i];
    graph[p].push_back(i + 1);
  }

  // 子から根までの深さを調べる。
  rep(ul, i, n) {
    std::vector<bool> visited(n, false);
    // const ul node_num = dfs<ul>(graph, i, &visited);
    ul node_num = 0;
    dfs<ul>(graph, i, &visited, &node_num);
    const ul children_num = node_num - 1;  // 自分を引く。
    std::cout << children_num << std::endl;
  }

  return 0;
}
