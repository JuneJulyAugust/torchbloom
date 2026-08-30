# Identifying Patterns of Association From Two-Way Tables

Source: https://www.mathacademy.com/topics/7936?courseId=39
Topic ID: 7936

## Prerequisites

- [Calculating Relative Frequencies From Two-Way Tables](./7935-calculating-relative-frequencies-from-two-way-tables.md)

## Lesson

### Introduction

A two-way table organizes counts for two categorical variables. A **categorical variable** is a characteristic whose possible values are categories. To look for a relationship between the variables, we do not just ask which count is largest. We ask whether the distribution of one variable changes from group to group.

Consider this survey table.

In this table, *grade level* is one variable, with Grade and Grade as its categories. *Preference* is another variable, with Drawing and Music as its categories.

The raw counts already suggest a difference. In Grade more students prefer drawing than music. In Grade more students prefer music than drawing.

The main question is whether that difference is meaningful when we compare the groups fairly. Since both grade levels have students, we can compare the parts within each row.

So, the table suggests that preference may be associated with grade level, because the pattern of preferences changes from Grade to Grade

### Conditional Relative Frequencies and Association

A **conditional relative frequency** is a fraction or percent calculated within a specified group. For a row comparison, divide each category count in a row by that row's total.

Using row relative frequencies allows us to fairly compare the distributions of the groups.

- For Grade the proportion that prefers drawing is and the proportion that prefers music is

- For Grade the proportion that prefers drawing is and the proportion that prefers music is

The distribution of preference changes from drawing and music in Grade to drawing and music in Grade

Here, the two categorical variables are *grade level* and *preference*. Because the conditional relative frequencies for preference are quite different between the two grade levels, the variables appear to be associated.

In general, compare the conditional relative frequencies for the groups. If the distributions are noticeably different, this suggests an association. If the distributions are similar, there is little evidence of an association.

**Watch out!** Equal row totals do not mean there is no association. We still need to compare the relative frequencies within the rows.

### Example: Identifying Whether Two Categorical Variables Appear to Be Associated

#### Question

Consider the two categorical variables shown in the two-way table above. Which of the following statements are true regarding whether the variables appear to be associated?

1. The distribution of one variable stays about the same across each category of the other variable.

2. The conditional relative frequencies differ meaningfully between groups.

3. The table suggests the two variables appear to be associated.

#### Explanation

To decide if there is an association between the variables, we examine whether the conditional relative frequencies (the distribution of preferences) change depending on the age group.

Let's calculate the row relative frequencies for each age group:

- For Children, the proportion that prefers hiking is and the proportion that prefers biking is

- For Teens, the proportion that prefers hiking is and the proportion that prefers biking is

- For Adults, the proportion that prefers hiking is and the proportion that prefers biking is

Now, we evaluate each statement in turn.

- Statement I is false. The distribution of preferences changes noticeably across the age groups. For example, the preference for hiking drops from for Children to for Adults.

- Statement II is true. As calculated above, the conditional relative frequencies differ meaningfully between the groups.

- Statement III is true. Because the distribution of preferred activities changes depending on the age group, the two variables appear to be associated.

Therefore, the correct answer is "II and III only."

### Describing Patterns of Association

Once we decide that two variables appear to be associated, we should describe the pattern using a clear comparison. A good description names the groups, names the category being compared, and uses relative frequencies rather than only raw counts.

Consider this table.

To compare the groups fairly, use the row relative frequencies for "Like Science."

Within Group A, the fraction who like science is

Within Group B, the fraction who like science is

Since a larger proportion of Group A likes science than Group B. A clear pattern statement is: “Liking science appears to be more common in Group A than in Group B, suggesting that science preference and group membership are associated.”

### Example: Comparing Relative Frequencies to Identify Patterns of Association

#### Question

The two-way table above records responses for two groups. What are the missing entries in the following statement comparing the conditional relative frequencies of the two groups to describe the pattern of association?

Within Class P, the fraction who prefer pizza is while within Class Q, the fraction who prefer pizza is

Since a fraction of Class P prefers pizza than Class Q, the two-way table suggests that preferring pizza is class membership.

#### Explanation

To compare the groups fairly, use the ** for "prefer pizza."

- Within Class P, the fraction who prefer pizza is

- Within Class Q, the fraction who prefer pizza is

Since both fractions have the same denominator, compare the numerators: So, is smaller than

That means a smaller fraction of Class P prefers pizza than Class Q.

Because the conditional relative frequencies are different, preferring pizza is ** class membership.

So the completed statement uses:

### Drawing Context-Based Conclusions Without Claiming Causation

Two-way tables can support conclusions about patterns in the observed data. They do not, by themselves, prove that one variable causes the other.

Suppose a survey compares whether students volunteer and whether they prefer group activities.

If the conclusion begins "Among students who volunteer," then the volunteer column is the group we condition on. The proportion who prefer group activities among students who volunteer is

Among students who do not volunteer, the proportion who prefer group activities is

Since a supported conclusion is: "Among students who volunteer, a greater proportion prefer group activities than among students who do not volunteer."

**Watch out!** We should not say, "Volunteering causes students to prefer group activities." The table shows a pattern in this survey, not proof of cause and effect.

### Example: Drawing Conclusions From a Two-Way Table in Real-World Contexts

#### Question

The two-way table above summarizes survey responses in a real-world context. Which of the following statements gives a conclusion that is supported by the relative-frequency comparison without claiming cause and effect?

1. Among students who own a pet, a greater proportion prefer outdoor activities than among students who do not own a pet.

2. Owning a pet causes students to prefer outdoor activities.

3. Preferring outdoor activities causes students to get a pet.

4. Students who do not own a pet are more likely to prefer outdoor activities than students who do own a pet.

5. Because more students prefer outdoor activities overall, every group must prefer outdoor activities.

#### Explanation

To evaluate the statements, we first calculate the proportion of students who prefer outdoor activities within each group.

- Among the students who own a pet, the total is Of those, prefer outdoor activities. The proportion is or

- Among the students who do not own a pet, the total is Of those, prefer outdoor activities. The proportion is or

Comparing the two groups, we see that This shows that among students who own a pet, a ** proportion prefer outdoor activities compared to students who do not own a pet.

This confirms Statement I. Let's check why the other statements are incorrect:

- Statements II and III, "Owning a pet causes students to prefer outdoor activities" and "Preferring outdoor activities causes students to get a pet," both claim causation. Two-way tables can show an association or pattern, but they do not prove a cause-and-effect relationship.

- Statement IV, "Students who do not own a pet are more likely to prefer outdoor activities than students who do own a pet," contradicts our finding that the proportion is greater for those who ** own a pet ().

- Statement V, "Because more students prefer outdoor activities overall, every group must prefer outdoor activities," is flawed reasoning, as overall totals do not guarantee that the preference holds identically for every subgroup.

Therefore, the correct conclusion is Statement I: "Among students who own a pet, a greater proportion prefer outdoor activities than among students who do not own a pet."
