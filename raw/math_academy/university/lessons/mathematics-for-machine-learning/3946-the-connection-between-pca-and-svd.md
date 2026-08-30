# The Connection Between PCA and SVD

Source: https://www.mathacademy.com/topics/3946?courseId=145
Topic ID: 3946

## Prerequisites

- [Singular Value Decomposition of Larger Matrices](./3133-singular-value-decomposition-of-larger-matrices.md)
- [Computing Principal Components](./3945-computing-principal-components.md)

## Lesson

### Introduction

Let $X$ be an $n \times m$ observation matrix with standardized data, where each row represents one observation and each column represents one feature.

Suppose we have the following **singular value decomposition** (SVD) of $X{:}$

$$


X = U \Sigma V^T


$$

Note that in the SVD, the columns of $U$ are orthonormal, which implies that $U^T U = I$ (the identity matrix).

Using this decomposition, the sample covariance matrix of $X$ can be derived as follows:

$$


\begin{aligned}𝐶 & =\frac{1}{𝑛−1}𝑋^{𝑇}𝑋 \\ & =\frac{1}{𝑛−1}(𝑈Σ𝑉^{𝑇})^{𝑇}(𝑈Σ𝑉^{𝑇}) \\ & =\frac{1}{𝑛−1}(𝑉Σ^{𝑇}𝑈^{𝑇})(𝑈Σ𝑉^{𝑇}) \\ & =\frac{1}{𝑛−1}𝑉Σ^{𝑇}\underset{𝐼}{\underset{}{(𝑈^{𝑇}𝑈)}}Σ𝑉^{𝑇} \\ & =𝑉(\frac{1}{𝑛−1}Σ^{𝑇}Σ)𝑉^{𝑇}.\end{aligned}


$$

The expression $\dfrac{1}{n-1}\Sigma^T \Sigma$ represents the diagonal form of the covariance matrix $C.$

Now, notice the following:

- The matrix $\dfrac{1}{n-1}\Sigma^T \Sigma$ is a diagonal $m \times m$ matrix with the eigenvalues of $C$ (in descending order) on the main diagonal.

- The matrix $V$ is an $m \times m$ matrix whose columns are the unit eigenvectors of $C.$

To summarize, if we write down the singular value decomposition of the standardized observation matrix $X,$ the columns of the matrix $V$ in the SVD are the **principal components** of the data.

### Example: Finding a Principal Component from SVD

#### Question

$$


\begin{aligned}\frac{2}{\sqrt{√5}} & −\frac{1}{\sqrt{√5}} \\ \frac{1}{\sqrt{√5}} & \frac{2}{\sqrt{√5}}\end{aligned}


$$

Consider the matrices $U$ and $V$ above. Let $X$ be a $2 \times 3$ standardized observation matrix, where each row represents one observation and each column represents one feature. Given that $X = U \Sigma V^T$ is a singular value decomposition of $X,$ what is the third principal component of the data?

#### Explanation

Recall that the unit eigenvectors of the covariance matrix $C$ are called the principal components of the data. If

$$


\lambda_1 \gt \lambda_2 \gt \lambda_3


$$

are the eigenvalues of $C$ written in descending order, then:

- the $1$st principal component is the unit eigenvector $\mathbf{v}_1$ corresponding to the $1$st eigenvalue $\lambda_1,$

- the $2$nd principal component is the unit eigenvector $\mathbf{v}_2$ corresponding to the $2$nd eigenvalue $\lambda_2,$

- the $3$rd principal component is the unit eigenvector $\mathbf{v}_3$ corresponding to the $3$rd eigenvalue $\lambda_3.$

Notice that the covariance matrix corresponding to $X$ is

$$


\begin{aligned}𝐶 & =\frac{1}{𝑛−1}𝑋^{𝑇}𝑋 \\ & =\frac{1}{𝑛−1}(𝑈Σ𝑉^{𝑇})^{𝑇}(𝑈Σ𝑉^{𝑇}) \\ & =\frac{1}{𝑛−1}𝑉Σ^{𝑇}(𝑈^{𝑇}𝑈)Σ𝑉^{𝑇} \\ & =𝑉(\frac{1}{𝑛−1}Σ^{𝑇}Σ)𝑉^{𝑇},\end{aligned}


$$

