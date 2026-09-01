# Modeling With Systems of Linear Inequalities

Source: https://www.mathacademy.com/topics/6360?courseId=127
Topic ID: 6360

## Prerequisites

- [Modeling With Two-Variable Linear Inequalities](../../../traditional/lessons/algebra-i/1320-modeling-with-two-variable-linear-inequalities.md)
- [Modeling With Compound Inequalities](../../../traditional/lessons/algebra-i/6224-modeling-with-compound-inequalities.md)

## Lesson

### Introduction

In this lesson, we'll learn how to translate constraints into systems of linear inequalities, represent them symbolically, and interpret their solutions. Let's start with an example.

Suppose a bakery manager is buying $x$ trays and $y$ boxes for a catering order. The manager needs to purchase at least $36$ items in total, but wants to spend no more than $180.$ Each tray costs $8$ and each box costs $2.$

To model this situation, we translate each condition into an inequality:

- The total number of items is equal to $x+y.$ There must be at least $36$ items in total, so we have

- Since each tray costs $8$ and each box costs $2,$ their total cost is $8x + 2y.$ We're told that it cannot exceed $180.$ So we have

Therefore, putting it all together, the system of inequalities that models this situation is the following:

$$


\begin{aligned}𝑥+𝑦≥36 \\ 8𝑥+2𝑦≤180\end{aligned}


$$

This system models all possible choices of trays and boxes that both satisfy the minimum item requirement and stay within the budget.

**Watch out!** We consider only non-negative pairs, as the number of items can't be negative.

### Checking a Possible Solution to a System

For the system

$$


\begin{aligned}𝑥+𝑦≥36 \\ 8𝑥+2𝑦≤180\end{aligned}


$$

every pair $(x,y)$ with $x,y \geq 0$ that satisfies both inequalities represents a solution of the system. For example, consider the pair $(x,y) = (10,40).$ Substituting into both inequalities, we obtain the following:

$$


\begin{aligned}10+40≥36 \\ 8(10)+2(40)≤180\end{aligned}


$$

Since both inequalities are satisfied, the point $(10,40)$ is a solution. Thus, buying $10$ trays and $40$ boxes is a valid option for the manager in our original problem.

Now, consider $(x,y) = (10,80).$ Substituting into both inequalities, we obtain the following:

$$


\begin{aligned}10+80≥36 \\ 8(10)+2(80)≤180\end{aligned}


$$

Since the second inequality does not hold, the point $(10,80)$ is *not* a solution. Thus, buying $10$ trays and $80$ boxes is not a valid option for the manager in our original problem.

### Strict vs. Non-Strict Inequalities

In the bakery example from the beginning of the lesson, we wrote the system

$$


\begin{aligned}𝑥+𝑦≥36 \\ 8𝑥+2𝑦≤180\end{aligned}


$$

because the problem said that the manager wanted

- to buy *at least $36$ items*, and

- to spend *no more than $180.$*

Both these phrases lead to *non-strict inequalities* ($\geq$, $\leq$).

But if the manager instead wants *more than $36$ items*, then the first inequality in the system becomes strict, as follows:

$$


\begin{aligned}𝑥+𝑦\,>\,36 \\ 8𝑥+2𝑦≤180\end{aligned}


$$

The most common phrases and the corresponding inequality symbols are listed in the table below.

### Example: Modeling a Situation Using Two Inequalities

#### Question

A bookstore is purchasing boxes of paperbacks and hardcovers from a distributor. The delivery van can carry no more than $275$ pounds in a single trip. Each box of paperbacks weighs $4.2$ pounds, and each box of hardcovers weighs $7.5$ pounds. The store also wants to buy at least twice as many boxes of paperbacks as boxes of hardcovers. Let $p$ represent the number of paperback boxes and $h$ represent the number of hardcover boxes, where $p$ and $h$ are nonnegative integers. Write a system of inequalities that best models this situation.

#### Explanation

First, we translate each condition into an inequality, as follows:

- The total weight cannot exceed $275$ pounds. Since each paperback box weighs $4.2$ pounds and each hardcover box weighs $7.5$ pounds, we have

