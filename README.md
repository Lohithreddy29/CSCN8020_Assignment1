# CSCN8020 – Assignment 1
Reinforcement Learning (Gridworld + Monte Carlo + Importance Sampling)

This repository contains my full solution for **CSCN8020 Assignment 1**.  
All problems are implemented in a single Jupyter Notebook, with supporting Python modules stored in the `src/` folder.

---

# 📁 Repository Structure

| Path | Description |
| --- | --- |
| **CSCN8020_Assignment1/** | Root folder of the assignment |
| ├── **CSCN8020_Assignment1.ipynb** | Full assignment notebook (Problems 1–4, math, code, talking points) |
| ├── **README.md** | Project description and instructions |
| ├── **requirements.txt** | Python dependencies for reproducibility |
| ├── **.gitignore** | Excludes venv, cache, logs, and temporary files |
| ├── **src/** | Source code folder (object‑oriented design) |
| &nbsp;&nbsp;&nbsp;&nbsp;├── **environments.py** | Gridworld environment classes |
| &nbsp;&nbsp;&nbsp;&nbsp;├── **agents.py** | Value Iteration, In‑Place VI, and Monte Carlo agents |
| &nbsp;&nbsp;&nbsp;&nbsp;└── **utils.py** | Helper utilities (logging, shared functions) |
| └── **logs/** | Logging output folder |
| &nbsp;&nbsp;&nbsp;&nbsp;└── **assignment.log** | Auto‑generated log file showing algorithm execution |
---

## 🧠 Contents

### Problem 1
Policy Evaluation on a 2×2 Gridworld.

### Problem 2
Value Iteration on a 2×2 Gridworld (UP‑only policy).

### Problem 3
5×5 Gridworld:
- Standard Value Iteration
- In‑Place Value Iteration
- Optimal Value Function V*
- Optimal Policy π*
- Comparison & discussion

### Problem 4
Off‑Policy Monte Carlo Prediction using:
- Ordinary Importance Sampling
- Weighted Importance Sampling

---

## ▶️ How to Run

1. Clone the repository
2. Open `CSCN8020_Assignment1.ipynb` in Jupyter or VS Code
3. Run all cells from top to bottom

All code uses only **Python + NumPy**.

---
  