where the final expression represents the diagonal form of the covariance matrix $C.$ Notice the following:

- The matrix $\dfrac{1}{n-1}\Sigma^T \Sigma$ is a diagonal $3 \times 3$ matrix, where the entries on the main diagonal are the eigenvalues (written in descending order) of the covariance matrix $C.$

- The matrix $V$ is a $3 \times 3$ matrix, whose columns are the corresponding unit eigenvectors of the covariance matrix $C.$

Therefore, the columns of $V$ are the principal components of the data. So, the third principal component is

$$


\begin{aligned}\frac{1}{3} \\ −\frac{2}{3} \\ \frac{2}{3}\end{aligned}


$$

### Total Variance of the Observation Matrix

Suppose we have a sample of $n$ observations, where each observation has $m$ features. We store this data in the $n \times m$ observation matrix $X,$ where each row represents one observation and each column represents one feature.

$$


\begin{aligned}𝑥_{11} & 𝑥_{12} & … & 𝑥_{1𝑚} \\ 𝑥_{21} & 𝑥_{22} & … & 𝑥_{2𝑚} \\ ⋮ & ⋮ & ⋱ & ⋮ \\ 𝑥_{𝑛1} & 𝑥_{𝑛2} & … & 𝑥_{𝑛𝑚}\end{aligned}


$$

We assume the data has been mean-centered. Let $\mathbf{x}_j$ denote the $j$th column of $X.$ The sample covariance matrix, $C_X,$ is given by

$$


\begin{aligned}Var[𝐱_{1}] & … & Cov[𝐱_{1},𝐱_{𝑚}] \\ ⋮ & ⋱ & ⋮ \\ Cov[𝐱_{𝑚},𝐱_{1}] & … & Var[𝐱_{𝑚}]\end{aligned}


$$

The **total variance** of the observed data equals the sum of the entries on the leading diagonal of $C_X$ (the trace of the matrix). That is,

$$


\textrm{Total Variance} = \textrm{Var}[\mathbf{x}_1] + \textrm{Var}[\mathbf{x}_2] + \cdots + \textrm{Var}[\mathbf{x}_m].


$$

How is the total variance related to the singular values of $X?$

We recall that using the singular value decomposition $X = U \Sigma V^T,$ the eigenvalues $\lambda_1,\ldots, \lambda_m$ of $C_X$ are related to the singular values $\sigma_1,\ldots, \sigma_m$ of $X$ by:

$$


\lambda_i = \dfrac{\sigma_i^2}{n-1} \quad \text{for } i=1,\ldots,m.


$$

Next, we will use this relationship to compute the total variance.

### Finding the Total Variance

To find the total variance in terms of singular values, define the change of variables $Y = XV.$ The covariance of $Y$ is given by

$$


\begin{aligned}𝐶_{𝑌}=\frac{1}{𝑛−1}𝑌^{𝑇}𝑌=\frac{1}{𝑛−1}(𝑋𝑉)^{𝑇}(𝑋𝑉)=𝑉^{𝑇}\underset{𝐶_{𝑋}}{\underset{}{(\frac{1}{𝑛−1}𝑋^{𝑇}𝑋)}}𝑉.\end{aligned}


$$

Since $V$ contains the eigenvectors of $C_X,$ the matrix $C_Y$ is diagonal and contains the eigenvalues $\lambda_i$ of $C_X{:}$

$$


\begin{aligned}𝜆_{1} & … & 0 \\ ⋮ & ⋱ & ⋮ \\ 0 & … & 𝜆_{𝑚}\end{aligned}


$$

The total variance is defined as the trace (sum of diagonal elements) of the covariance matrix. A key property of the trace is that it is invariant under orthogonal transformations like $Y=XV.$ Therefore, the total variance of $Y$ is the same as the total variance of $X{:}$

$$


\textrm{Total Variance} = \text{Tr}(C_X) = \text{Tr}(C_Y) = \sum_{i=1}^m \lambda_i.


$$

Substituting $\lambda_i = \frac{\sigma_i^2}{n-1},$ we conclude that the total variance is *proportional to* the sum of the squared singular values:

$$


\boxed{\textrm{Total Variance} \:\propto\: \sum_{i=1}^m \sigma^2_i.}


$$

Let's see an example.

