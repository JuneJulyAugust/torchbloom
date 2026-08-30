# Applying Prim's Algorithm to a Distance Matrix

Source: https://www.mathacademy.com/topics/1416?courseId=109
Topic ID: 1416

## Prerequisites

- [Distance Matrices](./1392-distance-matrices.md)
- [Prim's Algorithm](./1402-prim-s-algorithm.md)

## Lesson

### Introduction

Recall that Prim's algorithm finds a minimum spanning tree of a connected, weighted graph $G.$ It follows a so-called greedy approach by starting from an arbitrary vertex and expanding the tree by adding the smallest edge that connects a visited vertex to an unvisited vertex.

One advantage of Prim's algorithm over other spanning-tree algorithms is that it can easily be applied to a distance matrix. The steps of Prim's algorithm applied to a distance matrix are as follows:

- **Step 1:** Begin by marking the column corresponding to the starting vertex.

- **Step 2:** Cancel out the row corresponding to the starting vertex.

- **Step 3:** While not all columns are marked, find the smallest distance $s$ among all the marked columns. Identify the corresponding row and column, denoted as $u$ and $v$. Then, mark the column $u$ to indicate that the vertex has been added to the tree. Cancel out the row $u$ corresponding to $s$ to prevent revisiting, and add the edge $v-u$ to the tree.

- **Step 4:** Repeat this process until all vertices are included in the minimum spanning tree, ensuring that the tree grows by selecting the smallest available edge at each step.

The pseudocode for Prim's algorithm on a distance matrix is the following:

It's easiest to understand the algorithm by following a concrete example, so let's do that.

### A Concrete Example

Let's use Prim's algorithm to find the minimum spanning tree of the weighted graph G with the distance matrix given above.

We start from the vertex $v_1,$ and proceed as follows:

Every vertex is now in our tree (every column has been marked), so the process is completed. The list of edges in our minimum spanning tree is given by the table on the right, and the total weight of the resulting minimum spanning tree is

$$



8 + 11 + 13 + 3 = 35.



$$

### Example: Applying One Iteration of Prim's Algorithm Using a Distance Matrix

#### Question

Consider the distance matrix of a weighted graph shown above.

Prim's algorithm for finding a minimum spanning tree is applied to the matrix, starting at the vertex $v_1,$ and after a few steps, we arrive at the configuration shown below. Which edge will be added to the tree at the next step of the algorithm?

#### Explanation

The pseudocode for Prim's algorithm on a distance matrix is the following:

So, at the next step of Prim's algorithm, we consider the smallest unselected distance over all marked columns ($v_1,$ and $v_2$). The smallest value is $3$ at the intersection of row $v_4$ and column $v_1.$

We cancel out the row $v_4$ and add $\boxed{\color{blue}v_1-v_4}$ of length $\boxed{\color{blue}3}$ to the tree.

### Example: Applying Prim's Algorithm to a Distance Matrix

#### Question

#### Explanation

The pseudocode for Prim's algorithm on a distance matrix is the following:

With that in mind, we proceed as follows:

The total weight of the resulting minimum spanning tree is

$$



3 + 10 + 7 + 6 + 2 = 28.



$$
