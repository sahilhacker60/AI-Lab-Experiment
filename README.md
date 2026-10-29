 **A curated collection of 10 foundational AI search techniques, game-playing agents, and constraint satisfaction problems.**

  [![Python](https://img.shields.io/badge/Language-Code-blue.svg)](#)
  [![Python](https://img.shields.io/badge/Language-Python%203-blue.svg)](#)
  [![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/sohamswain26)

</div>
@@ -17,18 +17,18 @@ Welcome to my AI playground. This repository serves as a practical implementatio

Here are the 10 algorithms and problems solved in this repository, broken down by their mathematical and logical categories:

| Algorithm / Problem | AI Category | Core Concept |
| :--- | :--- | :--- |
| **Breadth-First Search (BFS)** | Uninformed Search | Scans environments level-by-level to guarantee the shortest path in unweighted spaces. |
| **Depth-First Search (DFS)** | Uninformed Search | Dives deep into a single path before backtracking, minimizing memory usage. |
| **A* (A-Star)** | Informed Search | Combines exact path cost with heuristic guessing to find the optimal route efficiently. |
| **Hill Climbing** | Local Search | Continuously steps toward mathematical peaks to find the best local solution. |
| **Minimax** | Adversarial Search | Calculates moves by assuming the opponent will always play optimally. |
| **Alpha-Beta Pruning** | Adversarial Search | Optimizes Minimax by ignoring mathematical branches that cannot affect the final outcome. |
| **Tic-Tac-Toe** | Game Theory | A complete environment testing adversarial decision-making agents. |
| **8 Queens Puzzle** | Constraint Satisfaction | Places 8 chess queens on a board without any two threatening each other. |
| **Traveling Salesman (TSP)** | Optimization | Calculates the shortest possible loop connecting a set of coordinates. |
| **Water Jug Problem** | State-Space Search | Reaches a target volume using two ungraduated jugs and strict mathematical constraints. |
| Algorithm / Problem | Script | AI Category | Core Concept |
| :--- | :--- | :--- | :--- |
| **Breadth-First Search (BFS)** | [`BFS.py`](BFS.py) | Uninformed Search | Scans environments level-by-level to guarantee the shortest path in unweighted spaces. |
| **Depth-First Search (DFS)** | [`DFS.py`](DFS.py) | Uninformed Search | Dives deep into a single path before backtracking, minimizing memory usage. |
| **A* (A-Star)** | [`A_algorithm.py`](A_algorithm.py) | Informed Search | Combines exact path cost with heuristic guessing to find the optimal route efficiently. |
| **Hill Climbing** | [`hill_climbing.py`](hill_climbing.py) | Local Search | Continuously steps toward mathematical peaks to find the best local solution. |
| **Minimax** | [`minimax_algorithm.py`](minimax_algorithm.py) | Adversarial Search | Calculates moves by assuming the opponent will always play optimally. |
| **Alpha-Beta Pruning** | [`alpha_beta_pruning.py`](alpha_beta_pruning.py) | Adversarial Search | Optimizes Minimax by ignoring mathematical branches that cannot affect the final outcome. |
| **Tic-Tac-Toe** | [`tic_tac_toe.py`](tic_tac_toe.py) | Game Theory | A complete environment testing adversarial decision-making agents. |
| **8 Queens Puzzle** | [`eight_queen.py`](eight_queen.py) | Constraint Satisfaction | Places 8 chess queens on a board without any two threatening each other. |
| **Traveling Salesman (TSP)** | [`tsp.py`](tsp.py) | Optimization | Calculates the shortest possible loop connecting a set of coordinates. |
| **Water Jug Problem** | [`water_jug.py`](water_jug.py) | State-Space Search | Reaches a target volume using two ungraduated jugs and strict mathematical constraints. |

---

@@ -38,4 +38,15 @@ To run these algorithms locally, pull the code to your machine:

**1. Clone the repository**
```bash
git clone [https://github.com/sohamswain26/AI_Codes.git](https://github.com/sohamswain26/AI_Codes.git)
git clone https://github.com/sohamswain26/AI_Codes.git
cd AI_Codes
```

**2. Run any algorithm**
Each code includes sample execution traces under `#output` at the bottom of the script.
```bash
python BFS.py
python A_algorithm.py
python minimax_algorithm.py
python alpha_beta_pruning.py
```