### Computing the Remaining Variance After Dimensionality Reduction

A nutritionist measured $3$ features among a group of clients:

- body mass index ($x_1$)

- height ($x_2$)

- weight ($x_3$)

The collected data was stored in the mean-centered observation matrix $X,$ where each row contains measurements for a particular client. The nutritionist finds that the singular values of $X$ are

$$


\sigma_1=12, \qquad \sigma_2=5, \qquad \sigma_3=4.


$$

The nutritionist then decides to reduce the dimensionality of the data set. To do this, they convert the original observation matrix $X$ into a new matrix $Y$ using the equation

$$


Y = X V_1,


$$

where $V_1$ is the $3 \times 1$ matrix containing the first principal component of the data only. As a result, $Y$ is an $n \times 1$ matrix that gives a single feature associated with each client.

What percentage of the original variance is preserved in the new transformed matrix $Y$ compared to the initial observation matrix $X?$

The total variance over all features is proportional to the sum of the squared singular values:

$$


\begin{aligned}Total & ∝\underset{\underset{𝑖=1}{∑}}{\overset{}{3}}𝜎_{2𝑖}^{} \\ & =(12)^{2}+(5)^{2}+(4)^{2} \\ & =185.\end{aligned}


$$

Since the nutritionist used only the first principal component, the preserved variance is

$$


\begin{aligned}Preserved & ∝\underset{\underset{𝑖=1}{∑}}{\overset{}{1}}𝜎_{2𝑖}^{} \\ & =(12)^{2} \\ & =144.\end{aligned}


$$

Therefore, our required percentage can be computed as

$$


\begin{aligned}\frac{Preserved}{Total} & =\frac{144}{185} \\ & ≈0.778 \\ & =77.8\%.\end{aligned}


$$

To summarize:

- The nutritionist reduced the dimensionality of the data from $3$ (initially, each client had three features) to just $1$ (only one feature characterizes each client after the transformation).

- In doing so, $77.8\%$ of the variance is preserved in the transformed data.

### Example: Finding the Variance from SVD

#### Question

A financial analyst measured $5$ features, $x_1,x_2,\ldots,x_5,$ for each company among a group of companies under study. The collected data was stored in the standardized observation matrix $X,$ where each row contains measurements for a particular company.

The singular values of $X$ are

$$


\sigma_1=7, \quad \sigma_2=5, \quad \sigma_3=3, \quad \sigma_4=2, \quad \sigma_5=1.


$$

The analyst then converted the original observation matrix $X$ into a new matrix $Y$ using the equation $Y = X V_2,$ where $V_2$ is the $5 \times 2$ matrix consisting of the first two principal components of the data. What percentage of the original variance is preserved in the new transformed matrix $Y$ compared to the initial observation matrix $X?$

#### Explanation

Let $V$ be the matrix of principal components. Then, applying the change of variables

$$


Y = XV


$$

we can convert our observation matrix $X$ into a new matrix $Y$ of (linearly) transformed observations such that

- the covariance matrix of $Y$ is diagonal (meaning that the new features $y_1,y_2,\ldots,y_5$ are uncorrelated),

- the features $y_1,y_2,\ldots,y_5$ are arranged in order of decreasing variance, and

- the squares of the singular values $\sigma_1^2, \sigma_2^2, \ldots, \sigma_5^2$ represent the variances in the respective features $y_1,y_2,\ldots,y_5.$

Now, the total variance over all features is proportional to the sum of the squared singular values:

$$


\begin{aligned}Total & ∝\underset{\underset{𝑖=1}{∑}}{\overset{}{5}}𝜎_{2𝑖}^{} \\ & =(7)^{2}+(5)^{2}+(3)^{2}+(2)^{2}+(1)^{2} \\ & =88\end{aligned}


$$

Since the analyst used only the first two principal components, the remaining variance is

$$


\begin{aligned}Remaining & ∝\underset{\underset{𝑖=1}{∑}}{\overset{}{2}}𝜎_{2𝑖}^{} \\ & =(7)^{2}+(5)^{2} \\ & =74.\end{aligned}


$$

Therefore, our required percentage can be computed as

$$


\begin{aligned}\frac{Remaining}{Total} & =\frac{74}{88} \\ & ≈0.841 \\ & =84.1\%.\end{aligned}


$$
