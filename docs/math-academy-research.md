# Math Academy Research Notes For TorchBloom

**Date:** 2026-06-11  
**Status:** Research note before TorchBloom knowledge-graph design  
**Purpose:** Capture what Math Academy appears to do, why it works, how its practice loop likely feels to learners, and what TorchBloom should borrow or deliberately change before designing a math/coding knowledge-graph pilot.

## Executive Summary

Math Academy is best understood as an expert-system learning platform, not as a chat tutor or content library. Its core asset is a fine-grained mathematical knowledge graph connected to a student model, diagnostic algorithm, spaced-repetition logic, and task-selection algorithm. The system tries to answer one operational question at every moment: what task should this learner do next to produce the most learning per unit of focused time?

For TorchBloom, the lesson is not "make a wiki like Math Academy." The lesson is to build a structured graph of small, testable knowledge units, attach practice evidence to each unit, and use source material like *Understanding Deep Learning* as a target map rather than a prose destination. The existing UDL wiki should remain a source-grounded target layer; the next learner-facing work should be a prerequisite graph plus practice loop.

Math Academy's public materials strongly support these design principles:

- Fine-grained topic graph before app polish.
- Adaptive diagnostic before fixed course path.
- Mastery and automaticity before progression.
- Difficult equations made approachable by decomposing them into many small prerequisite moves.
- Worked example before independent practice.
- Immediate feedback after each attempt.
- Question design that connects errors back to specific prerequisite gaps.
- Spaced, mixed, and interleaved review.
- Lightweight gamification around effort, not decoration.
- Progression based on a learner's "knowledge frontier," not age or grade alone.

TorchBloom should borrow the graph, mastery, review, and task-selection ideas, but should not copy Math Academy wholesale. TorchBloom's domain includes coding, data, explanation, projects, and deep learning artifacts, so its practice model must support open-ended code, written explanation, project rubrics, and source-grounded concept bridges in addition to multiple-choice math checks.

## Source Reliability