- The store wants the number of paperback boxes to be at least twice the number of hardcover boxes, so we have

Therefore, putting it all together, the system of inequalities that models this situation is the following:

$$


\begin{aligned}4.2𝑝+7.5ℎ≤275 \\ 𝑝≥2ℎ\end{aligned}


$$

### Example: Modeling Using Two Inequalities and Checking a Possible Solution

#### Question

An art teacher is buying $t$ canvases and $u$ paintbrush sets for a school workshop. The teacher needs to purchase at least $28$ items in total, but wants to spend no more than $360.$ Each canvas costs $12$ and each paintbrush set costs $6.$

Write a system of inequalities that models this situation, and check whether the pair $(t,u)=(10,20)$ is valid for your system or not.

#### Explanation

First, we translate each part of the problem into an inequality:

- There must be at least $28$ items in total, so we have

- We're told that the total cost cannot exceed $360.$ Since each canvas costs $12$ and each paintbrush set costs $6,$ we have

Therefore, putting it all together, the system of inequalities that models this situation is the following:

$$


\begin{aligned}𝑡+𝑢≥28 \\ 12𝑡+6𝑢≤360\end{aligned}


$$

To check if the pair $(t,u)=(10,20)$ is a solution of the system, we substitute it into the inequalities:

$$


\begin{aligned}10+20≥28 \\ 12(10)+6(20)≤360\end{aligned}


$$

Since all inequalities are satisfied, the pair $\boxed{\text{is}}$ a solution to the system.

Thus, purchasing $10$ canvases and $20$ paintbrush sets $\boxed{\text{is}}$ a valid option for the teacher.

### Modeling With Multiple Constraints

Sometimes, a situation has *more than two conditions* that must be satisfied. Let’s return to the bakery manager example from the beginning of the lesson. The manager wanted

- to buy at least $36$ items, and

- to spend no more than $180.$

Recall that the system of inequalities that models this situation looked as follows:

$$


\begin{aligned}𝑥+𝑦≥36 \\ 8𝑥+2𝑦≤180\end{aligned}


$$

In addition to these conditions, suppose the manager also decides to buy:

- more than $5$ trays, which can be written as

- no more than $50$ boxes, which can be written as

Therefore, the full system is now the following:

$$


\begin{aligned}𝑥+𝑦≥36 \\ 8𝑥+2𝑦≤180 \\ 𝑥>5 \\ 𝑦≤50\end{aligned}


$$

Let's see some more examples.

### Example: Modeling a Situation Using Multiple Inequalities

#### Question

A logistics company is hiring $r$ drivers and $l$ loaders for a regional operation. The company must hire at least $24$ people in total, but wants to keep the total weekly pay at no more than $28{,}400.$ Each driver will be paid $1{,}050$ per week, each loader will be paid $650$ per week, and the company must hire at least $9$ drivers and at least $8$ loaders.

Write a system of inequalities that models this situation, and check whether the pair $(r,l)=(12,12)$ is valid for your system or not.

#### Explanation

First, we translate each condition into an inequality:

- We're told that the total weekly pay cannot exceed $28{,}400.$ Since each driver costs $1{,}050$ and each loader costs $650,$ we have

- The total number of people hired must be at least $24,$ so we have

- The company must hire at least $9$ drivers, so we have

- The company must also hire at least $8$ loaders, so we have

Thus, putting it all together, the system of inequalities that models this situation is the following:

$$


\begin{aligned}1,050𝑟+650𝑙≤28,400 \\ 𝑟+𝑙≥24 \\ 𝑟≥9 \\ 𝑙≥8\end{aligned}


$$

To check if the pair $(r,l)=(12,12)$ is a solution of the system, we substitute it into the inequalities:

$$


\begin{aligned}1,050(12)+650(12)≤28,400 \\ 12+12≥24 \\ 12≥9 \\ 12≥8\end{aligned}


$$

Since all inequalities are satisfied, the pair $\boxed{\text{is}}$ a solution to the system.

Thus, hiring $12$ drivers and $12$ loaders $\boxed{\text{is}}$ a valid option for the company.
