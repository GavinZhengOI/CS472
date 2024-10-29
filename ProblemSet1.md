# Problem Set 1

## Problem 1

### A. Show the complete state space for the above example.

[],[C],[D],[DG],[DGH],[E],[EF],[EFH],[EG],[EGH],[EH],[F],[FG],[FGH],[G],[GH],[H]

#### B. Suppose that you use a depth-first search to explore the state space. Which of the states in (A) will you generate, and in what order?

[],[C],[D],[DG],[DGH]->end at [DGH]

#### C. Suppose that you use a breadth-first search to explore the state space. Which of the states in (A) will you generate, and in what order?

[],[C],[D],[E],[F],[G],[H],[DG],[EF],[EG],[EH],[FG],[GH],[DGH]->end at [DGH]

## Problem 2

- Q: Is the state space a tree? A: Yes it is.
- Q: Give an upper bound on the depth of the state space. A: $O(N)$
- Q: What is the branching factor? A: Is N.
- Q: Is the depth of the shallowest goal known in advance? A: We don't know that. But we know its at most N.

## Problem 3

#### A.

Define goal space as a list containing alphabetical objects. There won't be any edges between any of the objects in the list.

Start State: empty list [].

Successor to a state: The successor of state $S$, is state $S+[k]$, where $k$ is an object that alphabetically later than the last element in $S$ and $\forall e \in S$, there is no edge between $e$ and $k$.

Goal State: Is the state $S$ that $len(S)=K$. Where $len$ represent the length of a list.

#### B.

I know the depth of the goal state, which is K. We should use iterative deepening.