| Level | Sources Used | How To Treat |
| --- | --- | --- |
| Primary | Math Academy official pages: [home](https://www.mathacademy.com/), [How It Works](https://www.mathacademy.com/how-it-works), [Pedagogy](https://www.mathacademy.com/pedagogy), [How Our AI Works](https://www.mathacademy.com/how-our-ai-works), [FAQ](https://www.mathacademy.com/faq), [courses](https://www.mathacademy.com/courses), [Mathematics for Machine Learning](https://www.mathacademy.com/courses/mathematics-for-machine-learning), [Mathematical Foundations I](https://www.mathacademy.com/courses/mathematical-foundations-i), [Linear Algebra](https://www.mathacademy.com/courses/linear-algebra), [Probability & Statistics](https://www.mathacademy.com/courses/probability-and-statistics) | Verified claims about Math Academy's stated system, pedagogy, curriculum, and workflow. |
| Secondary | [Recess MathAcademy review](https://recess.gg/think/math-curriculum-review-mathacademy/), [Atrium provider page](https://www.exploreatrium.com/providers/math-academy), public screenshot images linked from those pages | Useful for visible learner experience and external critique; label as observation, not official fact. |
| Research Background | [Bloom's 2 Sigma Problem PDF](https://web.mit.edu/5.95/readings/bloom-two-sigma.pdf), [DAS3H spaced practice model](https://arxiv.org/abs/1905.06873), [HGKT hierarchical exercise graph](https://arxiv.org/abs/2006.16915), [Freeman active-learning meta-analysis summary](https://www.wired.com/2014/05/empzeal-active-learning), [Educational prerequisite graph paper](https://arxiv.org/abs/2509.05393), [math distractor generation study](https://arxiv.org/abs/2404.02124), [math distractor and feedback generation study](https://arxiv.org/abs/2308.03234), [MCQ student-reasoning study](https://arxiv.org/abs/1909.01455) | Supports the general learning-science and question-design direction, not proof that Math Academy specifically achieves every outcome it claims. |

Important limitation: I did not log into a paid Math Academy account. Details about exact item formats, answer-entry widgets, internal algorithms, and full reports are inferred from public official descriptions plus public screenshots and reviews.

## What Math Academy Is

Math Academy describes itself as an AI-powered, fully automated online math-learning platform. Publicly, "AI" does not appear to mean a generative chat interface. Their official "How Our AI Works" page describes an expert system made of four main parts:

- A knowledge graph storing mathematical topics and relationships.
- A student model that overlays learner answers on the graph.
- A diagnostic algorithm that estimates the learner's knowledge frontier.
- A task-selection algorithm that chooses what to learn or review next.

The homepage states that Math Academy combines cognitive learning strategies with adaptive knowledge graph technology. The "How It Works" page says the pedagogy is mastery-based and uses distributed practice, interleaving, mixed review, and knowledge graph technology. This matters for TorchBloom because the platform's intelligence is mostly in curriculum structure and sequencing, not in conversational tutoring.

## The Knowledge Graph

Math Academy's graph appears to be more than a list of textbook sections. The official AI page says the graph stores:

- Mathematical topics.
- Easier and harder problem variations within topics.
- Background knowledge required to learn a topic.
- Specific prerequisites that might explain struggle on a problem.
- Relationships among topics, including prerequisites and more detailed sub-topic relationships.

Their public examples describe topics as graph nodes and arrows as relationships. One example uses "Adding Fractions With Unlike Denominators" and prerequisite fraction topics. Their broader graph spans multiple thousands of linked topics from 4th grade through university-level math. A course is presented as a section of that larger graph.

For TorchBloom, this implies the graph should not be a book outline. It should be a prerequisite-and-practice structure with explicit node relationships. A node like `linear-regression` is too large unless it decomposes into smaller nodes such as `plot-points-on-coordinate-plane`, `linear-function-slope-intercept`, `prediction-error`, `squared-error`, `sum-of-squared-errors`, and `choose-parameters-to-minimize-loss`.

## Evidence: How Hard Equations Become Understandable

The strongest public evidence is not that Math Academy rewrites hard equations in a casual way. It is that Math Academy decomposes hard symbolic work into very small graph nodes, then controls the order, representation, feedback, and review schedule.

Official evidence from Math Academy:

- The pedagogy page says their calculus course has about 1,000 smaller steps instead of roughly 100 textbook-style steps. It describes about 300 topics times three knowledge points or stages of difficulty.
- The same page says each knowledge point starts with a worked example, uses subgoal labeling to group steps into meaningful units, and uses visualizations and diagrams when possible.
- The "How It Works" page says lessons are scaffolded into very small knowledge points, followed by concrete examples that focus attention on essential problem-solving steps.
- The "How Our AI Works" page says the graph stores prerequisite knowledge, easier and harder variations of problems, and specific background knowledge relevant when a student struggles.

The course catalogs give concrete evidence of how this decomposition works. Math Academy's Mathematics for Machine Learning course does not jump straight to neural networks or backpropagation. It first builds language and notation: sets, predicates, supremum/infimum, argmax/argmin, Boolean functions, matrices, vector spaces, inner products, projections, least squares, partial derivatives, gradients, Jacobians, matrix gradients, optimization, probability, random variables, expectation, variance, and inference. Its list explicitly separates:

- `Argmax and Argmin Notation` from `Finding Argmax and Argmin From Tables and Graphs`.
- `Introduction to Partial Derivatives` from `Computing Partial Derivatives`, `Geometric Interpretations`, `Gradient Vector`, `Jacobian`, `Vector Gradients`, and `Matrix Gradients`.
- `Linear Least-Squares Problems` from `Linear Regression With Matrices`, `Polynomial Regression With Matrices`, and `Multiple Linear Regression With Matrices`.
- `Probability`, `Bayes' Theorem`, `Random Variables`, `PDFs`, `CDFs`, `Transformations`, `Expectation`, `Variance`, and named distributions.

The Mathematical Foundations I catalog shows the same pattern earlier in the pipeline. "Functions" is not one lesson. It is split into introduction, visual representations, graphs, domain, range, roots, increasing/decreasing behavior, piecewise functions, modeling with linear functions, and constructing linear functions. This matters for TorchBloom because "understand ReLU" is not one node. It depends on functions, graphs, piecewise definitions, slope, input-output tables, and symbolic substitution.

Interpretation for TorchBloom:

- "Easy to understand" should mean "low cognitive load per step," not "watered down."
- Each equation should become a ladder of representation changes: words, table, graph, formula, code, and back.
- A hard formula should be introduced only after its notation and component actions have appeared as earlier nodes.
- A learner should practice the exact structural move the equation requires before seeing it in full form.

## Evidence: Why The Question Design Appears Strong

Math Academy's public materials imply that questions are not isolated items. They are graph probes. A question is useful because it can update the learner model, reveal prerequisite gaps, trigger review, and decide whether to unlock later tasks.

Official evidence:

- The AI page says the graph stores easiest and hardest variations within topics, background knowledge required for each topic, and the specific background knowledge most relevant when a student struggles with a problem type.
- The diagnostic algorithm uses the graph to minimize the number of questions needed to estimate a learner's knowledge profile.
- Correct diagnostic answers provide positive evidence for the topic, prerequisites, and related topics; incorrect answers provide negative evidence for the topic, postrequisites, and related topics.
- Slow correct answers are discounted because they may show weak automaticity.
- During lessons, the learner receives up to five practice problems; two correct in a row moves them forward, while errors produce additional problems.
- Every question has an explanation.
- Quizzes occur roughly every 150 XP, cover mixed recent topics, block access to examples during assessment, and trigger review on missed topics.
- The FAQ says failed lessons are re-served within days and the system prioritizes prerequisite review that may have caused the confusion.

Secondary evidence from the Recess review:

- Practice sets are described as short introductions followed by well-thought-out problem sets.
- Explanations are described as clear for every answer, right or wrong.
- The reviewer says exercises are multiple choice and "cleverly designed to catch common mistakes."
- Error analysis is described as detailed and specific, with step-by-step solutions and extra practice on frequently missed concepts.

Research background:

- Research on math multiple-choice question generation emphasizes that high-quality distractors are not random wrong answers; they should target common errors or misconceptions.
- The same research finds that LLMs can produce mathematically plausible distractors but are weaker at anticipating common student misconceptions. This is a warning for TorchBloom: generated choices need human review and misconception labels.
- A physics education study on multiple-choice explanations shows that answer choices can reveal richer student reasoning when learners are asked to explain why each choice could seem plausible. This suggests TorchBloom should sometimes ask for "why this wrong answer is tempting," not only "pick the right answer."

Question-design inference:

Math Academy's question quality likely comes from four combined design decisions:

1. **Graph-linked item design:** every problem maps to topics, prerequisites, postrequisites, and related skills.
2. **Variation control:** items vary from easy to hard within a topic instead of treating a topic as a flat bucket.
3. **Misconception-aware feedback:** wrong answers can drive specific explanations and prerequisite repair.
4. **Assessment separation:** lesson practice is scaffolded and reference-friendly, while quizzes are mixed, timed, and unsupported.

For TorchBloom, this means a good practice item schema must include more than a prompt and answer. It should record tested nodes, prerequisite nodes, likely misconceptions, distractor rationale, explanation, mastery signal, response-time expectation when relevant, and follow-up action after error.

## Concrete Question Patterns To Borrow

TorchBloom should prototype question patterns that match Math Academy's strengths while extending them to coding and AI.

| Pattern | Math Academy Evidence | TorchBloom Version |
| --- | --- | --- |
| Worked example pair | Official pages say each knowledge point begins with a worked example before similar practice. | Show one solved table/graph/formula/code example, then ask the learner to solve a near-transfer version. |
| Two-correct progression | Official lesson flow says two correct in a row advances the learner; errors trigger more problems. | Use two correct familiar items to mark `practiced`; require mixed review later for `mastered`. |
| Misconception distractor | Recess says answer choices catch common mistakes; research says distractors should target misconceptions. | Every multiple-choice item must label why each wrong option is tempting. |
| Slow-correct evidence | Official diagnostic and FAQ say response time affects mastery/automaticity. | Track time only for fluency nodes like arithmetic, substitution, and syntax; do not over-time deep reasoning. |
| Mixed quiz | Official pages say quizzes cover recent mixed topics and trigger review. | Use mixed "readiness checks" before projects or UDL chapter bridges. |
| Implicit review | Official FIRe description says advanced topics can partially count as review for simpler encompassed topics. | A coding task using slope and squared error can credit those math nodes, but only fractionally and only when the task really exercises them. |
| Prerequisite repair | Official FAQ says failed lessons trigger review of prerequisite knowledge. | If a learner misses squared error, repair may go to subtraction, squaring, coordinate reading, or formula substitution depending on error type. |

## Example: Rebuilding A Hard Formula The Math Academy Way

For UDL Ch2 linear least-squares loss, the final target might look like:

```text
L[phi] = sum_i (f[x_i, phi] - y_i)^2
```

A Math Academy-inspired TorchBloom path should not start there. It should build the equation as a stack:

1. Read a point from a table: input `x`, target `y`.
2. Use a simple function rule to make one prediction.
3. Compute one prediction error: prediction minus target.
4. Square one error and explain why negative errors become positive.
5. Add squared errors across two or three examples.
6. Change one parameter and compare total loss.
7. Translate the repeated table procedure into summation notation.
8. Read the final UDL-style loss formula as a compact version of the table.
9. Implement the same computation in a short Python loop.

This is the main design lesson: equations become understandable when the learner has already performed each hidden operation in a simpler representation.

## The Student Model

Math Academy's student model tracks a learner's answers against the knowledge graph and estimates a knowledge profile. It is not just a binary mastered/not-mastered flag. Official pages repeatedly emphasize:

- Correctness.
- Response time.
- Automaticity.
- Spaced repetitions accumulated per topic.
- Conditional completion when diagnostic evidence is weak.
- Falling backward when later struggle reveals missing foundations.

This is important. Math Academy treats fast, reliable recall as different from slow correct answering. The FAQ says diagnostics and quizzes are timed partly because they are measuring automaticity, not only correctness.

For TorchBloom, the first student model can be much simpler, but it should still distinguish:

- `introduced`: learner has seen the idea.
- `practiced`: learner can solve familiar examples.
- `mastered`: learner can solve mixed examples reliably.
- `durable`: learner has successful delayed review.
- `transfer-ready`: learner can use the skill inside a coding task, explanation, or project.

## Diagnostics And Knowledge Frontier

Math Academy starts with an adaptive diagnostic. Official pages describe a 30-45 minute diagnostic that can be paused and resumed. The diagnostic:

- Places the learner at the right point in a selected course.
- Identifies mastered course topics.
- Identifies missing foundational knowledge from earlier courses.
- Produces a report with placement recommendation, estimated completion dates under different XP goals, foundational gaps, mastery by topic, assessed topics, and performance.

Their AI page says a naive diagnostic would require far too many questions because a course and its foundations can involve 500-1,000 topics. Their claimed strategy compresses the graph into a smaller coverage set and chooses assessment topics that provide the most information about the learner's profile. Correct answers provide positive evidence for the topic and related prerequisites; incorrect answers provide negative evidence for the topic, postrequisites, and related topics. Slow correct answers receive less weight.

For TorchBloom, a pilot diagnostic should not try to infer hundreds of nodes at first. It should target one graph slice, for example UDL Ch2-3 readiness, and use 12-20 questions to identify the learner's frontier across arithmetic/algebra, functions, coordinates, basic coding, and early model-fitting concepts.

## Task Selection

Math Academy's task-selection objective is explicit: maximize learning per unit of time. Official materials say the system chooses what a student should learn next, what they need to review, and when to shore up missing foundations.

The task selector uses several principles:

- Move forward immediately after prerequisites are mastered.
- Continue reviewing prior material only as much as needed.
- Teach dissimilar concepts together to reduce associative interference.
- Use layering so advanced topics reinforce earlier component skills.
- Balance current-course progress with foundational remediation.
- Use student choice among unlocked tasks to preserve agency.

The important product insight is that "adaptive" is not just easier/harder. It is a constrained scheduling problem over a graph: some tasks are new lessons, some are reviews, some are quizzes, and some are prerequisite repairs.

## Practice Loop

The official "How It Works" page gives a concrete practice flow:

1. The student sees a set of available learning tasks.
2. Tasks vary by topic, type, and XP.
3. A lesson begins with a tutorial introducing a concept and method.
4. Each small knowledge point starts with a fully worked example.
5. The system then gives concrete examples focused on the essential problem-solving steps.
6. The learner receives up to five practice problems.
7. If the learner gets two practice problems correct in a row, they move to the next example or knowledge point.
8. If not, the system gives additional problems.
9. Every question has an explanation.
10. On task completion, the graph is updated and new tasks unlock.

That is a tight instructional loop:

```text
small explanation
  -> worked example
  -> similar practice
  -> immediate feedback
  -> mastery check
  -> graph update
  -> next selected task
```

The secondary Recess review says the practice problems are multiple choice and that explanations are provided for both correct and incorrect answers. Because that claim is not official, TorchBloom should treat it as a useful observation, not a hard fact. Public screenshots show a clean dashboard with task cards, XP values, progress bars, prerequisites, and a course progress panel.

## Quizzes, Reviews, And Automaticity

Math Academy schedules quizzes roughly every 150 XP. Official pages say quizzes:

- Cover a mix of recent topics.
- Are timed.
- Prevent reference to examples or lesson material.
- Trigger immediate review tasks for missed topics.
- Can be retaken after review.

The FAQ says quiz timing is adjustable for accommodations, and that both correctness and response time count as evidence of mastery and automaticity. It also says that if a student misses or takes too long on quiz topics, the system assigns review.

This gives TorchBloom a useful distinction:

- Lesson practice can be supported, untimed, and scaffolded.
- Mastery evidence should eventually be unsupported and mixed.
- Automaticity matters for lower-level math and coding syntax, but should not dominate creative problem solving or projects.

## XP And Motivation

Math Academy uses XP as a measure of focused effort. Official materials say one XP is roughly one minute of focused effort. Students have daily XP goals; parents or oversight accounts can adjust schedules. XP is awarded based on performance, with partial credit possible and rare negative XP for rushing or guessing. Perfect scores can earn bonus XP.

Public screenshots show:

- Course progress percentage.
- Estimated completion date.
- Total XP.
- Today/week XP.
- Daily XP goal progress.
- Weekly bar chart.
- League leaderboard.
- Lesson cards with XP values.

The gamification is deliberately lightweight. It does not appear to use a cartoon or narrative game layer. The motivational loop is effort, progress, league placement, and visible completion.

For TorchBloom, this argues for "honest progress" rather than heavy game mechanics. A young learner may still need warmer UI and mentor-visible feedback, but the core reward should remain mastery, not decoration.

## Curriculum Scope And Granularity

Math Academy begins at 4th-grade math. The FAQ says a student ready for 4th Grade Math should know multiplication facts through 12s. Courses span elementary, middle school, high school, AP, test prep, foundations, and university-level math. The course catalog includes Linear Algebra, Multivariable Calculus, Methods of Proof, Probability & Statistics, and Mathematics for Machine Learning.

The granularity is notable. The pedagogy page says a normal calculus textbook might have around 100 steps, while Math Academy's calculus course has about 1,000 smaller steps, roughly 300 topics times three knowledge points or difficulty stages. The Mathematics for Machine Learning course publicly lists detailed sections such as set theory, logic, vector geometry, matrices, vector spaces, diagonalization, orthogonality, SVD, regression, multivariable calculus, optimization, probability, random variables, expectation, joint distributions, covariance, and parametric inference.

The Mathematical Foundations I page shows how early and middle foundations are decomposed: systems of equations, functions, piecewise functions, modeling with linear functions, rational expressions, radicals, distance/rate graphs, and many other small topics. This is useful for TorchBloom because UDL readiness is not just "learn algebra." It is a graph of many small prerequisite moves.

## What Practice Probably Feels Like

Based on official descriptions plus public screenshots and secondary reviews, the learner experience likely feels like this:

- The learner opens a simple dashboard, not a game world.
- The left side shows course progress, XP, completion estimate, weekly activity, and league.
- The main area shows a list of available tasks.
- Some task cards are locked; current tasks can show progress, prerequisites, and resume buttons.
- The learner chooses among unlocked tasks, but the algorithm controls what appears.
- Inside a lesson, the learner reads a concise explanation and worked example.
- The learner solves short practice questions immediately.
- Feedback is immediate and explanatory.
- The learner needs a notebook or scratch paper; the system is not primarily a manipulative environment.
- Reviews and quizzes reappear old material in mixed contexts.
- A learner who rushes or guesses is penalized by lower XP, review, or lesson retry.

This is closer to an adaptive, graph-driven workbook than a video course or chatbot.

## What Math Academy Does Not Seem To Do

From public information, Math Academy does not appear to center:

- Open-ended written proof review inside each task.
- Full free-response work capture for all problems.
- Coding assignments.
- Notebook execution.
- Project artifacts.
- Generative AI tutor chat as the main teaching mode.
- Rich digital manipulatives.
- A child-centered narrative world.

The Recess review specifically criticizes the lack of interactive manipulatives, open-ended work review, and built-in help beyond written explanations. Those gaps matter for TorchBloom because AI learning needs code, experiments, explanations, and projects.

## Implications For TorchBloom

TorchBloom should borrow Math Academy's system shape, not its exact surface:

```text
source target
  -> concept/prerequisite graph
  -> diagnostic
  -> task selection
  -> small lesson/practice loop
  -> mastery evidence
  -> spaced and mixed review
  -> project transfer
```

The current UDL source layer is valuable because it gives the target: what deep learning eventually requires. But a learner does not need a broad LLM wiki first. They need graph nodes and tasks that build toward UDL.

For a UDL Ch2-3 pilot, the first graph should include:

- Arithmetic fluency: integer operations, fractions, decimals, squares.
- Algebra: variables, substitution, linear expressions, solving simple equations.
- Functions: input/output, parameters, graphs, domain/range, piecewise functions.
- Coordinates and data: points, tables, scatterplots, slope, intercept.
- Early modeling: prediction, error, squared error, sum of errors, fitting by comparison.
- Programming: variables, expressions, functions, lists, loops, conditionals, plotting.
- ML targets: supervised learning, linear regression, least-squares loss, ReLU, shallow network as composed functions.

Probability should be treated as critical but staged. For UDL Ch2-3, probability is not the first blocker; functions, algebra, graphs, and programming are. Probability becomes a central blocker for measuring performance, classification, cross-entropy, generative models, uncertainty, and later UDL chapters. The pilot should include probability foundations only where they support data and uncertainty intuition, then expand probability in a later graph slice.

## Proposed TorchBloom Adaptations

| Math Academy Pattern | TorchBloom Adaptation |
| --- | --- |
| Mathematical topic graph | Cross-domain graph with math, coding, data, ML, explanation, and project nodes. |
| Diagnostic estimates knowledge frontier | Diagnostic estimates readiness for a target project or UDL chapter slice. |
| Worked example then practice | Worked example, guided practice, then explanation or coding transfer. |
| Multiple short practice problems | Mix of multiple-choice, numeric entry, written explanation, debugging, code completion, and tiny notebook tasks. |
| XP as focused effort | Use XP or effort minutes, but pair with mastery states and parent/mentor notes. |
| Spaced repetition per topic | Spaced review per node, with implicit review credit from projects and coding tasks. |
| Task selection maximizes learning per time | Task selection balances learning efficiency, curiosity, project momentum, and confidence. |
| Timed quizzes for automaticity | Timed checks only for low-level fluency; deep reasoning and coding should be untimed or generously timed. |
| Course as graph section | UDL target as graph destination; project path as graph route. |

## Pilot Design Requirements Derived From Research

Before building any app, TorchBloom needs these artifacts:

1. **Node schema:** small concepts with prerequisites, outcomes, source anchors, mastery evidence, and task types.
2. **Relationship schema:** prerequisite, encompassed-by, transfer-to, interferes-with, review-of, source-target.
3. **Practice schema:** prompt, item type, expected answer, feedback, misconceptions, mastery signal, estimated time, review interval.
4. **Diagnostic schema:** question, tested nodes, evidence weight, expected time, fallback/remediation target.
5. **Task-selection rule:** first deterministic version that can choose available lessons, reviews, and project steps from graph state.
6. **Review model:** simple spaced-review status before any advanced FIRe-like implicit repetition.
7. **Project transfer evidence:** a way for code or explanation tasks to count toward underlying graph nodes.
8. **Audit policy:** all UDL-derived claims must point back to `raw/udl/textbook/` or `wiki/udl/` anchors.

## Risks And Open Questions

- **Paid-account opacity:** Public sources do not expose full item formats or internal algorithms. Any detailed replica would require hands-on use or user-provided screenshots.
- **Multiple-choice limitation:** Multiple-choice can scale and diagnose common errors, but TorchBloom must also assess reasoning, code, and explanation.
- **Young learner fit:** Math Academy starts at 4th grade and expects self-regulation. TorchBloom's stated target can begin around 2nd-grade math, so the earliest stages need more visual, oral, mentor-supported, and concrete tasks.
- **Coding graph complexity:** Coding prerequisites are not ordered as linearly as arithmetic. The graph must allow loops, projects, debugging, and artifact-based evidence.
- **Probability timing:** Probability is essential for deep learning, but front-loading too much probability before functions/coding/modeling may slow the UDL Ch2-3 pilot.
- **Source-derived target risk:** UDL is licensed and should remain private source evidence. TorchBloom's learner graph should be original and source-informed, not a derivative public replacement for the book.

## Recommended Next Step

Use this research note to write a design spec for:

**UDL Ch2-3 Math + Coding Knowledge Graph Pilot**

The spec should define a graph-first pilot, not a broad wiki expansion. It should produce a small validated graph, a handful of diagnostics, practice item templates, and one project transfer path. The first project should be "fit a line from scratch," followed by a ReLU/piecewise-function lab that bridges into shallow neural networks.

The design should explicitly state that:

- `raw/udl/textbook/` is source evidence.
- `wiki/udl/` is target interpretation and source anchors.
- The new graph/pilot artifacts are curriculum products.
- The learner-facing app remains out of scope until the graph and practice contracts are validated.
